#include<stdio.h>
#include<stdlib.h>
int k=0;
int largest(int arr[],int len)
{
    int larg=arr[0];
    for (int j=1;j<len;j++)
    {
        if(larg<arr[j])
        {
            printf("arr[0]=%d,arr[j]=%d\n",arr[0],arr[j]);
            larg=arr[j];
            k++;
        }
    }
    return larg;
}
int main()
{
    int t,i=0,larg=0;
    scanf("%d",&t);
    int arr[t],s1[t],s2[t];
    while(t!=0)
    {
        int p1,p2,diff=0;
        scanf("%d%d",&p1,&p2);
        //int a1[t],a2[t];
        diff=abs(p1-p2);
        arr[i]=diff;
        printf("arr=%d\n",arr[i]);
        if(p1>p2)
        {
            s1[i]=1;
            s2[i]=0;
        }
        else if(p2>p1)
        {
            s1[i]=0;
            s2[i]=1;
        }
        i++;
        t--;
    }
    /*for(int j=0;j<t;j++)
    {
        printf("arr[%d]=%d\n",j,arr[j]);
    }*/
   /* for (int j=1;j<t;j++)
    {
        if(larg<arr[j])
        {
            printf("arr[0]=%d,arr[j]=%d\n",arr[0],arr[j]);
            larg=arr[j];
            k++;
        }
    }*/
    larg=largest(arr,t);
    if(s1[k]>s2[k])
    {
        printf("1 %d",larg);
    }
    else
    {
        printf("2 %d",larg);
    }
}
