#include<stdio.h>
int main()
{
    int x;
    float c_balance,i=0.5,y,y_temp;
    scanf("%d",&x);
    scanf("%f",&y);
    if(x<=y && x%5==0)
    {
        y_temp=y;
        y=y-(i+x);
        if(y<0)
        {
            printf("%0.2f",y_temp);
        }
        else
        {
            printf("%0.2f",y);
        }
    }
    else
    {
        printf("%0.2f",y);
    }
}
