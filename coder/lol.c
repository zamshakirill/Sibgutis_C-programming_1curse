#include <stdio.h>

void rotateC(int *x1, int *y1, int *x2, int *y2);

int main()
{
    int x1, y1, x2, y2;
    rotateC(&x1, &y1, &x2, &y2);

    printf("%d %d %d %d\n", x1, y1, x2, y2);
}

void rotateC(int *x1, int *y1, int *x2, int *y2)
{
    int xlt, ylt, xrb, yrb;
    scanf("%d%d%d%d", &xlt, &ylt, &xrb, &yrb);
    int pxc = (xlt + xrb) / 2;
    int pyc = (ylt + yrb) / 2;
    *x1 = pxc + (yrb - pyc);
    *y1 = pyc - (xlt - pxc);
    *x2 = pxc + (ylt - pyc);
    *y2 = pyc - (xrb - pxc);
}
