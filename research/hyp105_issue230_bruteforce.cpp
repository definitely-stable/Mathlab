// Independent definition-level scan of all C(45,6) original sixsets.
// No physical template generator and no permanent computation.
#include <array>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int L[15][3]={{0,1,2},{0,7,8},{0,9,10},{1,3,5},{1,4,6},{2,11,14},{2,12,13},{3,7,11},{3,9,13},{4,7,12},{4,9,14},{5,8,14},{5,10,12},{6,8,13},{6,10,11}};
const int F[15]={13,4,2,14,0,11,1,7,10,6,9,5,12,3,8};
const int G[15]={12,9,11,4,1,6,0,13,5,14,3,7,2,10,8};
int pa[15],pb[15],ep[45],el[45];
long long totals[7]={0}, mass[15]={0},ba[15]={0},ab[15]={0};
long long evaluated=0,left_candidates=0,dual_mass=0;
int profile(const int count[15]) {
    int ones=0,twos=0;
    for(int i=0;i<15;i++) {if(count[i]==1)ones++;else if(count[i]==2)twos++;else if(count[i]>2)return -1;}
    if(ones==6)return 0;
    if(ones==4&&twos==1)return 1;
    if(twos==3&&ones==0)return 2;
    return -1;
}
void check(const array<int,6>&ids) {
    evaluated++;
    int cp[15]={0},cl[15]={0},dx[6]={0},dy[6]={0};
    unsigned xm[6]={0},ym[6]={0};
    for(int i=0;i<6;i++) {
        int p=ep[ids[i]],l=el[ids[i]],x=F[p],y=G[l];
        cp[p]++;cl[l]++;
        dx[pa[x]]++;dx[pb[x]]++;dy[pa[y]]++;dy[pb[y]]++;
        xm[pa[x]]|=1u<<i;xm[pb[x]]|=1u<<i;
        ym[pa[y]]|=1u<<i;ym[pb[y]]|=1u<<i;
    }
    bool left=true,right=true;
    for(int i=0;i<6;i++){left &= dx[i]==2;right &= dy[i]==2;}
    int pl=profile(cp),pr=profile(cl),anchor_p=-1,anchor_l=-1;
    if(pl==1)for(int i=0;i<15;i++)if(cp[i]==2)anchor_p=i;
    if(pr==1)for(int i=0;i<15;i++)if(cl[i]==2)anchor_l=i;
    if(left)left_candidates++;
    if(left&&pl==1&&pr==0)mass[anchor_p]++;
    if(right&&pr==1&&pl==0)dual_mass++;
    if(!left||!right)return;
    if(pl==1&&pr==0){totals[1]++;ba[anchor_p]++;return;}
    if(pl==0&&pr==1){totals[2]++;ab[anchor_l]++;return;}
    if((pl==2&&pr==0)||(pl==0&&pr==2)){totals[3]++;return;}
    if((pl==2&&pr==1)||(pl==1&&pr==2)){totals[4]++;return;}
    if(pl==1&&pr==1){
        bool shared=false;
        for(int i:ids)if(ep[i]==anchor_p&&el[i]==anchor_l)shared=true;
        totals[shared?5:6]++;return;
    }
    if(pl==0&&pr==0){
        array<unsigned,6>x,y;
        for(int i=0;i<6;i++){x[i]=xm[i];y[i]=ym[i];}
        sort(x.begin(),x.end());sort(y.begin(),y.end());
        if(x!=y||adjacent_find(x.begin(),x.end())!=x.end())return;
        unsigned seen=1,last=0;
        while(last!=seen){last=seen;for(unsigned edge:x)if(edge&seen)seen|=edge;}
        if(seen==63)totals[0]++;
    }
}
void choose(array<int,6>&ids,int depth,int start){
    if(depth==6){check(ids);return;}
    for(int j=start;j<=45-(6-depth);j++){ids[depth]=j;choose(ids,depth+1,j+1);}
}
int main(){
    int z=0;for(int a=0;a<6;a++)for(int b=a+1;b<6;b++){pa[z]=a;pb[z++]=b;}
    z=0;for(int l=0;l<15;l++)for(int p:L[l]){ep[z]=p;el[z++]=l;}
    array<int,6>ids;choose(ids,0,0);
    cout<<"original_sixsets "<<evaluated<<" left_candidates "<<left_candidates<<" source_mass ";
    long long m=0,s=0;for(auto v:mass)m+=v;cout<<m<<" dual_source_mass "<<dual_mass<<"\nseven_vector";
    for(auto v:totals){cout<<" "<<v;s+=v;}cout<<"\nS "<<s<<"\nanchor_table p M_p A_p B_l\n";
    for(int i=0;i<15;i++)cout<<i<<" "<<mass[i]<<" "<<ba[i]<<" "<<ab[i]<<"\n";
    const long long expected[7]={0,44,21,0,0,2,1};
    bool ok=evaluated==8145060&&left_candidates==62370&&m==6098&&dual_mass==4740;
    for(int i=0;i<7;i++)ok &=totals[i]==expected[i];
    return ok?0:1;
}
