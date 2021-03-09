#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        int n;
        scanf("%d",&n);
        if(n<10){
            printf("Thanks for helping Chef!\n");
        }
        else{
            printf("-1\n");
        }
        t--;
    }
}
