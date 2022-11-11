#include <stdio.h>
#include <stdlib.h>

typedef struct noh{
    int chave;
    struct noh *prox;
}TNoh;

typedef TNoh* Hash;

int hash(int mat, int tam){
    return mat % tam;
}

void inicializa(Hash *tab, int m){
    int i;
    for(i = 0; i < m; i++) {
        tab[i] = NULL;
    }
}

TNoh* busca(Hash *tab, int m, int chave){
    int h = hash(chave, m);
    TNoh *p = tab[h];
    while((p) && (p->chave != chave)) {
        p = p->prox;
    }
    return p;
}

TNoh* aloca(int chave){
    TNoh *novo = (TNoh*) malloc (sizeof (TNoh));
    novo->chave = chave;
    novo->prox = NULL;
    return novo;
}

void insere(Hash *tab, int m, int chave){
    int h = hash(chave, m);
    TNoh *p = tab[h];
    TNoh *ant = NULL;
    while((p != NULL)){// && (p->chave != chave)){ 
        ant = p;
        p = p->prox;
    }
    // if(p){ 
    //     return;
    // }
    TNoh *novo = aloca(chave);
    if(!ant) { 
        tab[h] = novo;
    }
    else { 
        ant->prox = novo;
    }
}

void libera(Hash *tab, int m){
    int i;
    for(i = 0; i < m; i++)
        if(tab[i]){
            TNoh *p = tab[i];
            TNoh *q;
            while(p){//percorre a lista liberando cada nó da memória
                q = p;
                p = p->prox;
                free(q);
            }
        }
}


void imprime(Hash *tab, int m){
    for(int i = 0; i < m; i++){
        printf("%d -> ", i);
        if(tab[i]){
            TNoh *p = tab[i];
            while(p){
                printf("%d -> ", p->chave);
                p = p->prox;
            }
            printf("\\\n");
        }
        else
            printf("\\\n");
    }
}

int main(void){
    int casos;
    int n, m;
    
    scanf("%d", &casos);
    
    for (int i = 0; i < casos; i++){
        
        scanf("%d", &m);
        scanf("%d", &n);
        
        if((n < 1) || (m < 1) || (n > 100) || (m > 200))
            continue;
        
        if (i != 0)
            printf("\n");
        
        Hash *tab[m];
        inicializa(tab, m);

        int i, chave;
        for(i = 0; i < n; i++){
            scanf("%d", &chave);
            insere(tab, m, chave);
        }
        imprime(tab, m);
        libera(tab, m);
    }
    
    
    

    return 0;
}
