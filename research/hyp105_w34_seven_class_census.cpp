// HYP-105 #230 AA4-SEVEN34 — exhaustive finite ORIGINAL B/C six-flag census.
//
// Input: V a N; V point pair labels; V line pair labels; N source (p,l) flags.
// All original source flags are distinct, true geometry independently
// certified by the Python caller.  No synthetic edges or sampled classes.
//
// Accepted A/A D6 is counted independently by #667 source-ID C6 oracle.
// Every other accepted historical class has a B or C endpoint partition:
//  B-left/A-right, A-left/B-right, C/A, C/B, B/B-overlap, B/B-disjoint.
//
// B side: one duplicated source factor (two distinct flags) whose physical
// pair plus four physical edges from four other distinct source factors form
// a 2-regular graph C2+C4.  C side: three distinct factors each selected twice,
// and their physical pair labels form a disjoint 3-matching (C2+C2+C2).
// Each ORIGINAL sixflag set in such a canonical side shape is visited ONCE.
// A/A D6 neither intersects these shapes nor needs to be recounted.
//
// Exact opposite physical six-coordinate degree-2 test uses a 4-bit nibble
// per coordinate.  Six edges contribute total degree 12, and no individual
// degree exceeds 6, so ordinary integer addition has NO nibble carries.
// Test each coordinate nibble is 0 or 2.  No hashing/fitting/roundoff.
//
// B side right-A/B counts; B/B counted only when B is on LEFT.
// C side opposite A/B counts; C/C always historically rejected.
// This is exact structural acceptance; Python verifies on W32 against
// independent historical GF5 seven_census and on W34 sampled witnesses.
// This finite kernel does not assert a universal all-h Omega(s^6) theorem.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
using U=uint64_t;
using P=array<int,2>;
struct Model {
  int V,a,N;
  vector<P> lab[2], flag;
  vector<vector<int>> by[2];
  vector<vector<int>> inverse[2];
  vector<U> otherPack[2];
  U forbidden = 0;
  Model() {
    if(!(cin>>V>>a>>N)) throw runtime_error("missing model header");
    if(V<3||a<6||a>15||N<6) throw runtime_error("unsupported finite alphabet");
    for(int axis=0;axis<2;++axis) {
      lab[axis].resize(V);
      inverse[axis].assign(a,vector<int>(a,-1));
      for(int p=0;p<V;++p) {
        int x,y;
        if(!(cin>>x>>y)||x<0||y<=x||y>=a) throw runtime_error("invalid canonical pair");
        if(inverse[axis][x][y]!=-1) throw runtime_error("noninjective factor pair map");
        inverse[axis][x][y]=p;
        inverse[axis][y][x]=p;
        lab[axis][p]={x,y};
      }
    }
    flag.resize(N);
    by[0].assign(V,{});
    by[1].assign(V,{});
    vector<vector<char>> seen(V,vector<char>(V,0));
    for(int i=0;i<N;++i) {
      int p,l;
      if(!(cin>>p>>l)||p<0||l<0||p>=V||l>=V||seen[p][l])
        throw runtime_error("not distinct original source incidence");
      seen[p][l]=1;
      flag[i]={p,l};
      by[0][p].push_back(i);
      by[1][l].push_back(i);
    }
    int d=int(by[0][0].size());
    if(d<2) throw runtime_error("source degree <2");
    for(int axis=0;axis<2;++axis)for(int p=0;p<V;++p)
      if(int(by[axis][p].size())!=d) throw runtime_error("source factor degree unequal");
    otherPack[0].resize(N);otherPack[1].resize(N);
    for(int axis=0;axis<2;++axis)for(int i=0;i<N;++i) {
      auto z=lab[1-axis][flag[i][1-axis]];
      otherPack[axis][i]=(U(1)<<(4*z[0]))+(U(1)<<(4*z[1]));
    }
    for(int k=0;k<a;++k) forbidden|=(U(13)<<(4*k));
    // 0xD (binary 1101) excludes all nibble patterns except 0000,0010.
  }
};
struct Result {
  U count[6]={};
  U bShapes=0,cShapes=0,bCandidates=0,cCandidates=0;
};
static inline int opposite_type(const array<int,6>& ids) {
  int doubled=0;
  for(int i=0;i<6;++i) {
    int multiplicity=0;
    for(int j=0;j<6;++j) multiplicity+=(ids[i]==ids[j]);
    if(multiplicity>2)return 0;
    if(multiplicity==2) doubled++;
  }
  if(doubled==0)return 1; // all six distinct original opposite factors
  if(doubled==2)return 2; // exactly one repeated twice, four singles
  return 0;               // C and all unaccepted endpoint structures
}
static void count_B(const Model& m,int axis,Result& out) {
  // axis=0: B-left; axis=1: B-right
  auto& labels=m.lab[axis];
  auto& inv=m.inverse[axis];
  auto& by=m.by[axis];
  auto& packed=m.otherPack[axis];
  auto& flags=m.flag;
  for(int p=0;p<m.V;++p) {
    int px=labels[p][0],py=labels[p][1];
    vector<int> v;
    for(int x=0;x<m.a;++x)if(x!=px&&x!=py)v.push_back(x);
    for(size_t i=0;i<v.size();++i)
    for(size_t j=i+1;j<v.size();++j)
    for(size_t k=j+1;k<v.size();++k)
    for(size_t t=k+1;t<v.size();++t) {
      int a=v[i],b=v[j],c=v[k],d=v[t];
      int paths[3][4]={{a,b,c,d},{a,b,d,c},{a,c,b,d}};
      for(auto& q:paths) {
        int p0=inv[q[0]][q[1]];
        int p1=inv[q[1]][q[2]];
        int p2=inv[q[2]][q[3]];
        int p3=inv[q[3]][q[0]];
        if(p0<0||p1<0||p2<0||p3<0)continue;
        ++out.bShapes;
        const auto& F=by[p];const auto& A=by[p0];const auto& B=by[p1];
        const auto& C=by[p2];const auto& D=by[p3];
        for(size_t x=0;x<F.size();++x)
        for(size_t y=x+1;y<F.size();++y) {
          int id0=F[x],id1=F[y];
          U pairMask=packed[id0]+packed[id1];
          int o0=flags[id0][1-axis],o1=flags[id1][1-axis];
          for(int id2:A)for(int id3:B) {
            U m4=pairMask+packed[id2]+packed[id3];
            int o2=flags[id2][1-axis],o3=flags[id3][1-axis];
            for(int id4:C)for(int id5:D) {
              ++out.bCandidates;
              U total=m4+packed[id4]+packed[id5];
              if(total&m.forbidden)continue;
              array<int,6> opp={o0,o1,o2,o3,
                                flags[id4][1-axis],flags[id5][1-axis]};
              int type=opposite_type(opp);
              if(type==1) {
                ++out.count[axis==0?0:1];
              } else if(type==2 && axis==0) {
                int repeated=-1;
                for(int h=0;h<6&&repeated<0;++h)
                  for(int z=h+1;z<6;++z)
                    if(opp[h]==opp[z]){repeated=opp[h];break;}
                if(repeated<0)throw runtime_error("missing B repeated factor");
                int overlap=(o0==repeated)||(o1==repeated);
                ++out.count[overlap?4:5];
              }
            }
          }
        }
      }
    }
  }
}
static void count_C(const Model& m,int axis,Result& out) {
  auto& labels=m.lab[axis];
  auto& by=m.by[axis];
  auto& packed=m.otherPack[axis];
  auto& flags=m.flag;
  struct Choice{U mask;int o0,o1;};
  vector<vector<Choice>> choices(m.V);
  for(int p=0;p<m.V;++p) {
    const auto& F=by[p];
    for(size_t i=0;i<F.size();++i)
    for(size_t j=i+1;j<F.size();++j) {
      int id0=F[i],id1=F[j];
      choices[p].push_back({packed[id0]+packed[id1],
                            flags[id0][1-axis],flags[id1][1-axis]});
    }
  }
  vector<unsigned> labelMask(m.V);
  for(int p=0;p<m.V;++p)
    labelMask[p]=(1U<<labels[p][0])|(1U<<labels[p][1]);
  for(int p=0;p<m.V;++p)
  for(int q=p+1;q<m.V;++q) {
    if(labelMask[p]&labelMask[q])continue;
    for(int r=q+1;r<m.V;++r) {
      if((labelMask[p]|labelMask[q])&labelMask[r])continue;
      ++out.cShapes;
      for(const auto& x:choices[p])
      for(const auto& y:choices[q]) {
        U m4=x.mask+y.mask;
        for(const auto& z:choices[r]) {
          ++out.cCandidates;
          if((m4+z.mask)&m.forbidden)continue;
          int type=opposite_type({x.o0,x.o1,y.o0,y.o1,z.o0,z.o1});
          if(type==1)++out.count[2];
          if(type==2)++out.count[3];
        }
      }
    }
  }
}
int main() {
  try {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    Model model;
    Result res;
    count_B(model,0,res);
    count_B(model,1,res);
    count_C(model,0,res);
    count_C(model,1,res);
    cout<<"COUNTS";
    for(U n:res.count)cout<<" "<<n;
    cout<<"\nSTATS "<<res.bShapes<<" "<<res.cShapes
        <<" "<<res.bCandidates<<" "<<res.cCandidates<<"\n";
    return 0;
  }catch(const exception& e) {
    cerr<<"HYP105_EXACT_SEVEN_FAIL_CLOSED: "<<e.what()<<"\n";
    return 2;
  }
}
