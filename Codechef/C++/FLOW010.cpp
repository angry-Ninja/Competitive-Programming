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
    	char ch;
    	cin>>ch;
    	if((ch=='b')||(ch=='B'))
    	{
    		cout<<"BattleShip"<<endl;
		}
		else if((ch=='c')||(ch=='C'))
    	{
    		cout<<"Cruiser"<<endl;
		}
		else if((ch=='d')||(ch=='D'))
    	{
    		cout<<"Destroyer"<<endl;
		}
		else if((ch=='f')||(ch=='F'))
    	{
    		cout<<"Frigate"<<endl;
		}
	}
    return 0;
}
