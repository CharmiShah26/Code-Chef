#include<stdio.h>
int main()
{
    int n;//test cases
    scanf("%d",&n);
    while(n!=0)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        int rem=0;
        rem=a%b;
        printf("%d\n",rem);
        n--;
        a=b=0;
    }
}
