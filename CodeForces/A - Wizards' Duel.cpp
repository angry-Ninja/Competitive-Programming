#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    float l,p,q;
    cin>>l>>p>>q;
    float b=(l*p)/(p+q);
    printf("%.4f",b);
    cout<<endl;
    return 0;
}
