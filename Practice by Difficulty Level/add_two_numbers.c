#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    while(n!=0)
    {
        int a=0,b=0;
        scanf("%d%d",&a,&b);
        int sum=0;
        sum=a+b;
        printf("%d\n",sum);
        n--;
    }
}
