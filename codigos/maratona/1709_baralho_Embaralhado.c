#include <stdio.h>

int p;

int embaralhar(int a, int c){
  int b; 
  if (2 * a <= p)
    b = 2 * a;
  else
    b = 2 * a - (p + 1);
  if (b == 1)
    return c;
  else
    return embaralhar(b, c + 1);
}

int main(){
 
    scanf("%i",&p);
    printf("%i\n",embaralhar(1, 1));

    return 0;
}