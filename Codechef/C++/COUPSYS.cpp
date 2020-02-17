#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t>0)
    {
    	t--;
    	int n;
    	cin>>n;
    	int level1=0;
        int	city1=9999999;
    	int city2=9999999;
    	int city3=9999999;
    	int level2=0;
    	int level3=0;
    	for(int i=0;i<n;i++)
    	{
    		int a,b,c;
    		cin>>a>>b>>c;
    		if (b==1)
    			{
				if (c>level1)
    			{
    			    	level1=c;
    			    	city1=a;
				}
				else if(c==level1)
				{
					city1=min(city1,a);
				}
				}
			if(b==2)
    			{
				if(c>level2)
    			{
    			    	level2=c;
    			    	city2=a;
				}
				else if(c==level2)
				{
					city2=min(city2,a);
				}
				}
				if(b==3)
    			{
				if(c>level3)
    			{
    			    	level3=c;
    			    	city3=a;
				}
				else if(c==level3)
				{
					city3=min(city3,a);
				}
				}
		}
		cout<<level1<<" "<<city1<<"\n"<<level2<<" "<<city2<<"\n"<<level3<<" "<<city3<<"\n";
		
	}
    return 0;
}

