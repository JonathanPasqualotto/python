#include <stdio.h>

int ordenaVet(int vet[], int n){
	int i,j, jogadas=0, aux;
	
	for(j=3-1; j>=1; j--)
	{
		for(i=0; i<n; i++)
		{
			if(vet[i]>vet[i+1])
			{
				aux = vet[i];
				vet[i] = vet[i+1];
                vet[i+1] = aux;
                jogadas++;
                
            }
        }
    }
	return jogadas;
}

int main()
{
	int n, i, jog, vet[1000000];
	
    while(1){
        
    
    	scanf("%d", &n);
    	if(n==0){
    	    break;
    	}
    	else{
    	    for(i=0;i<n;i++){
    		scanf("%d", &vet[i]);
    		}
    	}
    	
    	
    	jog = ordenaVet(vet,n);
    	
    	if(jog % 2 == 0){
    		printf("Marcelo\n");
    	}
    	else{
    		printf("Carlos\n");
    	}
	
    }
    
	return 0;
}