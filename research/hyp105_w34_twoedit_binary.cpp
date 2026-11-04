// HYP-105 AA4-BINARY: ALL original GF5 signed 2v2 / 3v3 events
// with EXACTLY TWO editable ORIGINAL source IDs and all remaining IDs
// in fixed F. This does not prove full 25/26-variable GF5 feasibility.
// Source vectors are complete physical 28D (W34) or real 12D (W32).
// Key is lossless base-625 encoding, compared by FULL 128-bit equality.
// The frozen triple-sum index is complete, never probabilistically pruned.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <set>

using std::array;
using Key=unsigned __int128;
using std::uint64_t;
static constexpr int BASE=625,PAL=51,MAXG=7,MAXM=28;
static int add5[BASE*BASE],sub5[BASE*BASE];
static const int pw[4]={1,5,25,125};
static void insist(bool ok,const std::string &msg) {
    if(!ok)throw std::runtime_error("HYP105_BINARY_FAIL_CLOSED: "+msg);
}
struct Hash{
    size_t operator()(Key k) const noexcept {
        uint64_t x=uint64_t(k)^uint64_t(k>>64)*0x9e3779b97f4a7c15ULL;
        x^=x>>30;x*=0xbf58476d1ce4e5b9ULL;
        x^=x>>27;x*=0x94d049bb133111ebULL;
        return size_t(x^(x>>31));
    }
};
using Limb=array<uint16_t,MAXG>;
struct Source {
    Limb grouped{};
    array<int,4> support{};
    int palette=0;
};
struct Input {
    std::string scheme;
    int n=0,m=0,ng=0;
    std::vector<Source> source;
    std::vector<array<int,4>> palette;
    std::vector<int> editable,frozen;
    std::vector<uint64_t> domains;
    std::vector<array<Limb,PAL>> candidates;
};
static int digit(int group,int q){return group/pw[q]%5;}
static void init(const Input& t){
    for(int a=0;a<BASE;a++)for(int b=0;b<BASE;b++){
        int c=0,d=0;
        for(int q=0;q<4;q++){
            c+=((digit(a,q)+digit(b,q))%5)*pw[q];
            d+=((digit(a,q)-digit(b,q)+5)%5)*pw[q];
        }
        add5[a*BASE+b]=c;
        sub5[a*BASE+b]=d;
    }
}
static Limb sum(const Limb&a,const Limb&b,int ng){
    Limb x{};
    for(int g=0;g<ng;g++)x[g]=add5[int(a[g])*BASE+b[g]];
    return x;
}
static Limb subtract(const Limb&a,const Limb&b,int ng){
    Limb x{};
    for(int g=0;g<ng;g++)x[g]=sub5[int(a[g])*BASE+b[g]];
    return x;
}
static Key encoded(const Limb &a,int ng){
    Key value=0;
    for(int g=ng-1;g>=0;g--){
        insist(a[g]<BASE,"bad GF5 limb during signature encoding");
        value=value*BASE+a[g];
    }
    return value;
}
static Input read(const std::string &filename){
    std::ifstream in(filename);
    insist(bool(in),"missing complete ORIGINAL source model");
    Input t;std::string version;
    int editableN,frozenN;
    in>>version>>t.scheme>>t.n>>t.m>>editableN>>frozenN;
    insist(version=="HYP105_BINARY_ORIGINAL_V1","bad source input version");
    insist((t.n==425&&t.m==28)||(t.n==45&&t.m==12),
           "only genuine complete W34/W32 physical source arrays");
    insist(editableN>=2&&editableN<=t.n && frozenN>=5 &&
           editableN+frozenN<=t.n,"invalid original F/T source cardinalities");
    if(t.n==425)insist(editableN+frozenN==425,
                       "full W34 binary experiment must partition all sources");
    t.ng=t.m/4;
    t.source.resize(t.n);
    std::set<std::string> distinct;
    for(int id=0;id<t.n;id++){
        auto &v=t.source[id];
        in>>v.palette;
        insist(bool(in)&&v.palette>=0&&v.palette<PAL,
               "invalid original source palette");
        std::set<int> support;
        for(int j=0;j<4;j++){
            in>>v.support[j];
            insist(bool(in)&&v.support[j]>=0&&v.support[j]<t.m,
                   "original support outside complete physical GF5 space");
            support.insert(v.support[j]);
        }
        insist(support.size()==4,"not exactly four distinct source coordinates");
        int sumdigits=0,nz=0;
        std::string fingerprint;
        for(int j=0;j<t.m;j++){
            int x;in>>x;
            insist(bool(in)&&x>=0&&x<5,"invalid original GF5 digit");
            v.grouped[j/4]+=uint16_t(x*pw[j%4]);
            sumdigits+=x;nz+=(x!=0);
            insist(bool(support.count(j))==(x!=0),
                   "original actual 2+2 support drift");
            fingerprint.push_back(char('0'+x));
        }
        insist(nz==4&&sumdigits%5==4&&distinct.insert(fingerprint).second,
               "source checksum / singleton ORIGINAL uniqueness failed");
    }
    t.palette.resize(PAL);
    std::set<array<int,4>> uniq;
    for(int p=0;p<PAL;p++){
        int checksum=0;
        for(int q=0;q<4;q++){
            in>>t.palette[p][q];
            insist(bool(in)&&1<=t.palette[p][q]&&t.palette[p][q]<=4,
                   "not 51 nonzero source coefficients");
            checksum+=t.palette[p][q];
        }
        insist(checksum%5==4&&uniq.insert(t.palette[p]).second,
               "invalid checksum4 51 source palette table");
    }
    for(int id=0;id<t.n;id++)for(int q=0;q<4;q++){
        int actual=digit(t.source[id].grouped[t.source[id].support[q]/4],
                         t.source[id].support[q]%4);
        insist(actual==t.palette[t.source[id].palette][q],
               "true original 2+2 physical source vs legal palette mismatch");
    }
    std::set<int> used;
    t.editable.resize(editableN);
    t.frozen.resize(frozenN);
    for(int&v:t.editable){
        in>>v;insist(bool(in)&&0<=v&&v<t.n&&used.insert(v).second,
                     "duplicate/out-of-range editable original ID");
    }
    for(int&v:t.frozen){
        in>>v;insist(bool(in)&&0<=v&&v<t.n&&used.insert(v).second,
                     "duplicate/out-of-range frozen original ID");
    }
    insist(std::is_sorted(t.editable.begin(),t.editable.end()) &&
           std::is_sorted(t.frozen.begin(),t.frozen.end()),
           "canonical ordered original-ID subsets required");
    t.domains.resize(t.editable.size());
    for(auto &v:t.domains){
        in>>v;
        insist(bool(in)&&v>0&&v<(uint64_t(1)<<PAL),
               "nonempty valid exact source palette domain required");
    }
    std::string extra;
    insist(!(in>>extra),"unexpected trailing original source input tokens");
    t.candidates.resize(t.editable.size());
    for(size_t j=0;j<t.editable.size();j++){
        int center=t.editable[j];
        const auto &original=t.source[center];
        for(int p=0;p<PAL;p++){
            Limb x=original.grouped;
            for(int q=0;q<4;q++){
                int coord=original.support[q];
                int oldgroup=x[coord/4];
                oldgroup-=digit(oldgroup,coord%4)*pw[coord%4];
                oldgroup+=t.palette[p][q]*pw[coord%4];
                insist(oldgroup>=0&&oldgroup<BASE,
                       "source replacement physical limb overflow");
                x[coord/4]=uint16_t(oldgroup);
            }
            t.candidates[j][p]=x;
        }
    }
    return t;
}
struct Pair {
    int a=0,b=0;Limb s{};
};
struct FrozenIndex{
    std::vector<Pair> pairs;
    std::unordered_map<Key,uint32_t,Hash> pairAt;
    std::unordered_map<Key,uint32_t,Hash> tripleAt;
    std::unordered_map<Key,uint16_t,Hash> singleAt;
    uint64_t triples=0;
};
static uint32_t tripcode(int a,int b,int c){
    insist(a>=0&&b>=0&&c>=0&&a<512&&b<512&&c<512,
           "invalid ORIGINAL triple source ID pack");
    return (uint32_t(a)<<18)|(uint32_t(b)<<9)|uint32_t(c);
}
static array<int,3> unpack(uint32_t v){
    return {int((v>>18)&511),int((v>>9)&511),int(v&511)};
}
static FrozenIndex frozenIndex(const Input &t){
    FrozenIndex z;
    z.pairs.reserve(t.frozen.size()*(t.frozen.size()-1)/2);
    z.pairAt.reserve(z.pairs.capacity()*2);
    z.singleAt.reserve(t.frozen.size()*2);
    for(int id:t.frozen)
        insist(z.singleAt.emplace(encoded(t.source[id].grouped,t.ng),
                                  uint16_t(id)).second,
               "duplicate frozen ORIGINAL singleton");
    const auto &F=t.frozen;
    for(size_t a=0;a+1<F.size();a++)for(size_t b=a+1;b<F.size();b++){
        const int ia=F[a],ib=F[b];
        Pair p{ia,ib,sum(t.source[ia].grouped,t.source[ib].grouped,t.ng)};
        Key k=encoded(p.s,t.ng);
        insist(z.pairAt.emplace(k,uint32_t(z.pairs.size())).second,
               "frozen ORIGINAL R2 collision, min source cover invalid");
        z.pairs.push_back(p);
    }
    const auto nt=uint64_t(F.size())*(F.size()-1)*(F.size()-2)/6;
    z.tripleAt.reserve(size_t(nt*1.16)+1);
    for(size_t a=0;a+2<F.size();a++)for(size_t b=a+1;b+1<F.size();b++){
        auto first=sum(t.source[F[a]].grouped,t.source[F[b]].grouped,t.ng);
        for(size_t c=b+1;c<F.size();c++){
            auto all=sum(first,t.source[F[c]].grouped,t.ng);
            Key k=encoded(all,t.ng);
            insist(z.tripleAt.emplace(k,tripcode(F[a],F[b],F[c])).second,
                   "frozen ORIGINAL triple collision, min source cover invalid");
            z.triples++;
        }
    }
    insist(z.pairs.size()==F.size()*(F.size()-1)/2&&z.triples==nt,
           "incomplete actual original frozen pair/triple sums");
    return z;
}
struct Witness{
    int k=0;
    array<int,3> pos{-1,-1,-1};
    array<int,3> neg{-1,-1,-1};
};
struct Choice {
    int p=0,q=0;
    Witness why{};
};
struct PairResult{
    int id1=0,id2=0;
    int domain1=0,domain2=0;
    uint64_t possible=0,allowed=0;
    std::vector<Choice> rejected;
    std::vector<array<int,2>> permitted;
    uint64_t opposite_pair_matches=0;
};
static int countDomain(uint64_t bits){return __builtin_popcountll(bits);}
static bool sourceDisjoint(const Pair &a,const Pair &b){
    return a.a!=b.a&&a.a!=b.b&&a.b!=b.a&&a.b!=b.b;
}
static Key outsideMasked(const Pair &p,const array<array<int,BASE>,MAXG>&lut,
                         int ng){
    Key out=0;
    for(int g=ng-1;g>=0;g--)out=out*BASE+lut[g][p.s[g]];
    return out;
}
static PairResult examine(const Input &t,const FrozenIndex &f,int x,int y){
    const int i=t.editable[x],j=t.editable[y];
    PairResult report;
    report.id1=i;report.id2=j;
    report.domain1=countDomain(t.domains[x]);
    report.domain2=countDomain(t.domains[y]);
    auto &F=t.frozen;
    struct Row {
        int p=0,q=0;
        Limb plus{},delta{};
        Witness witness{};
    };
    std::vector<Row> variants;
    variants.reserve(report.domain1*report.domain2);
    std::unordered_map<Key,std::vector<int>,Hash> required_delta;
    for(int p=0;p<PAL;p++)if((t.domains[x]>>p)&1)
        for(int q=0;q<PAL;q++)if((t.domains[y]>>q)&1){
            Row z;
            z.p=p;z.q=q;
            z.plus=sum(t.candidates[x][p],t.candidates[y][q],t.ng);
            z.delta=subtract(t.candidates[x][p],t.candidates[y][q],t.ng);
            variants.push_back(z);
        }
    report.possible=variants.size();
    auto assign=[&](Row &r,int k,array<int,3> pos,array<int,3> neg){
        if(r.witness.k)return;
        r.witness.k=k;r.witness.pos=pos;r.witness.neg=neg;
    };
    // Complete 2v2 with both edited on one side: i+j = F_a+F_b.
    // Complete 2v2 opposing: i+F_a = j+F_b.
    // Complete 3v3 same-side: i+j+F_a = F_b+F_c+F_d.
    for(auto &r:variants){
        const Key same=encoded(r.plus,t.ng);
        if(const auto it=f.pairAt.find(same);it!=f.pairAt.end()){
            const auto &v=f.pairs[it->second];
            assign(r,2,{i,j,-1},{v.a,v.b,-1});
        }
        for(int a:F){
            auto target=sum(r.delta,t.source[a].grouped,t.ng);
            // i+F_a=j+F_b iff F_b=F_a + i-j.
            if(const auto it=f.singleAt.find(encoded(target,t.ng));
               it!=f.singleAt.end()&&int(it->second)!=a){
                assign(r,2,{i,a,-1},{j,int(it->second),-1});
                break;
            }
        }
        if(!r.witness.k){
            for(int a:F){
                Key sig=encoded(sum(r.plus,t.source[a].grouped,t.ng),t.ng);
                const auto it=f.tripleAt.find(sig);
                if(it==f.tripleAt.end())continue;
                auto v=unpack(it->second);
                if(a==v[0]||a==v[1]||a==v[2])continue;
                assign(r,3,{i,j,a},{v[0],v[1],v[2]});
                break;
            }
        }
    }
    // Complete 3v3 opposing editable i and j:
    //    i + F_ab = j + F_cd     (four DISTINCT frozen IDs).
    // Therefore F_cd - F_ab = i-j. The outside projection of
    // F_ab and F_cd off support(i) UNION support(j) MUST agree.
    // Grouping by this EXACT outside signature loses NO candidates.
    std::set<int> support;
    support.insert(t.source[i].support.begin(),t.source[i].support.end());
    support.insert(t.source[j].support.begin(),t.source[j].support.end());
    array<array<int,BASE>,MAXG> outside{};
    for(int g=0;g<t.ng;g++)for(int v=0;v<BASE;v++){
        int result=0;
        for(int q=0;q<4;q++)if(!support.count(g*4+q))
            result+=digit(v,q)*pw[q];
        outside[g][v]=result;
    }
    required_delta.reserve(variants.size()*2);
    for(size_t k=0;k<variants.size();k++)if(!variants[k].witness.k){
        required_delta[encoded(variants[k].delta,t.ng)].push_back(int(k));
    }
    if(!required_delta.empty()){
        std::unordered_map<Key,std::vector<int>,Hash> matched;
        matched.reserve(f.pairs.size()*2);
        for(size_t p=0;p<f.pairs.size();p++)
            matched[outsideMasked(f.pairs[p],outside,t.ng)]
                .push_back(int(p));
        for(const auto &group:matched){
            const auto &entries=group.second;
            if(entries.size()<2)continue;
            for(int a:entries)for(int b:entries){
                if(a==b||!sourceDisjoint(f.pairs[a],f.pairs[b]))continue;
                report.opposite_pair_matches++;
                auto target=subtract(f.pairs[b].s,f.pairs[a].s,t.ng);
                const auto hit=required_delta.find(encoded(target,t.ng));
                if(hit==required_delta.end())continue;
                for(int idx:hit->second){
                    auto &r=variants[idx];
                    assign(r,3,{i,f.pairs[a].a,f.pairs[a].b},
                               {j,f.pairs[b].a,f.pairs[b].b});
                }
            }
        }
    }
    for(const auto&r:variants){
        if(r.witness.k)report.rejected.push_back(Choice{r.p,r.q,r.witness});
        else report.permitted.push_back({r.p,r.q});
    }
    report.allowed=report.permitted.size();
    insist(report.allowed+report.rejected.size()==report.possible,
           "binary source pair candidate loss");
    return report;
}
static void idsJson(std::ofstream &out,const array<int,3>&x,int k){
    out<<"[";
    for(int a=0;a<k;a++){if(a)out<<",";out<<x[a];}
    out<<"]";
}
static void save(const Input &t,const FrozenIndex &f,
                 const std::vector<PairResult>&rows,
                 int shard,int nshards,const std::string &outfile){
    std::ofstream out(outfile);
    insist(bool(out),"could not create complete original source binary report");
    out<<"{\"schema\":\"mathlab.hyp105.original-W34-binary-sector.v1\""
       <<",\"scheme\":\""<<t.scheme<<"\",\"n\":"<<t.n
       <<",\"m\":"<<t.m<<",\"edited_original_source_IDs\":[";
    for(size_t a=0;a<t.editable.size();a++){
        if(a)out<<",";out<<t.editable[a];
    }
    out<<"],\"frozen_original_source_IDs\":[";
    for(size_t a=0;a<t.frozen.size();a++){
        if(a)out<<",";out<<t.frozen[a];
    }
    out<<"],\"all_frozen_pairs\":"<<f.pairs.size()
       <<",\"all_frozen_triples\":"<<f.triples
       <<",\"shard\":"<<shard<<",\"shards\":"<<nshards
       <<",\"results\":[";
    for(size_t n=0;n<rows.size();n++){
        if(n)out<<",";
        const auto&r=rows[n];
        out<<"{\"source_i\":"<<r.id1<<",\"source_j\":"<<r.id2
           <<",\"domain_i\":"<<r.domain1
           <<",\"domain_j\":"<<r.domain2
           <<",\"total_domain_pairs\":"<<r.possible
           <<",\"allowed_pairs_count\":"<<r.allowed
           <<",\"opposite_fixed_pair_ordered_matches\":"
           <<r.opposite_pair_matches
           <<",\"allowed_pairs\":[";
        for(size_t a=0;a<r.permitted.size();a++){
            if(a)out<<",";
            out<<"["<<r.permitted[a][0]<<","<<r.permitted[a][1]<<"]";
        }
        out<<"],\"forbidden\":[";
        for(size_t a=0;a<r.rejected.size();a++){
            if(a)out<<",";
            const auto &z=r.rejected[a];
            out<<"{\"p\":"<<z.p<<",\"q\":"<<z.q<<",\"k\":"<<z.why.k
               <<",\"positive_original_IDs\":";
            idsJson(out,z.why.pos,z.why.k);
            out<<",\"negative_original_IDs\":";
            idsJson(out,z.why.neg,z.why.k);
            out<<"}";
        }
        out<<"]}";
    }
    out<<"]}\n";
    insist(bool(out),"truncated exact original source binary output");
}
int main(int argc,char **argv){
    try{
        insist(argc==5,"usage: SOURCE.txt OUTPUT.json shard shards");
        const Input t=read(argv[1]);
        const int shard=std::stoi(argv[3]),nshards=std::stoi(argv[4]);
        insist(shard>=0&&nshards>0&&nshards<=32&&shard<nshards,
               "bad exact binary original-ID shard count");
        init(t);
        FrozenIndex fixed=frozenIndex(t);
        std::vector<PairResult> rows;
        size_t total=0;
        for(int x=0;x<int(t.editable.size());x++)
            for(int y=x+1;y<int(t.editable.size());y++){
                int a=t.editable[x],b=t.editable[y];
                if((total++)%size_t(nshards)!=size_t(shard))continue;
                rows.push_back(examine(t,fixed,x,y));
                std::cerr<<"EXACT ORIGINAL TWO-EDIT "<<t.scheme<<" "<<a<<","
                         <<b<<" pair candidates "<<rows.back().possible
                         <<" allowed "<<rows.back().allowed
                         <<" physical F triples indexed "<<fixed.triples<<"\n";
            }
        save(t,fixed,rows,shard,nshards,argv[2]);
        std::cout<<"AA4_BINARY_PHYSICAL_FULL_2EDIT_PASS "<<t.scheme
                 <<" shard "<<shard<<"/"<<nshards
                 <<" exact true original source pairs "<<rows.size()<<"\n";
        return 0;
    }catch(const std::exception&e){
        std::cerr<<"AA4_BINARY_FAIL_CLOSED: "<<e.what()<<"\n";
        return 1;
    }
}
