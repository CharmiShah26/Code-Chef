#include<stdio.h>
int main()
{
    int n,k,total=0;
    scanf("%d%d",&n,&k);
    while(n!=0)
    {
        int x=0;
        scanf("%d",&x);
        if(x%k==0)
        {
            total+=1;
        }
        n--;
    }
    printf("\n%d",total);
    return 0;
}

