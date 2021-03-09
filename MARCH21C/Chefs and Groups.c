#include<stdio.h>
#include<string.h>
#define MAX 100000
int main()
{
    int t;
    scanf("%d",&t);
    while(t!=0)
    {
        char input[MAX];
        long long int count=0,group=0;
        int flag=0;
        scanf("%s",input);
        count=strlen(input);
        for(int i=0;i<count;i++)
        {
            //printf("%c:input \n",input[i]);
            if(input[i]=='1' && flag==0)
            {
                group+=1;
                flag=1;
            }
            if(input[i]=='0')
            {
                flag=0;
            }
           // printf("g:%lld, f:%d\n",group,flag);

        }
        printf("%lld\n",group);
        t--;
    }

}
