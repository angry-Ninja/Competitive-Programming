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
    	int grade=0;
    	double h,c,t=0;
    	cin>>h>>c>>t;
    	if((h>50)&& (c<0.7)&&(t>5600))
    	{
    		grade=10;
		}
		else if((h>50)&& (c<0.7))
		{
			grade=9;
		}
		else if((h>50)&&(t>5600))
		{
			grade=7;
		}
		else if((c<0.7)&&(t>5600))
    	{
    		grade=8;
		}
		else if((h>50)||(c<0.7)||(t>5600))
		{
			grade=6;
		}
		else
		{
		    grade=5;	
		}
		cout<<grade<<endl;
	}
    return 0;
}
