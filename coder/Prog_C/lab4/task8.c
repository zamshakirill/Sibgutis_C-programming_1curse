#include <stdio.h>

int nulbit(int n)
{
    for (int i = 1; i < 32; i++) {
        if ((n & 1) == 1) {
            n = n >> 1;
        }
        else {
            return i;
        }
    }
}

int main()
{
    int a;
    scanf("%d", &a);
    printf("%d\n", nulbit(a));
    return 0;
}

