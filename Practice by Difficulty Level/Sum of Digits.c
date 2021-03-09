#include<stdio.h>
#define MAX 100
int main()
{
    int n;
    scanf("%d",&n);
    while(n!=0)
    {
        int digit=0,x=0,arr[MAX],sum=0;
        /*for(int i=0;i<MAX;i++)
        {
            arr[i]=NULL;
        }*/
        scanf("%d",&digit);
        int i=0;
        while(digit!=0)
        {
            x=digit%10;//last digit will be extracted
            arr[i]=x;
            i++;
            digit=digit/10;
        }
        for(int j=i-1;j>-1;j--)
        {
            sum+=arr[j];
        }
        printf("\n%d\n",sum);
        n--;
    }
    return 0;
}
