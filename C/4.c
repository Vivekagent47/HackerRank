#include <stdio.h>

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(int x,int y,int z,int w)
{
    int c;
    c=(x>y?(x>z?(x>w?x:w):z):(y>z?(y>w?y:w):z));
    return(c);
}