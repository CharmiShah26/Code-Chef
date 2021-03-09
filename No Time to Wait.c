#include<stdio.h>
int main()
{
    int n,h,x,ans=0;
    scanf("%d%d%d",&n,&h,&x);
    while(n!=0)
    {
        int i=0;
        scanf("%d",&i);
        if(x+i==h)
        {
            ans+=1;
        }
        n--;
    }
    if(ans>0)
    {
        printf("YES\n");
    }
    else{
        printf("NO\n");
    }
}
