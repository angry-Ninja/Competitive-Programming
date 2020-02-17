#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

int digits(long long int x ) { 
    return ( (bool) x * (int) log10( abs( x ) ) + 1 );
}


int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t--)
    {
    
    	long long int b,a;
    	cin>>a>>b;
    	int lena=digits(a);
    	int last_digit=a%10;
    	int exp=4;
    	if (b%4!=0)
    	{
    		exp=b%4;
		}
    	int idigit=pow(last_digit,exp);
    	int res=idigit%10;
        if((a==0 && b==0) || b==0 )
        {
        	cout<<1<<endl;
		}
		else
		{
			cout<<res<<endl;
		}
    	
		
	}
    return 0;
}
