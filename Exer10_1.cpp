#include <stdio.h>

int main ()
{	
	int i,vet[10];
	for (i = 0; i < 10; i++)
	{
		printf("Entre o valor de vet[%d]: ", i);
		scanf("%d", &vet[i]);
	}
	for (i = 9; i >= 0; i--)
		printf("%d\n", vet[i]);
	return(0);
}
