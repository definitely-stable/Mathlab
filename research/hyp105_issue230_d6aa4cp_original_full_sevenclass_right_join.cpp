// HYP-105 #230 AA4-CP: exact ORIGINAL six-incidence full 7-GF5 join.
// Exhaustively enumerate RIGHT physical degree-two sixcoordinate shapes
// for SOURCE LINE A/B/C. Expand ONLY TRUE source incidence flags
// (s+1 slots for each distinct real LINE), reject LEFT degree violations
// early and classify exact historic seven-positive original sixflag Q.
// Every six distinct original incidence set appears at most once; all
// accepted ones have right 2regular, hence all are enumerated.
// Scope of THIS 64bit 4-bit nibble-engine: genuine W32 and W34 a<=16.
// No probabilistic independence, no synthetic original Q, no physics-only risk.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using U64=uint64_t;
struct Pattern { array<int,6> lines{}; int right_kind=0; bool connected=false; uint16_t dual=0; };
struct Alt { array<int,2> point{}; U64 mask=0; };
int s,V,a,I;
vector<array<int,2>> f,g,flags,allpairs;
vector<vector<int>> by_line,edge_index,original_flag_id;
vector<int> occupied;
vector<U64> fcode; // BY ORIGINAL POINT FACTOR ID: size V (15/85), NOT physical alphabet a!
U64 ONES=0,TWOS=0,FOURS=0;
array<unsigned long long,7> counts{}; // D6,B-left/A-right,A-left/B-right,C/A,C/B,B/B-overlap,B/B-disjoint
array<unsigned long long,3> patterns{}, visited{};
array<unsigned long long,3> right_pattern_biphysical{};
unsigned long long both_physical_sixcoordinate_Q=0;
unsigned long long candidates=0, pruned=0;
array<int,6> choice_point{},choice_line{};
array<int,6> target_ids{},target_original_lines{};
bool have_target=false,active_target_pattern=false;
unsigned long long target_pattern_seen=0,target_Q_leaf_seen=0,target_Q_physical_seen=0;
int physical_kind(const array<int,6>& labels) {
    array<int,6> ids=labels;sort(ids.begin(),ids.end());
    int multiplicity[6]={},n=0;
    for(int i=0;i<6;){
        int j=i+1;while(j<6 && ids[j]==ids[i])++j;
        if(j-i>2)return -1;
        multiplicity[n++]=j-i;i=j;
    }
    if(n==6)return 0;
    if(n==5 && count(multiplicity,multiplicity+n,2)==1)return 1;
    if(n==3 && count(multiplicity,multiplicity+n,2)==3)return 2;
    return -1;
}
int line_of(int x,int y){
    if(x>y)swap(x,y);
    return occupied[edge_index[x][y]];
}
uint16_t column_dual(const vector<array<int,2>>& images,const array<int,6>& ids){
    array<int,16> first{};first.fill(-1);
    uint16_t m=0;
    for(int i=0;i<6;i++)for(int v:images[ids[i]]){
        int &u=first[v];
        if(u<0)u=i;
        else if(u==i)return 0; // invalid loop flag
        else{int x=u,y=i;if(x>y)swap(x,y);
             int index=0;for(int z=0;z<x;z++)index+=5-z;
             index+=y-x-1;
             m|=(uint16_t(1)<<index);u=-2;
        }
    }
    for(int u=0;u<a;u++)if(first[u]>=0)return 0;
    return m;
}
void classify(const Pattern& pattern) {
    int L=physical_kind(choice_point);
    if(L<0)throw runtime_error("six original flags passed LEFT physical 2factor but source point type not A/B/C");
    int R=pattern.right_kind;
    int tag=-1;
    if(L==0 && R==0){
        if(pattern.connected && column_dual(f,choice_point)==pattern.dual)tag=0;
    }else if(L==1 && R==0)tag=1;
    else if(L==0 && R==1)tag=2;
    else if((L==0 && R==2)||(L==2 && R==0))tag=3;
    else if((L==1 && R==2)||(L==2 && R==1))tag=4;
    else if(L==1 && R==1) {
        array<int,2> left_pos{-1,-1},right_pos{-1,-1};
        for(int i=0;i<6;i++)for(int j=i+1;j<6;j++) {
            if(choice_point[i]==choice_point[j])left_pos={i,j};
            if(choice_line[i]==choice_line[j])right_pos={i,j};
        }
        if(left_pos[0]<0 || right_pos[0]<0)throw runtime_error("B multiplicities lost");
        const int k=(left_pos[0]==right_pos[0]||left_pos[0]==right_pos[1])+
                    (left_pos[1]==right_pos[0]||left_pos[1]==right_pos[1]);
        if(k>1)throw runtime_error("GQ unique original incidence violated by repeated POINT/LINE pair");
        tag=k?5:6;
    }
    if(tag>=0)++counts[tag];
}
void evaluate(const Pattern& pattern,const array<int,6>& selected_points) {
    choice_point=selected_points;
    ++both_physical_sixcoordinate_Q;
    if(have_target){
        array<int,6> ids{};
        for(int i=0;i<6;i++)ids[i]=original_flag_id[choice_point[i]][choice_line[i]];
        sort(ids.begin(),ids.end());
        if(ids==target_ids)++target_Q_physical_seen;
    }
    ++right_pattern_biphysical[pattern.right_kind];
    if(getenv("AA4CP_DUMP_PHYSICAL_Q")){
        array<int,6> ids{};
        for(int i=0;i<6;i++){
            int id=original_flag_id[choice_point[i]][choice_line[i]];
            if(id<0)throw runtime_error("wrong original flag chosen");
            ids[i]=id;
        }
        sort(ids.begin(),ids.end());
        cout<<"PHYSICAL_Q";for(int id:ids)cout<<" "<<id;
        cout<<"\n";
    }
    classify(pattern);
}
void walk_group(const Pattern& pat,const vector<vector<Alt>>& alternatives,
                const vector<vector<int>>& positions,int group,U64 sum){
    bool target_prefix=have_target && active_target_pattern;
    if(target_prefix)for(int k=0;k<group;k++)for(int slot:positions[k]){
        int id=original_flag_id[choice_point[slot]][choice_line[slot]];
        if(!binary_search(target_ids.begin(),target_ids.end(),id))
            target_prefix=false;
    }
    if(group==(int)alternatives.size()){
        ++candidates;
        if(have_target){
            array<int,6> ids{};
            for(int i=0;i<6;i++)ids[i]=original_flag_id[choice_point[i]][choice_line[i]];
            sort(ids.begin(),ids.end());
            if(ids==target_ids)++target_Q_leaf_seen;
        }
        if((sum&~TWOS)==0 && __builtin_popcountll(sum)==6){
            evaluate(pat,choice_point);
        }
        return;
    }
    const auto& ps=positions[group];
    for(const auto& alt:alternatives[group]){
        U64 next=sum+alt.mask;
        bool target_alt=target_prefix;
        if(target_alt)for(size_t j=0;j<positions[group].size();j++){
            int id=original_flag_id[alt.point[j]][choice_line[positions[group][j]]];
            if(!binary_search(target_ids.begin(),target_ids.end(),id))
                target_alt=false;
        }
        bool bad=((next&FOURS) || ((next&ONES)&((next>>1)&ONES)));
        if(target_alt)
            cout<<"TARGET_PREFIX depth "<<group<<" sum "<<sum
                <<" mask "<<alt.mask<<" next "<<next
                <<" rejected "<<int(bad)<<"\n";
        if(bad){++pruned;continue;}
        for(size_t i=0;i<ps.size();++i)choice_point[ps[i]]=alt.point[i];
        walk_group(pat,alternatives,positions,group+1,next);
    }
}
void process_pattern(const Pattern& p){
    ++patterns[p.right_kind];
    vector<vector<Alt>> alternatives;
    vector<vector<int>> positions;
    array<int,6> sorted=p.lines;
    // Input position indexing must stay identical for LEFT and RIGHT dual.
    choice_line=p.lines;
    active_target_pattern=false;
    if(have_target){
        auto target=p.lines;
        sort(target.begin(),target.end());
        if(target==target_original_lines){
            ++target_pattern_seen;
            active_target_pattern=true;
        }
    }
    array<bool,6> done{};
    for(int k=0;k<6;k++){
        if(done[k])continue;
        vector<int> ps;for(int j=k;j<6;j++)if(p.lines[j]==p.lines[k]){done[j]=true;ps.push_back(j);}
        if(ps.size()>2)throw runtime_error("right source LINE factor appears three times");
        vector<Alt> opts;const auto &adj=by_line[p.lines[k]];
        for(int i=0;i<(int)adj.size();i++) {
            for(int j=(ps.size()==2?i+1:(int)adj.size()); j<(ps.size()==2?(int)adj.size():(int)adj.size()+1);j++){
                Alt t{};t.point[0]=adj[i];t.mask=fcode[adj[i]];
                if(ps.size()==2){t.point[1]=adj[j];t.mask+=fcode[adj[j]];}
                opts.push_back(t);
            }
        }
        if(opts.empty())throw runtime_error("empty actual original LINE star");
        alternatives.push_back(move(opts));positions.push_back(move(ps));
    }
    if(have_target){
        auto source_lines=p.lines;sort(source_lines.begin(),source_lines.end());
        if(source_lines==target_original_lines){
            cout<<"TARGET_PATTERN_GROUPS "<<alternatives.size()<<"\n";
            for(size_t k=0;k<positions.size();k++){
                int line=p.lines[positions[k][0]];
                vector<int> want;
                for(int id:target_ids)if(flags[id][1]==line)want.push_back(flags[id][0]);
                sort(want.begin(),want.end());
                unsigned match=0;
                for(const auto& opt:alternatives[k]){
                    vector<int> got;
                    for(size_t i=0;i<positions[k].size();i++)got.push_back(opt.point[i]);
                    sort(got.begin(),got.end());
                    if(got==want)++match;
                }
                cout<<"TARGET_GROUP "<<k<<" LINE "<<line
                    <<" SIZE "<<positions[k].size()
                    <<" MATCH "<<match
                    <<" ALTS "<<alternatives[k].size()<<"\n";
            }
        }
    }
    walk_group(p,alternatives,positions,0,0);
}
vector<array<int,2>> local_edges;
void sixmask(const array<int,6>& v){
    // 70 right original source LINE A: simple C6 or two disjoint triangles
    for(int mask=0;mask<(1<<15);mask++){
        if(__builtin_popcount((unsigned)mask)!=6)continue;
        array<int,6> d{};array<int,6> lines{};
        int n=0;bool valid=true;
        for(int i=0;i<15;i++)if(mask&(1<<i)){
            const auto [x,y]=local_edges[i];d[x]++;d[y]++;
            int q=line_of(v[x],v[y]);
            if(q<0){valid=false;break;}
            lines[n++]=q;
        }
        if(!valid||any_of(d.begin(),d.end(),[](int n){return n!=2;}))continue;
        Pattern pat;pat.lines=lines;pat.right_kind=0;
        // 2regular of six physical coords: connected iff not two triangles
        array<int,6> comp{};int found=0;comp[0]=1;
        bool progress=true;
        while(progress){progress=false;for(int i=0;i<15;i++)if(mask&(1<<i)){
            auto [x,y]=local_edges[i];
            if(comp[x]&&!comp[y]){comp[y]=1;progress=true;}
            if(comp[y]&&!comp[x]){comp[x]=1;progress=true;}
        }}
        pat.connected=all_of(comp.begin(),comp.end(),[](int x){return x==1;});
        if(pat.connected)pat.dual=column_dual(g,pat.lines);
        process_pattern(pat);
    }
    // 45 physical source LINE B: repeat one original LINE twice,
    // remaining four physical coords form one four-cycle (three options).
    for(int rep=0;rep<15;rep++){
        const auto [x,y]=local_edges[rep];
        const int L=line_of(v[x],v[y]);if(L<0)continue;
        array<int,4> rem{};int n=0;
        for(int i=0;i<6;i++)if(i!=x&&i!=y)rem[n++]=i;
        for(int omit=0;omit<3;omit++){
            Pattern pat;pat.right_kind=1;pat.lines[0]=L;pat.lines[1]=L;
            int k=2;bool good=true;
            for(int i=0;i<4;i++)for(int j=i+1;j<4;j++){
                // K4 fourcycle == omit ONE perfect matching among three.
                int match=((i==0&&j==1)||(i==2&&j==3))?0:
                          (((i==0&&j==2)||(i==1&&j==3))?1:2);
                if(match==omit)continue;
                int line=line_of(v[rem[i]],v[rem[j]]);
                if(line<0){good=false;break;}
                pat.lines[k++]=line;
            }
            if(good && k==6)process_pattern(pat);
        }
    }
    // 15 physical source LINE C: three disjoint 2-fold edges.
    for(int b=1;b<6;b++){
        int others[4],n=0;
        for(int j=1;j<6;j++)if(j!=b)others[n++]=j;
        for(int k=1;k<4;k++){
            Pattern pat;pat.right_kind=2;
            int L0=line_of(v[0],v[b]);
            int L1=line_of(v[others[0]],v[others[k]]);
            int x=-1,y=-1;
            for(int j=1;j<4;j++)if(j!=k){
                if(x<0)x=others[j];else y=others[j];
            }
            int L2=line_of(v[x],v[y]);
            if(L0<0||L1<0||L2<0)continue;
            pat.lines={L0,L0,L1,L1,L2,L2};
            process_pattern(pat);
        }
    }
}
void validate(){
    if(a<6 || a>16 || V<=0 || I!=V*(s+1))throw runtime_error("only original GQ W32/W34 packed a<=16");
    occupied.assign(a*(a-1)/2,-1);
    edge_index.assign(a,vector<int>(a,-1));
    int eid=0;
    for(int u=0;u<a;u++)for(int v=u+1;v<a;v++){
        edge_index[u][v]=edge_index[v][u]=eid++;
    }
    by_line.assign(V,{});
    original_flag_id.assign(V,vector<int>(V,-1));
    vector<int> left_occ(eid,-1),right_occ(eid,-1);
    for(int q=0;q<V;q++){
        for(auto [side,img]:array<pair<int,array<int,2>>,2>{{{0,f[q]},{1,g[q]}}}){
            auto [u,v]=img;if(u<0||u>=a||v<0||v>=a||u>=v)throw runtime_error("invalid original source physical pair");
            int ix=edge_index[u][v];auto &used=side==0?left_occ:right_occ;
            if(used[ix]>=0)throw runtime_error("not globally injected original POINT/LINE map");
            used[ix]=q;
        }
    }
    occupied=right_occ;
    vector<int> left_degree(V),right_degree(V);
    vector<vector<char>> seen(V,vector<char>(V));
    for(int id=0;id<I;id++){
        auto [p,l]=flags[id];
        if(p<0||p>=V||l<0||l>=V || seen[p][l])throw runtime_error("repeated/invalid TRUE original incidence ID");
        seen[p][l]=true;original_flag_id[p][l]=id;
        ++left_degree[p];++right_degree[l];by_line[l].push_back(p);
    }
    if(const char* raw=getenv("AA4CP_TARGET_Q")){
        stringstream ss(raw);string item;int n=0;
        while(getline(ss,item,',')){
            if(n>=6)throw runtime_error("target Q more than six original source flags");
            int id=stoi(item);
            if(id<0||id>=I)throw runtime_error("target original source incidence ID out of range");
            target_ids[n++]=id;
        }
        if(n!=6)throw runtime_error("target Q must use exactly six real original incidence IDs");
        sort(target_ids.begin(),target_ids.end());
        for(int i=0;i<6;i++)target_original_lines[i]=flags[target_ids[i]][1];
        sort(target_original_lines.begin(),target_original_lines.end());
        have_target=true;
    }
    for(int q=0;q<V;q++)if(left_degree[q]!=s+1||right_degree[q]!=s+1)
        throw runtime_error("not exact true original GQ degree");
    for(int v=0;v<a;v++){ONES|=U64(1)<<(4*v);TWOS|=U64(2)<<(4*v);FOURS|=U64(4)<<(4*v);}
    fcode.assign(V,0);
    if(fcode.size()!=size_t(V))throw runtime_error("original POINT factor-mask array must have V entries");
    for(int q=0;q<V;q++) fcode.at(q)=(U64(1)<<(4*f[q][0]))+(U64(1)<<(4*f[q][1]));
    if(have_target){
        U64 total=0;
        for(int id:target_ids)total+=fcode[flags[id][0]];
        cout<<"TARGET_RAW_FULL_LEFT "<<total<<" VALID "<<int(
            (total&~TWOS)==0 && __builtin_popcountll(total)==6)<<"\n";
    }
    for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)local_edges.push_back({i,j});
}
void read_model(const string& path){
    ifstream in(path);
    if(!(in>>s>>V>>a>>I))throw runtime_error("missing original model header");
    f.resize(V);g.resize(V);flags.resize(I);
    for(auto& e:f)if(!(in>>e[0]>>e[1]))throw runtime_error("original f missing");
    for(auto& e:g)if(!(in>>e[0]>>e[1]))throw runtime_error("original g missing");
    for(auto& e:flags)if(!(in>>e[0]>>e[1]))throw runtime_error("original genuine source incidence missing");
}
int main(int argc,char**argv){
    try{
        if(argc!=2)throw runtime_error("usage exact_join <complete_original_gq_model.txt>");
        read_model(argv[1]);validate();
        array<int,6> chosen{};unsigned long long panels=0;
        auto rec=[&](auto&&self,int start,int depth)->void{
            if(depth==6){++panels;sixmask(chosen);return;}
            for(int c=start;c<=a-(6-depth);c++){
                chosen[depth]=c;self(self,c+1,depth+1);
            }
        };
        rec(rec,0,0);
        static const char* tags[]={"D6","B-left/A-right","A-left/B-right",
             "C/A","C/B","B/B-overlap","B/B-disjoint"};
        static const long long weights[]={5643,45600,45600,43320,49050,51750,45010};
        U64 S=0,W=0;for(int i=0;i<7;i++){S+=counts[i];W+=counts[i]*weights[i];}
        cout<<"SCHEMA AA4CP1\n";
        cout<<"s "<<s<<"\nV "<<V<<"\na "<<a<<"\n";
        cout<<"physical_sixpalettes "<<panels<<"\n";
        for(int i=0;i<3;i++)cout<<"source_LINE_pattern_"<<char('A'+i)<<" "<<patterns[i]<<"\n";
        cout<<"source_Q_right_deg2_tested "<<candidates<<"\n";
        cout<<"BOTH_left_and_right_physical_sixcoordinate_Q "<<both_physical_sixcoordinate_Q<<"\n";
        for(int i=0;i<3;i++)cout<<"BOTH_physical_right_source_"<<char('A'+i)
                               <<" "<<right_pattern_biphysical[i]<<"\n";
        cout<<"early_right_to_left_physical_degree_prunes "<<pruned<<"\n";
        for(int i=0;i<7;i++)cout<<tags[i]<<" "<<counts[i]<<"\n";
        cout<<"S_unweighted "<<S<<"\nW_weighted "<<W<<"\n";
        if(have_target){cout<<"TARGET_right_pattern_seen "<<target_pattern_seen<<"\n";
            cout<<"TARGET_six_incidence_combination_seen "<<target_Q_leaf_seen<<"\n";
            cout<<"TARGET_left_and_right_physical_seen "<<target_Q_physical_seen<<"\n";}
        cout<<"all_h_lower_proved 0\n";
        return 0;
    }catch(const exception&e){cerr<<"AA4CP FAIL CLOSED: "<<e.what()<<"\n";return 2;}
}
