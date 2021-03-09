#include<stdio.h>
#define MAX 100
int main()
{
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        int n,x,i=0,arr[MAX];
        scanf("%d",&n);
        while(n%10==0)
            {
                n=n/10;
            }
        while(n!=0)
        {
            x=n%10;
            arr[i]=x;
            n=n/10;
            i++;
        }
        for(int j=0;j<i;j++)
        {
            printf("%d",arr[j]);
        }
        printf("\n");
        t--;
    }
}
/*#include <stdio.h>
int main()
{
int n;
scanf("%d",&n);
for(int i=0;i<n;i++) //2301
   {
        long int n, string=0, rem;
        scanf("%ld", &n);
        while(n!=0)
              {
                 rem=n%10;//0
                 string=string*10+rem;//10
                 n=n/10;//230
              }
        printf("%ld\n",string);
    }
return 0;
}*/
