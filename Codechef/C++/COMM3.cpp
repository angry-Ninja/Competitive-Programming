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
    	int max;
    	cin>>max;
    	int x1,x2,x3,y1,y2,y3;
    	cin>>x1>>y1;
    	cin>>x2>>y2;
    	cin>>x3>>y3;
    	float d1=sqrt(pow((x1-x2),2)+pow((y1-y2),2));
    	float d2=sqrt(pow((x2-x3),2)+pow((y2-y3),2));
    	float d3=sqrt(pow((x1-x3),2)+pow((y1-y3),2));
    	
    	if(((d1<=max)&&(d2<=max)||(d3<=max)))
    	{
    		if((d1<=max) || ((d3<=max)&&(d2<=max))) 
    		{
    			cout<<"yes"<<"\n";
			}
			else
			{
				cout<<"no"<<"\n";
			}
		}
		else
		{
				cout<<"no"<<"\n";
		}
	}
    
    return 0;
}

