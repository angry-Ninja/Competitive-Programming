#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int n,once;
    cin>>n>>once;
    int arr[n]={0};
    int neww[n]={0};
    int neww1[n]={0};
    int maxx=0;
    int pos=0;
    
    for(int i=0;i<n;i++)
    {
    	cin>>arr[i];
	}
	
    for(int i=0;i<n;i++)
    {
    	if(arr[i]>once)
    	{
    		
    		neww[i]=(arr[i])/once;
    		if((arr[i]%once)!=0)
    			neww[i]++;
    		neww1[i]=(arr[i])/once;
    		if ((arr[i]%once)!=0)
    			neww1[i]++;
		}
	}
	
    sort(neww,neww+n);
    
    for(int i=n-1;i>=0;i--)
    {
    	
    	if(neww[i]!=0)
    	{
    		maxx=neww[i];
    		break;
		}
	}
	
	
	for(int i=n-1;i>=0;i--)
    {
    	if(neww1[i]==maxx)
    	{
    		pos=i+1;
    		break;
		}
	}
	
	cout<<pos<<endl;
    return 0;
}
