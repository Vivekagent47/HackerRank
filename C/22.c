#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

void sort_by_area(triangle* tr, int n) {
    int i,j,temp;
    double p,*a;
    a = malloc(n*sizeof(double));
    for(i=0;i<n;i++)
    {
       p=(tr[i].a+tr[i].b+tr[i].c)/2.0;
       a[i]=(p*(p-tr[i].a)*(p-tr[i].b)*(p-tr[i].c));
    }
    for(i=0;i<n;i++)
    {    for(j=0;j<n-i;j++)
        {    if(a[j]<a[j-1])
            {    temp=a[j];
                a[j]=a[j-1];
                a[j-1]=temp;
                temp=tr[j].a;
                tr[j].a=tr[j-1].a;
                tr[j-1].a=temp;
                temp=tr[j].b;
                tr[j].b=tr[j-1].b;
                tr[j-1].b=temp;
                temp=tr[j].c;
                tr[j].c=tr[j-1].c;
                tr[j-1].c=temp;
            }
        }
    }
} 

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}