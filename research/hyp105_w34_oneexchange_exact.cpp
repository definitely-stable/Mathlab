// HYP-105 AA4-W34-ALL1: exact exhaustive active-source 51-palette GF5 oracle.
//
// Fixed original W(3,4) real source: 425 distinct incidence flags, physical
// GF5^28, one globally reused 51-valued checksum4 palette per original ID.
// For fixed i, compare each DISJOINT original pair P and triple T disjoint
// from i.  c_i(t)+sum(P)=sum(T), complete GF5, iff their 24D outside
// projections agree and the four inside digits force precisely palette t.
// H_i(t) is EXACT number of real six-distinct-source signed events using i.
// True full R3(t)=R3(current)+H_i(t)-H_i(current).
// 2+2 source R2(t) via a second independent projected singleton/pair scan.
// This optimized C++ is NOT a source of truth on its own: independent Python
// exact 12.7m full-original-triple verifier checks chosen changes, and the
// same C++ 51-vectors are validated on true original W32 vs Python oracles.
//
// Input is reproducible text generated and fully audited by the Python source
// preparer, NOT a synthetic geometry or synthetic palette assignment.

#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>
#include <set>

using std::array;
using std::uint16_t;
using std::uint64_t;
static constexpr int B=625,MAXN=425,MAXM=28,PAL=51;
static int add4[B*B];
static int diff4[B*B];
static int pw5[4]={1,5,25,125};
static void insist(bool ok,const std::string &why) {
    if(!ok) throw std::runtime_error("EXACT original GF5 source audit failed: "+why);
}
static array<int,4> unpack(int x) {
    array<int,4> z{};
    for(int j=0;j<4;++j) z[j]=(x/pw5[j])%5;
    return z;
}
struct Flag {
    array<unsigned char,MAXM> c{};
    array<int,4> support{};
    int palette=-1;
};
struct Input {
    std::string scheme;
    int n=0,m=0,d2=0,d3=0,r3=0;
    std::vector<Flag> flags;
    std::vector<array<int,4>> palettes;
    std::vector<std::pair<int,int>> active;
};
static Input read_source(const std::string& path) {
    std::ifstream in(path);
    insist(bool(in),"cannot read complete actual source context "+path);
    Input t;std::string version;
    int count,pcount;
    in>>version>>t.scheme>>t.n>>t.m>>pcount>>t.d2>>t.d3>>t.r3>>count;
    insist(version=="HYP105_W34_ALL1_V1","wrong scientific data version");
    insist((t.n==425 && t.m==28)||(t.n==45 && t.m==12),
           "only REAL complete symplectic W34/W32 source");
    insist(pcount==PAL && t.d3==t.r3+(t.n-4)*t.d2 && t.d2>=0&&t.r3>=0,
           "inconsistent initial GF5 source baseline");
    insist(count>=1 && count<=t.n,"source active list count outside model");
    t.flags.resize(t.n);
    std::set<std::string> distinct;
    for(int i=0;i<t.n;++i) {
        std::string key;
        int x;
        for(int j=0;j<t.m;++j) {
            in>>x;insist(bool(in)&&x>=0&&x<5,"source vector has illegal GF5 digit");
            t.flags[i].c[j]=static_cast<unsigned char>(x);
            key.push_back(char('0'+x));
        }
        int support_count=0,checksum=0;
        for(int j=0;j<t.m;++j) {
            support_count+=(t.flags[i].c[j]!=0);
            checksum+=t.flags[i].c[j];
        }
        insist(support_count==4 && checksum%5==4,
               "original physical source support or checksum not legal");
        for(int k=0;k<4;++k) {
            in>>x;insist(bool(in)&&x>=0&&x<t.m,"source support outside GF5 space");
            t.flags[i].support[k]=x;
        }
        in>>x;insist(bool(in)&&x>=0&&x<PAL,"illegal source palette index");
        t.flags[i].palette=x;
        std::set<int> support(t.flags[i].support.begin(),t.flags[i].support.end());
        insist(support.size()==4,"not four distinct physical source coordinates");
        for(int j=0;j<t.m;++j)
            insist((t.flags[i].c[j]!=0)==(support.count(j)!=0),
                   "physical source support changed");
        insist(distinct.insert(key).second,"two original source columns identical");
    }
    t.palettes.resize(PAL);
    std::set<int> distinct_palettes;
    for(int k=0;k<PAL;++k) {
        int xsum=0,key=0;
        for(int d=0;d<4;++d) {
            int v;in>>v;insist(bool(in)&&v>=1&&v<=4,"illegal nonzero source coefficient");
            t.palettes[k][d]=v;xsum+=v;key+=v*pw5[d];
        }
        insist(xsum%5==4 && distinct_palettes.insert(key).second,
               "noncanonical duplicate or checksum-invalid 51 source palette");
    }
    std::set<int> seen;
    for(int a=0;a<count;++a) {
        int id,degree;in>>id>>degree;
        insist(bool(in) && id>=0&&id<t.n&&degree>=0&&
               seen.insert(id).second,"duplicate/out-of-range active original source ID");
        t.active.push_back({id,degree});
    }
    std::string junk;
    insist(!(in>>junk),"unexpected extra source input tokens");
    for(const Flag& f:t.flags)
        for(int j=0;j<4;++j)
            insist(f.c[f.support[j]]==t.palettes[f.palette][j],
                   "original globally assigned source coefficient incompatible with palette");
    return t;
}
static void init_luts(const Input& t) {
    std::fill(std::begin(diff4),std::end(diff4),-1);
    std::unordered_map<int,int> palette_ids;
    for(int k=0;k<PAL;++k) {
        int key=0;
        for(int q=0;q<4;++q) key+=t.palettes[k][q]*pw5[q];
        insist(palette_ids.emplace(key,k).second,
               "duplicate source physical GF5 palette coefficient vector");
    }
    array<array<int,4>,B> digs;
    for(int a=0;a<B;++a)digs[a]=unpack(a);
    for(int a=0;a<B;++a)for(int b=0;b<B;++b) {
        int s=0,d=0;
        for(int q=0;q<4;++q) {
            s+=((digs[a][q]+digs[b][q])%5)*pw5[q];
            d+=((digs[a][q]-digs[b][q]+5)%5)*pw5[q];
        }
        add4[a*B+b]=s;
        auto it=palette_ids.find(d);
        if(it!=palette_ids.end())diff4[a*B+b]=it->second;
    }
}
struct Projected {
    array<uint16_t,6> outside{};
    uint16_t inside=0;
    uint64_t key=0;
};
struct Pair {uint16_t inside=0;uint16_t a=0,b=0;};
struct Singleton {uint16_t inside=0;uint16_t id=0;};
static uint64_t encode(const array<uint16_t,6>& limb,int groups) {
    uint64_t key=0;
    for(int g=groups-1;g>=0;--g) {
        insist(limb[g]<B,"invalid exact outside GF5 limb");
        key=key*B+limb[g];
    }
    return key;
}
static std::vector<Projected> project(const Input& t,int center) {
    std::vector<Projected> projected(t.n);
    std::set<int> support(
        t.flags[center].support.begin(),t.flags[center].support.end());
    array<int,MAXM> outside_pos{};
    outside_pos.fill(-1);
    int p=0;
    for(int j=0;j<t.m;++j)if(!support.count(j))outside_pos[j]=p++;
    insist(p==t.m-4 && (p==24||p==8),"wrong complete physical outside projection");
    int groups=p/4;
    for(int source=0;source<t.n;++source) {
        Projected z;
        for(int j=0;j<t.m;++j) {
            int v=t.flags[source].c[j];
            if(outside_pos[j]>=0) {
                int at=outside_pos[j];
                z.outside[at/4]+=uint16_t(v*pw5[at%4]);
            }
        }
        for(int k=0;k<4;++k)
            z.inside+=uint16_t(t.flags[source].c[
                t.flags[center].support[k]]*pw5[k]);
        z.key=encode(z.outside,groups);
        projected[source]=z;
    }
    return projected;
}
struct Row {
    int id=-1,degree=0,current_palette=0,h_current=0,d2_current=0;
    array<int,PAL> h{},two{};
    int best_palette=-1,best_d2=0,best_d3=0,best_r3=0;
    uint64_t projected_matches=0,source_overlaps_removed=0;
};
static Row exact_original_source(const Input& t,int source,int degree) {
    const int groups=(t.m-4)/4;
    auto projs=project(t,source);
    std::unordered_map<uint64_t,std::vector<Pair>> pairs;
    pairs.reserve(t.n*3);
    std::unordered_map<uint64_t,std::vector<Singleton>> singles;
    singles.reserve(t.n*2);
    std::vector<int> other;
    for(int id=0;id<t.n;++id)if(id!=source) {
        other.push_back(id);
        singles[projs[id].key].push_back(Singleton{projs[id].inside,
                                                  uint16_t(id)});
    }
    Row result;
    result.id=source;result.degree=degree;
    result.current_palette=t.flags[source].palette;
    uint64_t npairs=0;
    for(size_t a=0;a+1<other.size();++a) {
        int ia=other[a];
        for(size_t b=a+1;b<other.size();++b) {
            int ib=other[b];
            array<uint16_t,6> limb{};
            for(int g=0;g<groups;++g)
                limb[g]=uint16_t(add4[
                    int(projs[ia].outside[g])*B+projs[ib].outside[g]]);
            uint64_t key=encode(limb,groups);
            int inside=add4[int(projs[ia].inside)*B+projs[ib].inside];
            pairs[key].push_back(Pair{uint16_t(inside),
                                      uint16_t(ia),uint16_t(ib)});
            auto found=singles.find(key);
            if(found!=singles.end()) for(const Singleton& single:found->second){
                if(single.id==ia||single.id==ib)continue;
                int pal=diff4[inside*B+single.inside];
                if(pal>=0)result.two[pal]++;
            }
            ++npairs;
        }
    }
    insist(npairs==uint64_t(other.size())*(other.size()-1)/2,
           "not all other ORIGINAL 2-source subsets indexed");
    uint64_t ntriples=0;
    for(size_t a=0;a+2<other.size();++a) {
        int ia=other[a];
        for(size_t b=a+1;b+1<other.size();++b) {
            int ib=other[b];
            array<uint16_t,6> partial{};
            for(int g=0;g<groups;++g)
                partial[g]=uint16_t(add4[int(projs[ia].outside[g])*B+
                                            projs[ib].outside[g]]);
            int pair_inside=add4[
                int(projs[ia].inside)*B+projs[ib].inside];
            for(size_t c=b+1;c<other.size();++c) {
                int ic=other[c];
                array<uint16_t,6> limb{};
                for(int g=0;g<groups;++g)
                    limb[g]=uint16_t(add4[int(partial[g])*B+
                                              projs[ic].outside[g]]);
                uint64_t key=encode(limb,groups);
                auto found=pairs.find(key);
                if(found!=pairs.end()) {
                    int inside=add4[pair_inside*B+projs[ic].inside];
                    for(const Pair& pair:found->second) {
                        ++result.projected_matches;
                        if(pair.a==ia||pair.a==ib||pair.a==ic||
                           pair.b==ia||pair.b==ib||pair.b==ic) {
                            ++result.source_overlaps_removed;
                            continue;
                        }
                        int pal=diff4[inside*B+pair.inside];
                        if(pal>=0)result.h[pal]++;
                    }
                }
                ++ntriples;
            }
        }
    }
    int n=int(other.size());
    insist(ntriples==uint64_t(n)*(n-1)*(n-2)/6,
           "not all REAL 3-source subsets processed");
    result.h_current=result.h[result.current_palette];
    result.d2_current=result.two[result.current_palette];
    insist(result.h_current==degree,
           "INDEPENDENT complete true-R3 source witness degree mismatch");
    insist(result.d2_current<=t.d2,
           "source R2 incident collisions exceed actual global R2");
    // The current-palette candidate is always legal under R2 nonincrease.
    auto score=[&](int k) {
        int d2=t.d2+result.two[k]-result.d2_current;
        int r3=t.r3+result.h[k]-degree;
        int d3=r3+(t.n-4)*d2;
        insist(d2>=0&&r3>=0&&d3>=0,
               "negative predicted true ORIGINAL signed GF5 source risk");
        return std::make_tuple(r3,d2,d3,k);
    };
    auto best=score(result.current_palette);
    for(int k=0;k<PAL;++k) {
        auto trial=score(k);
        if(std::get<1>(trial)>t.d2)continue; // hard R2 guard
        if(trial<best)best=trial;
    }
    result.best_r3=std::get<0>(best);
    result.best_d2=std::get<1>(best);
    result.best_d3=std::get<2>(best);
    result.best_palette=std::get<3>(best);
    insist(result.best_r3<=t.r3 && result.best_d2<=t.d2,
           "source R2 guard or signed R3 monotonicity violated");
    return result;
}
static void print_array(std::ofstream& out,const array<int,PAL>& a) {
    out<<"[";
    for(int k=0;k<PAL;++k) {
        if(k)out<<",";
        out<<a[k];
    }
    out<<"]";
}
static void save_rows(const Input& t,int shard,int shards,
                      const std::vector<Row>& rows,const std::string& path) {
    std::ofstream out(path);
    insist(bool(out),"cannot write exact scientific source audit shard");
    out<<"{\n\"schema\":\"mathlab.hyp105.original-w34-active-oneexchange-v1\",\n";
    out<<"\"scheme\":\""<<t.scheme<<"\",\"shard\":"<<shard
       <<",\"shards\":"<<shards<<",\"n\":"<<t.n<<",\"m\":"<<t.m
       <<",\"original_D2\":"<<t.d2<<",\"original_D3\":"<<t.d3
       <<",\"original_R3\":"<<t.r3
       <<",\"total_active_original_IDs\":"<<t.active.size()
       <<",\"results\":[\n";
    for(size_t x=0;x<rows.size();++x){
        const Row& z=rows[x];
        if(x)out<<",\n";
        out<<"{\"source_ID\":"<<z.id<<",\"witness_degree\":"<<z.degree
           <<",\"current_palette\":"<<z.current_palette
           <<",\"current_true_R3_incidence\":"<<z.h_current
           <<",\"current_R2_cross_incidence\":"<<z.d2_current
           <<",\"best_palette\":"<<z.best_palette
           <<",\"best_full_D2\":"<<z.best_d2
           <<",\"best_full_D3\":"<<z.best_d3
           <<",\"best_full_R3\":"<<z.best_r3
           <<",\"projected_matches\":"<<z.projected_matches
           <<",\"overlapping_source_pairs_removed\":"
           <<z.source_overlaps_removed<<",\"H_R3_all_51\":";
        print_array(out,z.h);
        out<<",\"H_R2_all_51\":";
        print_array(out,z.two);
        out<<"}";
    }
    out<<"]}\n";
    insist(bool(out),"lost exact scientific W34 source audit output");
}
int main(int argc,char** argv) {
    try {
        insist(argc==5,"usage: original_source.txt shard shard_count result.json");
        Input t=read_source(argv[1]);
        int shard=std::stoi(argv[2]),shards=std::stoi(argv[3]);
        insist(shards>=1 && shards<=64 && shard>=0 && shard<shards,
               "invalid exhaustive source shard parameters");
        init_luts(t);
        std::vector<Row> rows;
        for(const auto& a:t.active) if(a.first%shards==shard) {
            Row z=exact_original_source(t,a.first,a.second);
            rows.push_back(std::move(z));
            std::cerr<<"EXACT original "<<t.scheme<<" active original ID "
                     <<a.first<<" / "<<t.active.size()
                     <<" current signed R3 "<<t.r3
                     <<" best signed R3 "<<rows.back().best_r3
                     <<" full four-coordinate GF5 source 51 verified\n";
        }
        save_rows(t,shard,shards,rows,argv[4]);
        std::cout<<"EXACT original 51-palette active-source shard PASS: scheme "
                 <<t.scheme<<" shard "<<shard<<"/"<<shards
                 <<" checked "<<rows.size()<<" real source IDs\n";
        return 0;
    }catch(const std::exception& e) {
        std::cerr<<"FAIL CLOSED: "<<e.what()<<"\n";
        return 1;
    }
}
