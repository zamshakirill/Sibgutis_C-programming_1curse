#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int N;
    int min = -32768;
    int max = 32767;
    srand(time(NULL));
    scanf("%d", &N);
    int mat[N * 2];
    for (int i = 0; i < N * 2; i++) {
        mat[i] = min + rand() % (max - min + 1);
        }

    int count = 0;
    for (int j = 0; j < N * 2; j += 2) {
        printf("s[%d]= %d + j * (%d)\n", count, mat[j], mat[j + 1]);
        count += 1;
        }

    int E = 0;
    for (int k = 0; k < N * 2; k += 2) {
        E += (mat[k] * mat[k] + mat[k + 1] * mat[k + 1]);
    }
    printf("E = %d\n", E);

    int maxim = -32769;
    int index = -1;
    for (int l = 0; l < N * 2; l += 2) {
        if (mat[l] > maxim) {
            maxim = mat[l];
            index = l / 2;
        }
    }
    printf("Максимальная реальная часть %d, его индекс %d\n", maxim, index);
    return 0;
}
