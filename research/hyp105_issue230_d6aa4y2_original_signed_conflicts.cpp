// HYP-105 issue #230 / D6-AA4-Y2
// NEW exact ALL-h signed-mode conflict decomposition, evaluated for
// complete real ORIGINAL W(3,2) globally injected physical pair labels.
// Distinguish favorable coincident updates (+,+),(-,-) from harmful
// conflicts (+,-),(-,+), on the SAME immutable source 6-flag Q and mode.
#define HYP105_Y2_GRAD_LIBRARY_ONLY
#include "hyp105_issue230_d6aa4y2_original_mode_gradient.cpp"
#undef HYP105_Y2_GRAD_LIBRARY_ONLY

struct SignedMode {
    Mode feature;
    int sign;
};
static vector<SignedMode> signed_diff(const vector<Mode>& base,
                                      const vector<Mode>& changed) {
    size_t a=0,b=0;
    vector<SignedMode> differences;
    while(a<base.size()||b<changed.size()) {
        if(b==changed.size()||(a<base.size()&&base[a]<changed[b])) {
            differences.push_back({base[a],-1});
            a++;
        } else if(a==base.size()||changed[b]<base[a]) {
            differences.push_back({changed[b],+1});
            b++;
        } else {a++;b++;}
    }
    return differences;
}
struct Conflict {
    uint64_t pp=0,nn=0,pn=0,np=0;
    uint64_t wpp=0,wnn=0,wpn=0,wnp=0;
};
static Conflict count_coincident_signed_modes(const vector<SignedMode>& x,
                                                const vector<SignedMode>& y) {
    static constexpr array<uint64_t,7> weight={
        5643,45600,45600,43320,49050,51750,45010
    };
    size_t i=0,j=0;
    Conflict c;
    while(i<x.size()&&j<y.size()) {
        if(x[i].feature<y[j].feature){i++;continue;}
        if(y[j].feature<x[i].feature){j++;continue;}
        auto tag=x[i].feature.tag;
        ensure(tag==y[j].feature.tag&&tag>=0&&tag<7,
               "original mode tag mismatch in signed original-source intersection");
        const uint64_t w=weight[size_t(tag)];
        if(x[i].sign>0&&y[j].sign>0){c.pp++;c.wpp+=w;}
        if(x[i].sign<0&&y[j].sign<0){c.nn++;c.wnn+=w;}
        if(x[i].sign>0&&y[j].sign<0){c.pn++;c.wpn+=w;}
        if(x[i].sign<0&&y[j].sign>0){c.np++;c.wnp+=w;}
        i++;j++;
    }
    return c;
}
int main() {
    try {
        const Model m=load_model();
        const auto physical_two=two_factors(m);
        const auto perfect=matchings(m);
        vector<pair<int,int>> swaps={{-1,-1}};
        for(int u=0;u<15;u++)for(int v=u+1;v<15;v++)
            swaps.push_back({u,v});
        ensure(swaps.size()==106,"missing genuine original full global source swaps");
        array<vector<vector<SignedMode>>,2> derivatives;
        for(int side=0;side<2;side++) {
            const auto origin=(side==0?m.f:m.g);
            const auto rows=make_half(m,side,origin,physical_two,perfect);
            const auto baseline=feature_index(m,const_cast<vector<Row>&>(rows),side);
            derivatives[size_t(side)].reserve(106);
            for(auto [u,v]:swaps) {
                auto labels=origin;
                if(u>=0)swap(labels[size_t(u)],labels[size_t(v)]);
                auto current_rows= u>=0?
                    make_half(m,side,labels,physical_two,perfect) : rows;
                auto current=u>=0?
                    feature_index(m,current_rows,side) : baseline;
                derivatives[size_t(side)].push_back(signed_diff(baseline,current));
            }
            ensure(derivatives[size_t(side)][0].empty(),
                   "original baseline gradient must vanish");
            cerr<<"GENUINE ORIGINAL SIDE "<<side
                <<" 106 COMPLETE SIGNED SIX-INCIDENCE POSITIONAL MODES\n";
        }
        cout<<"point_move\tline_move\tpp\tnn\tpn\tnp\twpp\twnn\twpn\twnp\n";
        for(size_t p=0;p<106;p++) {
            for(size_t l=0;l<106;l++) {
                const auto c=count_coincident_signed_modes(
                    derivatives[0][p],derivatives[1][l]);
                cout<<p<<'\t'<<l<<'\t'<<c.pp<<'\t'<<c.nn<<'\t'
                    <<c.pn<<'\t'<<c.np<<'\t'
                    <<c.wpp<<'\t'<<c.wnn<<'\t'<<c.wpn<<'\t'<<c.wnp<<'\n';
            }
        }
        cerr<<"GENUINE ORIGINAL 11236 EXACT SIGNED MODE CONFLICTS COMPLETE\n";
        return 0;
    } catch(const exception& e) {
        cerr<<"HYP105 ORIGINAL SIGNED CONFLICT FAIL CLOSED: "<<e.what()<<'\n';
        return 1;
    }
}
