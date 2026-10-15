// HYP-105 #230 D6-AA4-Y2: genuine ORIGINAL half-projection feature
// gradient Gram energies. Reuses the already independently audited
// C++20 source six-incidence enumerator of AA4-Y-CYC. The only purpose
// of the renamed parent entry point is to reuse its exact original
// generator WITHOUT running its 11,236 global-map-pair main program.
#define main aa4y_previous_matrix_main
#include "hyp105_issue230_d6aa4ycyc_bilateral_original_join.cpp"
#undef main

struct Mode {
    uint64_t key=0;
    uint64_t cycle=0;
    int tag=0;
    bool operator<(const Mode& o) const {
        if(key!=o.key)return key<o.key;
        if(cycle!=o.cycle)return cycle<o.cycle;
        return tag<o.tag;
    }
};
static int source_shape_kind(const Model& m,uint64_t key,int side) {
    Flags flags=flags_from(key);
    array<int,15> multiplicities{};
    for(int flag:flags) {
        int source=(side==0?m.point[flag]:m.line[flag]);
        multiplicities[source]++;
    }
    array<int,6> positive{};
    int k=0;
    for(int c:multiplicities)if(c>0) {
        if(k>=6)return -1;
        positive[k++]=c;
    }
    sort(positive.begin(),positive.end(),greater<int>());
    if(k==6&&positive[0]==1)return 0; // A
    if(k==5&&positive[0]==2&&positive[1]==1)return 1; // B
    if(k==3&&positive[0]==2&&positive[1]==2&&positive[2]==2)return 2; // C
    return -1;
}
static int source_class_tag(const Model& m,const Row& row,int side) {
    int left=side==0?row.kind:source_shape_kind(m,row.key,0);
    int right=side==1?row.kind:source_shape_kind(m,row.key,1);
    if(left<0||right<0)return -1;
    if(left==0&&right==0)return 0;  // positional C6 mode
    if(left==1&&right==0)return 1;
    if(left==0&&right==1)return 2;
    if((left==0&&right==2)||(left==2&&right==0))return 3;
    if((left==1&&right==2)||(left==2&&right==1))return 4;
    if(left==1&&right==1) {
        Flags q=flags_from(row.key);
        array<int,15> pc{},lc{};
        for(int id:q){pc[m.point[id]]++;lc[m.line[id]]++;}
        int rp=-1,rl=-1;
        for(int i=0;i<15;i++){
            if(pc[i]==2)rp=i;
            if(lc[i]==2)rl=i;
        }
        ensure(rp>=0&&rl>=0,"BB genuine source doubled factors absent");
        bool overlap=false;
        for(int id:q)if(m.point[id]==rp&&m.line[id]==rl)overlap=true;
        return overlap?5:6;
    }
    if(left==2&&right==2)
        throw runtime_error("GQ girth 8 forbids ORIGINAL source C/C");
    throw runtime_error("unrecognized genuine ORIGINAL seven source cell");
}
static vector<Mode> feature_index(const Model& m,vector<Row>& rows,int side) {
    vector<Mode> index;
    index.reserve(rows.size());
    for(const Row& row:rows) {
        int tag=source_class_tag(m,row,side);
        if(tag<0)continue;
        // AA only accepted if this half projects to CONNECTED C6;
        // source non-AA has a SINGLE scalar mode per genuine original Q.
        if(tag==0&&row.cycle==0)continue;
        index.push_back({row.key,tag==0?row.cycle:0,tag});
    }
    sort(index.begin(),index.end());
    for(size_t i=1;i<index.size();i++)
        ensure(!(index[i].key==index[i-1].key&&
                 index[i].cycle==index[i-1].cycle&&
                 index[i].tag==index[i-1].tag),
               "duplicate true-original projection mode");
    return index;
}
static array<uint64_t,7> gradient_energy(const vector<Mode>& baseline,
                                          const vector<Mode>& updated) {
    size_t i=0,j=0;
    array<uint64_t,7> energy{};
    while(i<baseline.size()||j<updated.size()) {
        if(j==updated.size()||
           (i<baseline.size()&&baseline[i]<updated[j])) {
            energy[size_t(baseline[i].tag)]++;
            i++;
        } else if(i==baseline.size()||updated[j]<baseline[i]) {
            energy[size_t(updated[j].tag)]++;
            j++;
        } else {i++;j++;}
    }
    return energy;
}
#ifndef HYP105_Y2_GRAD_LIBRARY_ONLY
int main() {
    try {
        const Model m=load_model();
        const auto physical_two=two_factors(m);
        const auto physical_matchings=matchings(m);
        vector<pair<int,int>> swaps={{-1,-1}};
        for(int i=0;i<15;i++)for(int j=i+1;j<15;j++)swaps.push_back({i,j});
        ensure(swaps.size()==106,"all source point/line swap variants needed");
        cout<<"side\tmove\tD6\tBleft\tAleft\tCA\tCB\tBBover\tBBdisjoint\n";
        for(int side=0;side<2;side++) {
            const auto& origin=(side==0?m.f:m.g);
            auto original_half=make_half(m,side,origin,physical_two,physical_matchings);
            const auto baseline=feature_index(m,original_half,side);
            for(int move=0;move<106;move++) {
                auto labels=origin;
                if(move) {
                    auto [u,v]=swaps[size_t(move)];
                    swap(labels[size_t(u)],labels[size_t(v)]);
                }
                vector<Row> candidate=move?
                    make_half(m,side,labels,physical_two,physical_matchings):
                    original_half;
                auto current=move?feature_index(m,candidate,side):baseline;
                const auto E=gradient_energy(baseline,current);
                if(move==0)ensure(all_of(E.begin(),E.end(),
                    [](uint64_t n){return n==0;}),"identity gradient not zero");
                cout<<side<<'\t'<<move;
                for(uint64_t n:E)cout<<'\t'<<n;
                cout<<'\n';
            }
            cerr<<"GENUINE ORIGINAL SOURCE "<<(side==0?"POINT":"LINE")
                <<" COMPLETE 106 TRUE SIX-FLAG MODE GRADIENTS PASS\n";
        }
        return 0;
    } catch(const exception& ex) {
        cerr<<"HYP-105 Y2 ORIGINAL FEATURE ENERGY FAIL CLOSED: "<<ex.what()<<'\n';
        return 1;
    }
}

#endif // HYP105_Y2_GRAD_LIBRARY_ONLY
