#include <stdio.h>

int nulbit(int a)
{
    int k = 1;
    if ((a & 1) == 0) {
        return k;
    } else {
        k += 1;
        a >> 1;
    }
}

int main()
{
    int a;
    scanf("%d", &a);
    printf("%d\n", nulbit(a));
    return 0;
}

