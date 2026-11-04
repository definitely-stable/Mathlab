// HYP-105 AA4-FROZEN: true ORIGINAL source fixed-core GF5 palette obstruction.
// Every returned forbidden pattern has a complete physical, source-disjoint
// 2v2 or 3v3 witness involving one editable ORIGINAL ID and otherwise ONLY
// frozen ORIGINAL IDs. This does not solve multi-edit feasibility or root #230.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using std::array;
using std::uint64_t;
static constexpr int BASE=625, MAXM=28, NP=51;
static int add4[BASE*BASE], diff4[BASE*BASE];
static int pow5[4]={1,5,25,125};
static void require(bool ok,const char* msg){if(!ok)throw std::runtime_error(msg);}
struct Flag {
    int palette=0;
    array<int,4> support{};
    array<unsigned char,MAXM> c{};
};
struct Model {
    std::string scheme;
    int n=0,m=0;
    std::vector<Flag> flags;
    std::vector<array<int,4>> palettes;
    std::vector<int> edited,frozen;
};
static Model load(const std::string &name) {
    std::ifstream in(name);
    require(bool(in),"missing frozen-core SOURCE file");
    std::string version; Model z; int k;
    in>>version>>z.scheme>>z.n>>z.m>>k;
    require(version=="HYP105_FROZEN_CORE_V1","bad model format");
    require((z.n==425&&z.m==28)||(z.n==45&&z.m==12),
            "only genuine full W34/W32 source sizes");
    require(k>=1 && k<z.n,"invalid selected source-cover size");
    z.flags.resize(z.n);
    std::set<std::string> unique;
    for(int i=0;i<z.n;i++){
        Flag &f=z.flags[i]; in>>f.palette;
        require(bool(in)&&f.palette>=0&&f.palette<NP,"invalid source palette ID");
        std::set<int> support;
        for(int q=0;q<4;q++){
            in>>f.support[q];
            require(bool(in)&&f.support[q]>=0&&f.support[q]<z.m,
                    "invalid original four-source support");
            support.insert(f.support[q]);
        }
        require(support.size()==4,"repeated source physical coordinate");
        std::string key;int checksum=0,nz=0;
        for(int j=0;j<z.m;j++){
            int v;in>>v;
            require(bool(in)&&v>=0&&v<=4,"source vector not GF5");
            f.c[j]=static_cast<unsigned char>(v);key.push_back(char('0'+v));
            checksum+=v; nz+=(v!=0);
            require((v!=0)==bool(support.count(j)),
                    "full physical support != original 2+2 source flag");
        }
        require(nz==4 && checksum%5==4 && unique.insert(key).second,
                "illegal or duplicate original GF5 physical column");
    }
    z.palettes.resize(NP);
    std::set<array<int,4>> seen;
    for(int p=0;p<NP;p++){
        int checksum=0;
        for(int j=0;j<4;j++){
            in>>z.palettes[p][j];int v=z.palettes[p][j];
            require(bool(in)&&v>=1&&v<=4,"bad legal palette digit");
            checksum+=v;
        }
        require(checksum%5==4 && seen.insert(z.palettes[p]).second,
                "duplicate/invalid legal checksum4 palette");
    }
    std::set<int> selected;
    for(int a=0;a<k;a++){
        int id;in>>id;
        require(bool(in)&&id>=0&&id<z.n&&selected.insert(id).second,
                "invalid/repeated edited ORIGINAL flag ID");
        z.edited.push_back(id);
    }
    std::string extra;require(!(in>>extra),"unexpected source tokens");
    for(const auto &f:z.flags)
        for(int q=0;q<4;q++)
            require(f.c[f.support[q]]==z.palettes[f.palette][q],
                    "physical original source vector/palette mismatch");
    for(int id=0;id<z.n;id++)if(!selected.count(id))z.frozen.push_back(id);
    require(int(z.frozen.size())==z.n-k,"frozen core not complement of edit set");
    return z;
}
static void init(const Model &z){
    std::map<array<int,4>,int> lookup;
    for(int k=0;k<NP;k++)lookup[z.palettes[k]]=k;
    for(int a=0;a<BASE;a++)for(int b=0;b<BASE;b++){
        int s=0;array<int,4> d{};
        for(int t=0;t<4;t++){
            int av=a/pow5[t]%5, bv=b/pow5[t]%5;
            s+=((av+bv)%5)*pow5[t];
            d[t]=(av-bv+5)%5;
        }
        add4[a*BASE+b]=s;
        const auto it=lookup.find(d);
        diff4[a*BASE+b]=(it==lookup.end()?-1:it->second);
    }
}
struct P {
    array<int,6> out{};
    int in=0;
};
static uint64_t key(const array<int,6>&groups,int count){
    uint64_t out=0;
    for(int g=count-1;g>=0;g--){require(groups[g]<BASE,"overflow key limb");
        out=out*BASE+uint64_t(groups[g]);}
    return out;
}
static std::vector<P> project(const Model &z,int center){
    std::vector<P> result(z.n);
    array<int,MAXM> outside{};outside.fill(-1);
    std::set<int> support(z.flags[center].support.begin(),
                          z.flags[center].support.end());
    int next=0;
    for(int j=0;j<z.m;j++)if(!support.count(j))outside[j]=next++;
    require(next==z.m-4,"wrong outside physical count");
    for(int id:z.frozen) {
        P x;
        for(int j=0;j<z.m;j++){
            int v=z.flags[id].c[j], pos=outside[j];
            if(pos>=0)x.out[pos/4]+=v*pow5[pos%4];
        }
        for(int q=0;q<4;q++)
            x.in+=int(z.flags[id].c[z.flags[center].support[q]])*pow5[q];
        result[id]=x;
    }
    return result;
}
struct Pair {int a,b,inside;};
struct Witness {
    bool has=false;
    int k=0;
    array<int,3> positive{},negative{};
};
struct Result {
    int center=0, frozen=0;
    uint64_t pairs=0,triples=0,projected=0;
    array<Witness,NP> forbidden{};
    array<uint64_t,NP> counts2{},counts3{};
};
static Result evaluate(const Model&z,int center){
    const int groups=(z.m-4)/4;
    const auto pr=project(z,center);
    const auto& F=z.frozen;
    Result out;out.center=center;out.frozen=int(F.size());
    std::unordered_map<uint64_t,std::vector<Pair>> pairs;
    std::unordered_map<uint64_t,std::vector<int>> single;
    pairs.reserve(F.size()*3);single.reserve(F.size()*2);
    for(int x:F)single[key(pr[x].out,groups)].push_back(x);
    for(size_t a=0;a+1<F.size();a++)for(size_t b=a+1<F.size();b++){
        int ia=F[a],ib=F[b];
        array<int,6> limb{};
        for(int g=0;g<groups;g++)
            limb[g]=add4[pr[ia].out[g]*BASE+pr[ib].out[g]];
        uint64_t projected=key(limb,groups);
        int inside=add4[pr[ia].in*BASE+pr[ib].in];
        pairs[projected].push_back(Pair{ia,ib,inside});
        if(const auto it=single.find(projected);it!=single.end())
            for(int x:it->second)if(x!=ia&&x!=ib){
                int palette=diff4[inside*BASE+pr[x].in];
                if(palette>=0){
                    out.counts2[palette]++;
                    auto &w=out.forbidden[palette];
                    if(!w.has){
                        w.has=true;w.k=2;
                        w.positive={center,x,-1};
                        w.negative={ia,ib,-1};
                    }
                }
            }
        out.pairs++;
    }
    for(size_t a=0;a+2<F.size();a++)for(size_t b=a+1;b+1<F.size();b++){
        int ia=F[a],ib=F[b];
        array<int,6> partial{};
        for(int g=0;g<groups;g++)
            partial[g]=add4[pr[ia].out[g]*BASE+pr[ib].out[g]];
        int partinside=add4[pr[ia].in*BASE+pr[ib].in];
        for(size_t c=b+1;c<F.size();c++){
            int ic=F[c];
            array<int,6> limb{};
            for(int g=0;g<groups;g++)
                limb[g]=add4[partial[g]*BASE+pr[ic].out[g]];
            const auto it=pairs.find(key(limb,groups));
            if(it!=pairs.end()){
                int inside=add4[partinside*BASE+pr[ic].in];
                for(const auto &p:it->second) {
                    if(p.a==ia||p.a==ib||p.a==ic||
                       p.b==ia||p.b==ib||p.b==ic)continue;
                    out.projected++;
                    int palette=diff4[inside*BASE+p.inside];
                    if(palette>=0){
                        out.counts3[palette]++;
                        auto &w=out.forbidden[palette];
                        if(!w.has){
                            w.has=true;w.k=3;
                            w.positive={center,p.a,p.b};
                            w.negative={ia,ib,ic};
                        }
                    }
                }
            }
            out.triples++;
        }
    }
    const uint64_t n=uint64_t(F.size());
    require(out.pairs==n*(n-1)/2 && out.triples==n*(n-1)*(n-2)/6,
            "not complete frozen ORIGINAL pair/triple enumeration");
    return out;
}
static void array_json(std::ofstream&o,const array<int,3>&a,int k){
    o<<"[";
    for(int i=0;i<k;i++){if(i)o<<",";o<<a[i];}
    o<<"]";
}
static void save(const Model&z,const std::vector<Result>&rows,
                 const std::string&filename,int shard,int shards){
    std::ofstream o(filename);
    require(bool(o),"cannot write frozen-core exact source report");
    o<<"{\"schema\":\"mathlab.hyp105.original-frozen-core-fibers.v1\""
     <<",\"scheme\":\""<<z.scheme<<"\",\"n\":"<<z.n
     <<",\"m\":"<<z.m<<",\"selected_original_ID_count\":"
     <<z.edited.size()<<",\"frozen_original_ID_count\":"
     <<z.frozen.size()<<",\"shard\":"<<shard<<",\"shards\":"
     <<shards<<",\"edited_original_IDs\":[";
    for(size_t j=0;j<z.edited.size();j++){
        if(j)o<<",";o<<z.edited[j];
    }
    o<<"],\"results\":[";
    for(size_t r=0;r<rows.size();r++){
        const auto &zrow=rows[r];if(r)o<<",";
        int blocked=0;
        for(const auto &w:zrow.forbidden)blocked+=w.has;
        o<<"{\"source_ID\":"<<zrow.center
         <<",\"frozen_pairs_processed\":"<<zrow.pairs
         <<",\"frozen_triples_processed\":"<<zrow.triples
         <<",\"projected_disjoint_matches\":"<<zrow.projected
         <<",\"blocked_count\":"<<blocked<<",\"allowed_palettes\":[";
        bool comma=false;
        for(int p=0;p<NP;p++)if(!zrow.forbidden[p].has){
            if(comma)o<<",";comma=true;o<<p;
        }
        o<<"],\"patterns\":[";
        for(int p=0;p<NP;p++) {
            if(p)o<<",";
            const auto &w=zrow.forbidden[p];
            o<<"{\"palette\":"<<p<<",\"R2_fixed_core_count\":"
             <<zrow.counts2[p]<<",\"R3_fixed_core_count\":"
             <<zrow.counts3[p]<<",\"forbidden\":"
             <<(w.has?"true":"false");
            if(w.has){
                o<<",\"witness_k\":"<<w.k<<",\"positive_original_IDs\":";
                array_json(o,w.positive,w.k);
                o<<",\"negative_original_IDs\":";
                array_json(o,w.negative,w.k);
            }
            o<<"}";
        }
        o<<"]}";
    }
    o<<"]}\n";
    require(bool(o),"lost saved frozen source report");
}
int main(int argc,char**argv){
    try{
        require(argc==5,"usage: SOURCE.txt OUTPUT.json shard shards");
        const Model z=load(argv[1]);
        int shard=std::stoi(argv[3]),shards=std::stoi(argv[4]);
        require(shards>=1&&shards<=64&&shard>=0&&shard<shards,
                "bad frozen-core shard");
        init(z);
        std::vector<Result> rows;
        for(int source:z.edited)if(source%shards==shard){
            rows.push_back(evaluate(z,source));
            int blocked=0;
            for(const auto&w:rows.back().forbidden)blocked+=w.has;
            std::cerr<<"FROZEN_CORE "<<z.scheme<<" ORIGINAL source "<<source
                     <<" blocked="<<blocked<<" allowed="<<NP-blocked
                     <<" processed="<<rows.back().triples
                     <<" complete fixed-core triples\n";
        }
        save(z,rows,argv[2],shard,shards);
        std::cout<<"AA4_FROZEN_FULL_ORIGINAL_GF5_PASS "<<z.scheme<<" shard "
                 <<shard<<"/"<<shards<<" sources="<<rows.size()<<"\n";
        return 0;
    }catch(const std::exception&e){
        std::cerr<<"AA4_FROZEN_FAIL_CLOSED: "<<e.what()<<"\n";
        return 1;
    }
}
