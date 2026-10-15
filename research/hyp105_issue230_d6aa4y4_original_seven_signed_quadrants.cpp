// HYP-105 issue #230 / D6-AA4-Y4.
// Reconstruct seven historical true-ORIGINAL GF5 modes on the SAME six
// actual source incidence IDs. Full 106x106 simultaneous global point+
// line physical-edge-label swap grid; each of 7 immutable source tags
// gets exact four signed-mode quadrants ++,--,+-,-+.
// Reuse preceding independently verified Y2 ORIGINAL feature generator.
#define main hyp105_y2_original_signed_conflict_main
#include "hyp105_issue230_d6aa4y2_original_signed_conflicts.cpp"
#undef main

using Quadrants=array<array<uint64_t,4>,7>;

static Quadrants true_original_seven_signed_quadrants(
    const vector<SignedMode>& point,const vector<SignedMode>& line
) {
    size_t i=0,j=0;
    Quadrants q{};
    while(i<point.size() && j<line.size()) {
        if(point[i].feature<line[j].feature) { ++i; continue; }
        if(line[j].feature<point[i].feature) { ++j; continue; }
        const int t=point[i].feature.tag;
        ensure(t>=0 && t<7 && t==line[j].feature.tag,
            "tag must be immutable original source forest type for SAME mode");
        const int p=point[i].sign,l=line[j].sign;
        ensure((p==1||p==-1)&&(l==1||l==-1),
            "only +/-1 true original binary mode gradients allowed");
        // Quadrant column order: (++), (--), (+-), (-+).
        const int k=(p==1&&l==1) ? 0 : ((p==-1&&l==-1) ? 1 :
                      ((p==1&&l==-1) ? 2 : 3));
        ++q[size_t(t)][size_t(k)];
        ++i;++j;
    }
    return q;
}

int main() {
    try {
        const Model m=load_model();
        const auto two=two_factors(m),matching=matchings(m);
        vector<pair<int,int>> moves={{-1,-1}};
        for(int p=0;p<15;p++) for(int q=p+1;q<15;q++)
            moves.push_back({p,q});
        ensure(moves.size()==106,"full original source transposition catalog invalid");
        array<vector<vector<SignedMode>>,2> differences;
        for(int side=0;side<2;side++) {
            const auto orig=(side==0?m.f:m.g);
            const auto base_rows=make_half(m,side,orig,two,matching);
            const auto base_modes=feature_index(m,base_rows,side);
            differences[size_t(side)].reserve(106);
            for(auto [u,v]:moves) {
                auto labels=orig;
                if(u>=0)swap(labels[size_t(u)],labels[size_t(v)]);
                auto rows=u>=0?make_half(m,side,labels,two,matching):base_rows;
                auto modes=u>=0?feature_index(m,rows,side):base_modes;
                differences[size_t(side)].push_back(signed_diff(base_modes,modes));
            }
            ensure(differences[size_t(side)].size()==106,
                "missing globally coherent original source map");
            ensure(differences[size_t(side)][0].empty(),
                "identity has nonzero source feature gradient");
        }

        cout<<"point_move\tline_move";
        const char* tags[]={"D6","Bleft","Aleft","CA","CB","BBover","BBdisjoint"};
        const char* quadrants[]={"pp","nn","pn","np"};
        for(auto t:tags)for(auto q:quadrants)cout<<'\t'<<t<<'_'<<q;
        cout<<'\n';
        for(int i=0;i<106;i++)for(int j=0;j<106;j++) {
            auto Q=true_original_seven_signed_quadrants(
                differences[0][size_t(i)],differences[1][size_t(j)]);
            cout<<i<<'\t'<<j;
            for(const auto& tag:Q)for(auto n:tag)cout<<'\t'<<n;
            cout<<'\n';
        }
        cerr<<"GENUINE ORIGINAL 11236 SEVEN-CLASS SIGNED POSITIONAL MODE QUADRANTS COMPLETE\n";
        return 0;
    } catch(const exception& e) {
        cerr<<"HYP105 Y4 TRUE ORIGINAL CLASS-SIGNED FAILURE: "<<e.what()<<'\n';
        return 1;
    }
}
