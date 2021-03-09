#include<stdio.h>
#define MAX 100
int main()
{
    int t,arr[MAX];
    scanf("%d",&t);
    while(t!=0)
    {
        int n,x,i=0,sum=0;
        scanf("%d",&n);
        while(n!=0)
        {
            x=n%10;//last digit will be extracted
            arr[i]=x;
            i++;
            n=n/10;
        }
        sum=arr[i-1]+arr[0];
        printf("%d\n",sum);
        t--;

    }
}
