// HYP-105 AA4-MULTI: exact ORIGINAL 2+2 and 3+3 GF(5) counterexample
// oracle for complete W34 (425 sources, GF5^28) and genuine W32 subcases.
// Frozen-only exact pair/triple maps are cached ONCE and reused across
// multiple candidate coefficient assignments. Every reported signed event
// is physical/full-coordinate/source-distinct. No probabilistic fingerprints.
// BOUNDED CEGAR search NEVER licenses an UNSAT or all-h theorem conclusion.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

using Key=unsigned __int128;
using std::uint64_t;
using std::uint32_t;
using Limb=std::array<uint16_t,7>;
static constexpr int RAD=625,PAL=51,MAXN=425;
static int add[RAD*RAD],powers[4]={1,5,25,125};
static void require(bool v,const std::string&msg) {
    if(!v)throw std::runtime_error("ORIGINAL_CEGAR_FAIL_CLOSED: "+msg);
}
struct Hash {
    size_t operator()(Key k) const noexcept {
        uint64_t a=uint64_t(k) ^ (uint64_t(k>>64)*0x9e3779b97f4a7c15ULL);
        a^=a>>30;a*=0xbf58476d1ce4e5b9ULL;a^=a>>27;
        a*=0x94d049bb133111ebULL;
        return size_t(a^(a>>31));
    }
};
static int digit(int limb,int q) {return (limb/powers[q])%5;}
static void init_lut() {
    for(int a=0;a<RAD;a++)for(int b=0;b<RAD;b++){
        int s=0;
        for(int q=0;q<4;q++)
            s+=((digit(a,q)+digit(b,q))%5)*powers[q];
        add[a*RAD+b]=s;
    }
}
static Limb plus(const Limb&a,const Limb&b,int ng){
    Limb out{};
    for(int i=0;i<ng;i++)out[i]=add[int(a[i])*RAD+b[i]];
    return out;
}
static Key sig(const Limb &v,int ng){
    Key k=0;
    for(int g=ng-1;g>=0;--g){
        require(v[g]<RAD,"illegal complete GF5 limb");
        k=k*RAD+v[g];
    }
    return k;
}
static uint32_t pack2(int a,int b){return (uint32_t(a)<<9)|uint32_t(b);}
static uint32_t pack3(int a,int b,int c){
    return (uint32_t(a)<<18)|(uint32_t(b)<<9)|uint32_t(c);
}
static std::array<int,2> unpack2(uint32_t p){
    return {int((p>>9)&511),int(p&511)};
}
static std::array<int,3> unpack3(uint32_t p){
    return {int((p>>18)&511),int((p>>9)&511),int(p&511)};
}
struct Column{
    Limb base{};
    std::array<int,4> support{};
    int originalPalette=-1;
};
struct Input {
    std::string scheme;
    int n=0,m=0,ng=0;
    std::vector<Column> columns;
    std::array<std::array<int,4>,PAL> palettes{};
    std::vector<int> T,F;
    std::vector<uint64_t> domains;
    std::vector<std::array<Limb,PAL>> candidates;
};
static Input read_original_source(const std::string&path){
    std::ifstream in(path);
    require(bool(in),"missing source input");
    Input t;
    std::string version;
    int tcount,fcount;
    in>>version>>t.scheme>>t.n>>t.m>>tcount>>fcount;
    require(version=="HYP105_BINARY_ORIGINAL_V1","wrong complete ORIGINAL source schema");
    require((t.n==425&&t.m==28)||(t.n==45&&t.m==12),
            "only genuine W34/W32 original physical dimensions");
    require(tcount>=2&&fcount>=6&&tcount+fcount<=t.n,
            "unsupported real-source finite active subset");
    if(t.n==425)require(tcount+fcount==425,
                        "W34 must partition ALL original sources");
    t.ng=t.m/4;
    t.columns.resize(t.n);
    std::set<std::string> singletons;
    for(int id=0;id<t.n;id++){
        auto &c=t.columns[id];
        in>>c.originalPalette;
        require(bool(in)&&0<=c.originalPalette&&c.originalPalette<PAL,
                "invalid original global source palette");
        std::set<int> support;
        for(int q=0;q<4;q++){
            in>>c.support[q];
            require(bool(in)&&0<=c.support[q]&&c.support[q]<t.m,
                    "original support outside physical dimension");
            support.insert(c.support[q]);
        }
        require(support.size()==4,"original coefficient support not four distinct positions");
        int nz=0,checksum=0;std::string identity;
        for(int j=0;j<t.m;j++){
            int x;in>>x;
            require(bool(in)&&0<=x&&x<5,"invalid original physical GF5 coefficient");
            require(bool(support.count(j))==(x!=0),"original 2+2 support violation");
            c.base[j/4]+=uint16_t(x*powers[j%4]);
            checksum+=x;nz+=(x!=0);identity+=char('0'+x);
        }
        require(nz==4 && checksum%5==4 && singletons.insert(identity).second,
                "not unique checksum4 original full physical columns");
    }
    std::set<std::array<int,4>> uniqueP;
    for(int p=0;p<PAL;p++){
        int checksum=0;
        for(int q=0;q<4;q++){
            in>>t.palettes[p][q];
            int value=t.palettes[p][q];
            require(bool(in)&&1<=value&&value<=4,"not a legal original GF5 palette");
            checksum+=value;
        }
        require(checksum%5==4 && uniqueP.insert(t.palettes[p]).second,
                "wrong checksum4 51 legal source palette");
    }
    for(int id=0;id<t.n;id++){
        const auto &c=t.columns[id];
        for(int q=0;q<4;q++){
            int coordinate=c.support[q],g=coordinate/4;
            require(digit(c.base[g],coordinate%4)==t.palettes[c.originalPalette][q],
                    "physical source vector does not match global source palette");
        }
    }
    t.T.resize(tcount);t.F.resize(fcount);
    std::set<int> used;
    for(int&i:t.T){
        in>>i;require(bool(in)&&0<=i&&i<t.n&&used.insert(i).second,
                      "invalid edited ORIGINAL source ID");
    }
    for(int&i:t.F){
        in>>i;require(bool(in)&&0<=i&&i<t.n&&used.insert(i).second,
                      "invalid frozen ORIGINAL source ID");
    }
    require(std::is_sorted(t.T.begin(),t.T.end())&&
            std::is_sorted(t.F.begin(),t.F.end()),
            "noncanonical original T/F source ID order");
    t.domains.resize(tcount);
    for(auto &v:t.domains){
        in>>v;
        require(bool(in)&&v>0&&v<(uint64_t(1)<<PAL),
                "exact frozen source domain must be nonempty and subset of 51 palettes");
    }
    std::string extra;require(!(in>>extra),"extra tokens in source input");
    t.candidates.resize(tcount);
    for(int a=0;a<tcount;a++){
        const auto &source=t.columns[t.T[a]];
        for(int p=0;p<PAL;p++){
            Limb v=source.base;
            for(int q=0;q<4;q++){
                int position=source.support[q],g=position/4,r=position%4;
                int x=v[g];
                x+=(t.palettes[p][q]-digit(x,r))*powers[r];
                require(0<=x&&x<RAD,"candidate GF5 source limb overflow");
                v[g]=uint16_t(x);
            }
            t.candidates[a][p]=v;
        }
    }
    return t;
}
struct SignedEvent{
    int k=0;
    std::array<int,3> pos{-1,-1,-1},neg{-1,-1,-1};
    std::vector<int> alteredSourceIDs;
};
static SignedEvent equal_event(const std::vector<int>&a,
                               const std::vector<int>&b,
                               const std::set<int>&selected){
    std::vector<int> x,y;
    for(int p:a)if(std::find(b.begin(),b.end(),p)==b.end())x.push_back(p);
    for(int q:b)if(std::find(a.begin(),a.end(),q)==a.end())y.push_back(q);
    require(x.size()==y.size()&&x.size()>=1&&x.size()<=3,
            "signed original equal-sum overlap invalid");
    SignedEvent result;
    result.k=int(x.size());
    if(y<x)std::swap(x,y);
    for(int i=0;i<result.k;i++){
        result.pos[i]=x[i];result.neg[i]=y[i];
    }
    for(int id:x)if(selected.count(id))result.alteredSourceIDs.push_back(id);
    for(int id:y)if(selected.count(id))result.alteredSourceIDs.push_back(id);
    std::sort(result.alteredSourceIDs.begin(),result.alteredSourceIDs.end());
    require(result.alteredSourceIDs.size()>=1,
            "all-frozen source event contradicts true original minimum cover");
    return result;
}
struct State{
    const Input &src;
    std::vector<Limb> current;
    std::set<int> selected;
    std::unordered_map<Key,uint32_t,Hash> fPairs,fTriples;
    uint64_t f_pair_total=0,f_triple_total=0;
    explicit State(const Input& t):src(t),current(t.n){
        selected.insert(t.T.begin(),t.T.end());
        for(int i=0;i<t.n;i++)current[i]=t.columns[i].base;
        const auto &F=t.F;
        f_pair_total=uint64_t(F.size())*(F.size()-1)/2;
        f_triple_total=uint64_t(F.size())*(F.size()-1)*(F.size()-2)/6;
        fPairs.reserve(size_t(f_pair_total*1.25)+1);
        fTriples.reserve(size_t(f_triple_total*1.25)+1);
        for(size_t a=0;a+1<F.size();a++)for(size_t b=a+1;b<F.size();b++){
            int i=F[a],j=F[b];
            Key key=sig(plus(current[i],current[j],src.ng),src.ng);
            require(fPairs.emplace(key,pack2(i,j)).second,
                    "frozen core has actual original R2 collision");
        }
        for(size_t a=0;a+2<F.size();a++)for(size_t b=a+1;b+1<F.size();b++){
            int i=F[a],j=F[b];
            Limb part=plus(current[i],current[j],src.ng);
            for(size_t c=b+1;c<F.size();c++){
                int k=F[c];
                Key key=sig(plus(part,current[k],src.ng),src.ng);
                require(fTriples.emplace(key,pack3(i,j,k)).second,
                        "frozen core has original 1/2/3-subset equality");
            }
        }
        require(fPairs.size()==f_pair_total&&fTriples.size()==f_triple_total,
                "complete original F-only pair/triple source census incomplete");
    }
};
struct Audit{
    bool fullScan=true,zero=false;
    uint64_t checkedPairs=0,checkedTriples=0;
    std::vector<SignedEvent> events;
};
static Audit audit(State&state,const std::vector<int>&palettes,int maxEvents){
    const auto &t=state.src;
    require(palettes.size()==t.T.size(),"candidate must assign EVERY editable ORIGINAL ID");
    for(size_t k=0;k<t.T.size();k++){
        int p=palettes[k];
        require(0<=p&&p<PAL&&((t.domains[k]>>p)&1),
                "candidate violates the independently verified 51 source fiber");
        state.current[t.T[k]]=t.candidates[k][p];
    }
    Audit result;
    std::unordered_map<Key,uint32_t,Hash> otherPairs,otherTriples;
    const uint64_t neededPairs=uint64_t(t.T.size())*t.F.size()+
         uint64_t(t.T.size())*(t.T.size()-1)/2;
    const uint64_t neededTriples=
          uint64_t(t.T.size())*t.F.size()*(t.F.size()-1)/2+
          uint64_t(t.T.size())*(t.T.size()-1)/2*t.F.size()+
          uint64_t(t.T.size())*(t.T.size()-1)*(t.T.size()-2)/6;
    otherPairs.reserve(size_t(neededPairs*1.5)+1);
    otherTriples.reserve(size_t(neededTriples*1.3)+1);
    auto emit=[&](const std::vector<int>&positive,const std::vector<int>&negative){
        SignedEvent e=equal_event(positive,negative,state.selected);
        if(e.k==1)throw std::runtime_error(
            "identical singleton source after legal recoloring");
        result.events.push_back(e);
        if(int(result.events.size())>=maxEvents){
            result.fullScan=false;
            return true;
        }
        return false;
    };
    auto pair=[&](int i,int j){
        ++result.checkedPairs;
        Key key=sig(plus(state.current[i],state.current[j],t.ng),t.ng);
        if(auto x=state.fPairs.find(key);x!=state.fPairs.end()){
            auto ab=unpack2(x->second);
            if(emit({i,j},{ab[0],ab[1]}))return true;
        }
        auto v=otherPairs.emplace(key,pack2(i,j));
        if(!v.second){
            auto ab=unpack2(v.first->second);
            if(emit({i,j},{ab[0],ab[1]}))return true;
        }
        return false;
    };
    for(int i:t.T)for(int j:t.F)if(pair(i,j))return result;
    for(size_t a=0;a+1<t.T.size();a++)
        for(size_t b=a+1;b<t.T.size();b++)
            if(pair(t.T[a],t.T[b]))return result;
    require(result.checkedPairs==neededPairs,"not all dynamic ORIGINAL pairs examined");
    auto triple=[&](int i,int j,int k,const Limb &sum12){
        ++result.checkedTriples;
        Key key=sig(plus(sum12,state.current[k],t.ng),t.ng);
        if(auto x=state.fTriples.find(key);x!=state.fTriples.end()){
            auto ids=unpack3(x->second);
            if(emit({i,j,k},{ids[0],ids[1],ids[2]}))return true;
        }
        auto v=otherTriples.emplace(key,pack3(i,j,k));
        if(!v.second){
            auto ids=unpack3(v.first->second);
            if(emit({i,j,k},{ids[0],ids[1],ids[2]}))return true;
        }
        return false;
    };
    const auto& F=t.F;const auto&T=t.T;
    for(int ti:T){
        const auto &cv=state.current[ti];
        for(size_t a=0;a+1<F.size();a++){
            int fa=F[a];
            Limb partial=plus(cv,state.current[fa],t.ng);
            for(size_t b=a+1;b<F.size();b++){
                if(triple(ti,fa,F[b],partial))return result;
            }
        }
    }
    for(size_t a=0;a+1<T.size();a++)
        for(size_t b=a+1;b<T.size();b++){
            int i=T[a],j=T[b];
            Limb partial=plus(state.current[i],state.current[j],t.ng);
            for(int k:F)if(triple(i,j,k,partial))return result;
        }
    for(size_t a=0;a+2<T.size();a++)
        for(size_t b=a+1;b+1<T.size();b++){
            int i=T[a],j=T[b];
            Limb partial=plus(state.current[i],state.current[j],t.ng);
            for(size_t c=b+1;c<T.size();c++)
                if(triple(i,j,T[c],partial))return result;
        }
    require(result.checkedTriples==neededTriples,
            "not all dynamic original triple GF5 signatures audited");
    result.zero=result.events.empty();
    return result;
}
static void jsonIds(std::ostream&out,const std::array<int,3>&v,int n){
    out<<"[";
    for(int i=0;i<n;i++){if(i)out<<",";out<<v[i];}
    out<<"]";
}
int main(int argc,char**argv){
    try{
        require(argc==3,"usage: SOURCE.txt max_witnesses; then one line per complete candidate");
        int maxEvents=std::stoi(argv[2]);
        require(maxEvents>=1&&maxEvents<=4096,"incorrect bounded true-source witnesses");
        init_lut();
        Input input=read_original_source(argv[1]);
        State state(input); // complete expensive F-only cache, ONCE
        std::cout<<"ORIGINAL_CEGAR_READY "<<input.scheme<<" "<<input.T.size()
                 <<" "<<state.f_pair_total<<" "<<state.f_triple_total<<"\n"<<std::flush;
        std::string line;
        while(std::getline(std::cin,line)){
            if(line=="QUIT")break;
            std::istringstream in(line);
            std::vector<int> chosen(input.T.size());
            for(auto&p:chosen)
                require(bool(in>>p),"incomplete candidate source coefficient vector");
            std::string extra;
            require(!(in>>extra),"extra palette in candidate");
            Audit a=audit(state,chosen,maxEvents);
            std::cout<<"ORIGINAL_CEGAR_RESULT {\"scheme\":\""<<input.scheme
                     <<"\",\"zero\":"<<(a.zero?"true":"false")
                     <<",\"full_scan\":"<<(a.fullScan?"true":"false")
                     <<",\"dynamic_pairs_checked\":"<<a.checkedPairs
                     <<",\"dynamic_triples_checked\":"<<a.checkedTriples
                     <<",\"max_witnesses\":"<<maxEvents
                     <<",\"assigned_palettes\":[";
            for(size_t p=0;p<chosen.size();p++){
                if(p)std::cout<<",";
                std::cout<<chosen[p];
            }
            std::cout<<"],\"events\":[";
            for(size_t j=0;j<a.events.size();j++){
                if(j)std::cout<<",";
                const auto &e=a.events[j];
                std::cout<<"{\"k\":"<<e.k<<",\"positive_original_IDs\":";
                jsonIds(std::cout,e.pos,e.k);
                std::cout<<",\"negative_original_IDs\":";
                jsonIds(std::cout,e.neg,e.k);
                std::cout<<",\"edited_original_IDs\":[";
                for(size_t q=0;q<e.alteredSourceIDs.size();q++){
                    if(q)std::cout<<",";
                    std::cout<<e.alteredSourceIDs[q];
                }
                std::cout<<"]}";
            }
            std::cout<<"]}\n"<<std::flush;
        }
        return 0;
    }catch(const std::exception&e){
        std::cerr<<"ORIGINAL_CEGAR_FAIL_CLOSED: "<<e.what()<<"\n";
        return 1;
    }
}
