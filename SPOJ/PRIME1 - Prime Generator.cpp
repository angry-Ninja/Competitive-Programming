#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int prime(long long int n)
{
	if(n<2)
	{
		return 0;
	}
	else
	{   long long int i;
	    
		for( i=2;i<=(long long int)sqrt(n);i++)
		{
			if(n%i==0)
			{
				return 0;
			}
		}
		return 1;
	}
	
}

int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t--)
    {
    	long long int a,b,j;
    	cin>>a>>b;
    	for(j=a;j<=b;j++)
    	{
    		if(prime(j)==1)
    			cout<<j<<endl;
		}
		cout<<endl;
	}
    return 0;
}



