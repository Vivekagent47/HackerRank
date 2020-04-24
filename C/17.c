#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.

int term(int n, int a, int b, int c) {
  //Write your code here.
  if(n==1)
    return(a);
  else if(n==2)
    return(b);
  else if(n==3)
    return(c);
  else
    return(term(n-1,a,b,c)+term(n-2,a,b,c)+term(n-3,a,b,c));
}

int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
      printf("%d", term(n, a, b, c));
    return 0;
}