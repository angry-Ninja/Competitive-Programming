#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t--)
    {
    	long long int hcf,lcm,a,b;
    	cin>>a>>b;
    	hcf=__gcd(a,b);
    	lcm=(a*b)/hcf;
    	cout<<hcf<<" "<<lcm<<"\n";
    }
    return 0;
}
