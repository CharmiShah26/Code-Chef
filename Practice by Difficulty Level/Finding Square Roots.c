#include<stdio.h>
#include<math.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        double n;
        int result;
        scanf("%lf",&n);
        result=(int)sqrt(n);
        printf("%d\n",result);
        t--;
    }
    return 0;
}
