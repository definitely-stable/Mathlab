// HYP-105 #230 / D6-AA4-V-CYC
// Exact full ORIGINAL W32 D6 second moment under ONE globally uniform
// complete right GQ source-line injection, with arbitrary fixed full f.
//
// PYTHON producer proves that N=21,186 actual six-ORIGINAL-incidence Q,
// each with distinct true source line factor IDs, compress to M distinct
// undirected SOURCE-LINE 6-cycles C with integer multiplicities w_f(C).
// These Q share EXACTLY the same historical D6 acceptance event under
// one global g iff they induce the same source-line C6 edge graph.
//
// PYTHON also builds the exact ALL-h 13,327 partial positional gluing
// table for physical a=6, with joint probabilities encoded as integer
// numerator divided by D=(15)_12. This C++ kernel only counts the
// *genuine ORIGINAL weighted pair* histogram, avoiding the 448,846,596
// QxQ uncompressed Python pair iterations.
// One complete globally injected original g is used per probabilistic
// event; no independent Q local injection is applied.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
using u64 = std::uint64_t;
using u128 = unsigned __int128;
static constexpr unsigned ALPHABET = 7;
static constexpr unsigned LOOKUP_SIZE = 117649; // 7^6
static constexpr u64 D = 217945728000ULL; // (15)_12

static std::string decimal(u128 x) {
    if(x==0) return "0";
    std::string s;
    while(x) { s.push_back('0'+static_cast<unsigned>(x%10)); x/=10; }
    std::reverse(s.begin(),s.end());
    return s;
}
struct Cycle {
    u64 weight;
    std::array<unsigned char,6> line;
};
int main() {
    try {
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
        unsigned n, anchor;
        if(!(std::cin>>n>>anchor) || !n || n>21186 || anchor>=n)
            throw std::runtime_error("invalid original source line C6 group header");
        std::vector<Cycle> a(n);
        u64 total=0;
        for(unsigned i=0;i<n;++i) {
            if(!(std::cin>>a[i].weight) || !a[i].weight)
                throw std::runtime_error("invalid positive true original Q multiplicity");
            total+=a[i].weight;
            unsigned mask=0;
            for(int j=0;j<6;++j) {
                unsigned x;
                if(!(std::cin>>x) || x>=15 || ((mask>>x)&1))
                    throw std::runtime_error("invalid six different original LINE IDs");
                mask|=(1u<<x); a[i].line[j]=static_cast<unsigned char>(x);
            }
        }
        if(total!=21186) throw std::runtime_error("true original AA Q total not exactly 21186");
        std::vector<u64> kernels(LOOKUP_SIZE);
        unsigned valid_count=0;
        for(unsigned i=0;i<LOOKUP_SIZE;++i) {
            std::int64_t value;
            if(!(std::cin>>value) || value< -1)
                throw std::runtime_error("invalid exact cyclic glue pair lookup");
            if(value>=0) { kernels[i]=static_cast<u64>(value); ++valid_count; }
            else kernels[i]=std::numeric_limits<u64>::max();
        }
        if(valid_count!=13327)
            throw std::runtime_error("not all 13327 valid original relative C6 matching diagrams");

        u128 moment_numerator=0;
        u128 anchored_numerator=0;
        std::array<u128,7> overlap_counts{};
        std::array<u128,7> overlap_positive{};
        std::array<u128,7> overlap_weighted_moment{};
        u128 positive_pairs=0,zero_pairs=0;
        for(unsigned i=0;i<n;++i) {
            std::array<unsigned char,15> positions;
            positions.fill(6);
            for(unsigned j=0;j<6;++j) positions[a[i].line[j]]=static_cast<unsigned char>(j);
            u128 row=0;
            const u64 wi=a[i].weight;
            for(unsigned j=0;j<n;++j) {
                unsigned code=0,overlap=0;
                for(int slot=0;slot<6;++slot) {
                    const unsigned pos=positions[a[j].line[slot]];
                    code=ALPHABET*code+pos;
                    overlap+=(pos!=6);
                }
                const u64 probnum=kernels[code];
                if(probnum==std::numeric_limits<u64>::max())
                    throw std::runtime_error("cycle pair not valid injective original factor partial map");
                const u128 wj=a[j].weight;
                const u128 pair_weight=static_cast<u128>(wi)*wj;
                const u128 weighted=pair_weight*probnum;
                moment_numerator+=weighted;
                row+=wj*probnum;
                overlap_counts[overlap]+=pair_weight;
                overlap_weighted_moment[overlap]+=weighted;
                if(probnum){ positive_pairs+=pair_weight;overlap_positive[overlap]+=pair_weight; }
                else zero_pairs+=pair_weight;
            }
            if(i==anchor) anchored_numerator=row;
        }
        if(positive_pairs+zero_pairs!=static_cast<u128>(total)*total)
            throw std::runtime_error("all 21186^2 original ordered Q pairs not counted");
        u128 sums=0,parts=0;
        for(int r=0;r<=6;++r){
            sums+=overlap_counts[r];parts+=overlap_weighted_moment[r];
        }
        if(sums!=static_cast<u128>(total)*total||parts!=moment_numerator)
            throw std::runtime_error("moment source original shared-line overlap sector reconciliation failed");

        std::cout<<"{";
        std::cout<<"\"full_original_Q_count\":"<<total<<",";
        std::cout<<"\"distinct_source_line_C6_event_groups\":"<<n<<",";
        std::cout<<"\"full_original_ordered_Q_pairs\":"<<decimal(sums)<<",";
        std::cout<<"\"exact_common_denominator\":"<<D<<",";
        std::cout<<"\"full_conditional_D6_second_moment_numerator\":"<<decimal(moment_numerator)<<",";
        std::cout<<"\"original_Q_anchored_joint_row_numerator\":"<<decimal(anchored_numerator)<<",";
        std::cout<<"\"positive_joint_original_ordered_pairs\":"<<decimal(positive_pairs)<<",";
        std::cout<<"\"zero_joint_original_ordered_pairs\":"<<decimal(zero_pairs)<<",";
        for(const auto category : {0,1,2}) {
            const auto& arr=category==0?overlap_counts:(category==1?overlap_positive:overlap_weighted_moment);
            const char* name=category==0?"source_line_overlap_ordered_pair_counts":
                             category==1?"source_line_overlap_positive_joint_pair_counts":
                                         "source_line_overlap_second_moment_numerators";
            std::cout<<"\""<<name<<"\":[";
            for(int j=0;j<7;++j){if(j)std::cout<<",";std::cout<<decimal(arr[j]);}
            std::cout<<"],";
        }
        std::cout<<"\"all_original_source_six_ID_weight_multiplicities_exact\":true,";
        std::cout<<"\"same_one_global_right_injection_probabilities\":true,";
        std::cout<<"\"full_fixed_f_conditional_second_moment_computed\":true,";
        std::cout<<"\"universal_all_f_g_GF5_S_lower_PROVED\":false";
        std::cout<<"}\n";
    } catch(const std::exception& ex) {
        std::cerr<<"FAIL CLOSED: "<<ex.what()<<"\n";
        return 1;
    }
    return 0;
}
