#include<stdio.h>
#include<string.h>
int main()
{
	char *str = "xueyong";
	char s[]="xueyong";
	printf("%d,%d\n",sizeof(str),sizeof(s));
	printf("%d,%d\n",strlen(str),strlen(s));
	printf("%s,%s\n",str,s);
	return 0;
}