#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function   
    printf("%d\n",(*a)+(*b));
    if(*a<*b)
        printf("%d",(-1)*((*a)-(*b)));
    else 
        printf("%d",(*a)-(*b));
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa,pb);

    return 0;
}
