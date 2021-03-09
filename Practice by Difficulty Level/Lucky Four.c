#include<stdio.h>
#define MAX 100
int main()
{
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        int n,x,i=0,four=0,arr[MAX];
        scanf("%d",&n);
        while(n!=0)
        {
            x=n%10;
            arr[i]=x;
            n=n/10;
            i++;
        }
        for(int j=i-1;j>-1;j--)
        {
            if(arr[j]==4)
            {
                four+=1;
            }
        }
        printf("%d\n",four);
        t--;
    }
}
