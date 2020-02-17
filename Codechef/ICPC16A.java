import java.util.*;
class ram
{
   public static void main(String[] args)
   {
       Scanner sc=new Scanner(System.in);
       int n=sc.nextInt();
       for(int i=0;i<n;i++)
       {
          int j=0;
         int arr[]=new int[4];
         for(j=0;j<4;j++)
          {
             arr[j]=sc.nextInt();
          } 
          if(arr[0]==arr[2])
          {
              if(arr[1]==arr[3])
               {
                  System.out.println("sad");}
              else if(arr[1]>arr[3])
                  {
                  System.out.println("down");
                  }
              else
                {
                System.out.println("up");
                  }
           } 
          else if(arr[1]==arr[3])
          {
              if(arr[0]==arr[2]){
                  System.out.println("sad");}
              else if(arr[0]>arr[2]){
                  System.out.println("left");}
              else{
                System.out.println("right");}
           } 
          else
           {
             System.out.println("sad");
           }
        }
   }
}
