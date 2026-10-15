// HYP-105 / issue #230 / D6-AA4-Y-CYC
// Exact finite ORIGINAL W(3,2) simultaneous point+line physical-label
// transposition matrix: 106*106 FULL globally injected map pairs.
// Native enumeration of original six-flag half A/B/C sets on BOTH sides,
// sort-merge join on the SAME 6 actual original incidence IDs. No
// stochastic maps, no independent 6set physical reassignments.
//
// Input: 45 true original "point line" flags, then 15 point physical edges,
// then 15 line physical edges. All physical edges are canonical K6 pairs.
// Output TSV: point_move line_move D6 Bleft Aleft CA CB BBover BBdisjoint S weight.
// Variant 0 = identity; variants 1..105 = lexicographic source-factor swaps.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using namespace std;
using Edge=array<int,2>;
using Flags=array<int,6>;
struct Row {
    uint64_t key=0, cycle=0;
    uint8_t kind=255, repeat=255;
};
struct Totals { array<uint64_t,7> n{}; };
struct Model {
    array<int,45> point{}, line{};
    array<Edge,15> f{},g{};
    array<Edge,15> physical{};
    array<array<vector<int>,15>,2> flags{};
};
static void ensure(bool ok, const string& error) {
    if(!ok) throw runtime_error(error);
}
static uint64_t key_of(Flags ids) {
    sort(ids.begin(),ids.end());
    for(int k=0;k<6;k++) {
        ensure(ids[k]>=0 && ids[k]<45,"bad original flag");
        if(k) ensure(ids[k-1]!=ids[k],"not six distinct original flags");
    }
    uint64_t value=0;
    for(int i=0;i<6;i++) value |= uint64_t(ids[i])<<(6*i);
    return value;
}
static Flags flags_from(uint64_t key) {
    Flags a{};
    for(int i=0;i<6;i++) a[i]=int((key>>(6*i))&63);
    return a;
}
static int phys_id(const Model& m,Edge e) {
    if(e[0]>e[1]) swap(e[0],e[1]);
    for(int i=0;i<15;i++) if(m.physical[i]==e) return i;
    throw runtime_error("physical pair not in K6");
}
static Model load_model() {
    Model m;
    int at=0;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)m.physical[at++]={a,b};
    for(int i=0;i<45;i++) {
        ensure(bool(cin>>m.point[i]>>m.line[i]),"missing original incidence");
        ensure(m.point[i]>=0&&m.point[i]<15&&m.line[i]>=0&&m.line[i]<15,
               "bad original incidence endpoint");
        m.flags[0][m.point[i]].push_back(i);
        m.flags[1][m.line[i]].push_back(i);
    }
    for(int side=0;side<2;side++)for(auto &v:m.flags[side])
        ensure(v.size()==3,"W32 every source point and line must have degree3");
    for(int a=0;a<15;a++)for(int b=a+1;b<15;b++) {
        int common=0;
        for(int i=0;i<45;i++)if(m.point[i]==a)
          for(int j=0;j<45;j++)if(m.point[j]==b&&m.line[i]==m.line[j])
            common++;
        ensure(common<=1,"source partial linearity failed");
    }
    for(int side=0;side<2;side++) {
        auto& labels=(side==0 ? m.f : m.g);
        int seen=0;
        for(auto& edge: labels) {
            ensure(bool(cin>>edge[0]>>edge[1]),"missing physical edge label");
            ensure(0<=edge[0]&&edge[0]<edge[1]&&edge[1]<6,"noncanonical physical pair");
            int id=phys_id(m,edge);
            ensure(!(seen&(1<<id)),"physical labels not globally injective");
            seen |=1<<id;
        }
        ensure(seen==(1<<15)-1,"incomplete physical K6 bijection");
    }
    return m;
}
static vector<array<int,6>> two_factors(const Model& m) {
    vector<array<int,6>> result;
    for(int a=0;a<10;a++)for(int b=a+1;b<11;b++)
    for(int c=b+1;c<12;c++)for(int d=c+1;d<13;d++)
    for(int e=d+1;e<14;e++)for(int f=e+1;f<15;f++) {
        array<int,6> indexes={a,b,c,d,e,f};
        array<int,6> deg{};
        for(auto q:indexes) {
            deg[m.physical[q][0]]++;
            deg[m.physical[q][1]]++;
        }
        if(all_of(deg.begin(),deg.end(),[](int x){return x==2;}))
            result.push_back(indexes);
    }
    ensure(result.size()==70,"K6 two-factors !=70");
    return result;
}
static void matching_rec(const Model& m,vector<int>& used,
                         vector<int>& edges,vector<array<int,3>>& out) {
    int first=-1;
    for(int i=0;i<6;i++)if(!used[i]){first=i;break;}
    if(first<0) {
        ensure(edges.size()==3,"bad perfect matching edge length");
        out.push_back({edges[0],edges[1],edges[2]});
        return;
    }
    used[first]=1;
    for(int j=first+1;j<6;j++)if(!used[j]) {
        used[j]=1;
        edges.push_back(phys_id(m,{first,j}));
        matching_rec(m,used,edges,out);
        edges.pop_back();
        used[j]=0;
    }
    used[first]=0;
}
static vector<array<int,3>> matchings(const Model& m) {
    vector<int> used(6),edges;
    vector<array<int,3>> v;
    matching_rec(m,used,edges,v);
    ensure(v.size()==15,"K6 perfect matchings !=15");
    return v;
}
static uint64_t connected_6cycle_mask(const Model& m, const Flags& ids,
                                      const array<Edge,15>& labels, int side) {
    array<vector<int>,6> positions{};
    for(int i=0;i<6;i++) {
        int source=(side==0?m.point[ids[i]]:m.line[ids[i]]);
        auto edge=labels[source];
        positions[edge[0]].push_back(i);
        positions[edge[1]].push_back(i);
    }
    array<int,6> adj{};
    uint64_t mask=0;
    for(auto& vec:positions) {
        ensure(vec.size()==2,"A pattern not two regular in 6 physical colors");
        int a=vec[0],b=vec[1];
        ensure(a!=b,"physical coordinate self loop");
        adj[a]|=1<<b; adj[b]|=1<<a;
        mask|=uint64_t(1)<<(6*a+b);
    }
    for(int i=0;i<6;i++)ensure(__builtin_popcount(unsigned(adj[i]))==2,
                              "A pattern not simple 2factor");
    int visited=1,work=1;
    while(work) {
        int i=__builtin_ctz(unsigned(work));
        work&=~(1<<i);
        int fresh=adj[i]&~visited;
        visited|=fresh; work|=fresh;
    }
    return visited==63?mask:0; // AA 2 triangles rejected for genuine D6.
}
static vector<Row> make_half(const Model& m,int side,
                             const array<Edge,15>& labels,
                             const vector<array<int,6>>& two,
                             const vector<array<int,3>>& perfect) {
    array<int,15> inverse{};
    for(int source=0;source<15;source++)
        inverse[phys_id(m,labels[source])]=source;
    vector<Row> out;
    out.reserve(62370);

    // Recursion choosing one or two actual distinct original incidence
    // IDs at each physically prescribed original factor.
    auto emit=[&](const vector<vector<Flags>>& options, const vector<int>& sizes,
                  int kind,int root) {
        Flags current{};
        auto rec=[&](auto&& self,int group,int filled)->void {
            if(group==int(options.size())) {
                ensure(filled==6,"wrong original six incidence count");
                Flags ids=current;
                uint64_t key=key_of(ids);
                sort(ids.begin(),ids.end());
                uint64_t cycle=kind==0?
                    connected_6cycle_mask(m,ids,labels,side):0;
                out.push_back({key,cycle,uint8_t(kind),uint8_t(root)});
                return;
            }
            for(const Flags& chosen:options[group]) {
                int n=sizes[group];
                for(int j=0;j<n;j++)current[filled+j]=chosen[j];
                self(self,group+1,filled+n);
            }
        };
        rec(rec,0,0);
    };
    auto single=[&](int source){
        vector<Flags> opts;
        for(int id:m.flags[side][source]) {
            Flags tmp{}; tmp[0]=id;opts.push_back(tmp);
        }
        return opts;
    };
    auto doubled=[&](int source){
        vector<Flags> opts;
        const auto& a=m.flags[side][source];
        for(int i=0;i<3;i++)for(int j=i+1;j<3;j++) {
            Flags t{};t[0]=a[i];t[1]=a[j];opts.push_back(t);
        }
        return opts;
    };
    for(const auto& edges:two) {
        vector<vector<Flags>> options;
        for(int phys:edges)options.push_back(single(inverse[phys]));
        emit(options,{1,1,1,1,1,1},0,255);
    }
    // B: one twice-used factor plus physical four-cycle on disjoint colors.
    for(int root=0;root<15;root++) {
        const auto e=m.physical[root];
        vector<int> other;
        for(int c=0;c<6;c++)if(c!=e[0]&&c!=e[1])other.push_back(c);
        ensure(other.size()==4,"bad B physical root complement");
        for(int match=0;match<3;match++) {
            array<Edge,2> excluded;
            if(match==0)excluded={Edge{other[0],other[1]},Edge{other[2],other[3]}};
            if(match==1)excluded={Edge{other[0],other[2]},Edge{other[1],other[3]}};
            if(match==2)excluded={Edge{other[0],other[3]},Edge{other[1],other[2]}};
            vector<vector<Flags>> options={doubled(inverse[root])};
            for(int i=0;i<4;i++)for(int j=i+1;j<4;j++) {
                Edge candidate={other[i],other[j]};
                if(candidate==excluded[0]||candidate==excluded[1])continue;
                options.push_back(single(inverse[phys_id(m,candidate)]));
            }
            ensure(options.size()==5,"B physical complement needs 4cycle");
            emit(options,{2,1,1,1,1},1,inverse[root]);
        }
    }
    for(const auto& matching:perfect) {
        vector<vector<Flags>> options;
        for(int phys:matching)options.push_back(doubled(inverse[phys]));
        emit(options,{2,2,2},2,255);
    }
    ensure(out.size()==62370,"W32 half candidate count !=62370");
    sort(out.begin(),out.end(),[](const Row& a,const Row& b){return a.key<b.key;});
    for(size_t i=1;i<out.size();i++)ensure(out[i-1].key!=out[i].key,
                                           "duplicate true original Q in half index");
    return out;
}
static Totals join_exact(const Model& m,const vector<Row>& left,
                          const vector<Row>& right) {
    size_t i=0,j=0;
    Totals totals;
    while(i<left.size()&&j<right.size()) {
        if(left[i].key<right[j].key) {i++;continue;}
        if(right[j].key<left[i].key) {j++;continue;}
        const Row& a=left[i],&b=right[j];
        int tag=-1;
        if(a.kind==0&&b.kind==0) {
            if(a.cycle!=0&&a.cycle==b.cycle)tag=0; // D6
        } else if(a.kind==1&&b.kind==0)tag=1;
        else if(a.kind==0&&b.kind==1)tag=2;
        else if((a.kind==0&&b.kind==2)||(a.kind==2&&b.kind==0))tag=3;
        else if((a.kind==1&&b.kind==2)||(a.kind==2&&b.kind==1))tag=4;
        else if(a.kind==1&&b.kind==1) {
            bool overlap=false;
            auto ids=flags_from(a.key);
            for(int id:ids)if(m.point[id]==a.repeat&&m.line[id]==b.repeat)
                overlap=true;
            tag=overlap?5:6;
        } else if(a.kind==2&&b.kind==2) {
            throw runtime_error("forbidden C/C original source 6cycle in genuine GQ");
        } else throw runtime_error("invalid original half A/B/C join");
        if(tag>=0)totals.n[size_t(tag)]++;
        i++;j++;
    }
    return totals;
}
static array<uint64_t,9> full_values(Totals t) {
    // 0..6: historical true original seven class counts; 7 S; 8 51palette
    static constexpr array<uint64_t,7> weight={
        5643,45600,45600,43320,49050,51750,45010
    };
    array<uint64_t,9> out{};
    for(int i=0;i<7;i++) {
        out[i]=t.n[i];
        out[7]+=t.n[i];
        out[8]+=t.n[i]*weight[i];
    }
    return out;
}
int main() {
    try {
        const Model m=load_model();
        const auto factors=two_factors(m);
        const auto perfect=matchings(m);
        vector<pair<int,int>> swaps={{-1,-1}};
        for(int u=0;u<15;u++)for(int v=u+1;v<15;v++)swaps.push_back({u,v});
        ensure(swaps.size()==106,"incorrect 105+identity source move catalog");
        array<vector<vector<Row>>,2> indices;
        for(int side=0;side<2;side++) {
            const auto& original=(side==0?m.f:m.g);
            indices[side].reserve(106);
            for(auto [u,v]:swaps) {
                auto labels=original;
                if(u>=0)swap(labels[u],labels[v]);
                indices[side].push_back(make_half(m,side,labels,factors,perfect));
            }
            cerr<<"BUILT ORIGINAL "<<(side==0?"POINT":"LINE")
                <<" PHYSICAL HALF INDEX 106 x 62370\n";
        }
        cout<<"point_move\tline_move\tD6\tBleft\tAleft\tCA\tCB\tBBover\tBBdisjoint\tS\tweight\n";
        for(int p=0;p<106;p++) {
            for(int l=0;l<106;l++) {
                auto values=full_values(join_exact(m,indices[0][p],indices[1][l]));
                cout<<p<<'\t'<<l;
                for(auto n:values)cout<<'\t'<<n;
                cout<<'\n';
            }
            if(p%16==0)cerr<<"JOINED point variant "<<p<<"/105\n";
        }
        cerr<<"GENUINE ORIGINAL 106x106 BILATERAL MATRIX COMPLETE\n";
        return 0;
    } catch(const exception& e) {
        cerr<<"HYP-105 ORIGINAL GQ FAIL CLOSED: "<<e.what()<<'\n';
        return 1;
    }
}
