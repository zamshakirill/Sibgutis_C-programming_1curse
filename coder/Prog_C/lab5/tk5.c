#include <stdio.h>

#define N 10
int x[N] = {3, 3, 3, 3, 7, 7, 9, 1, 1, 1};

void series(int n[]);
void coef(int n[]);
void unbox(int n[]);

int main()
{
    series(x);
    coef(x);
    unbox(x);
}

void series(int n[]) {

    int num[N] = {0};
    int means[N] = {0};
    
    int k = 1; 
    int check = 0; 

    for (int j = 0; j < N; j++) {
        if (j < 19 && n[j] == n[j + 1]) {
            k += 1;
        } 
        else {
            if (k > 2) {
                num[check] = k;
                means[check] = n[j];
                check += 1;
            }
            k = 1;
        }
    }
    printf("----------------Таблица серий----------------\n");
    for (int i = 0; i < check; i++) {
        printf("Значение: %d; Длина: %d\n", means[i], num[i]);
    }
    printf("-------------Самая длинная серия-------------\n");
    int max = -1;
    for (int i = 0; i < check; i++) {
        if (num[i] > max) {
            max = means[i];
        }
    }
    for (int j = 0; j < N; j++) {
        if (n[j] == max) {
            printf("%d ", max);
        }
    }
    printf("\n");
}

void coef(int n[]) {

    int check = 0;
    int k = 1;

    for (int j = 0; j < N; j++) {
        if (j < (N - 1) && n[j] == n[j + 1]) {
            k += 1;
        } 
        else {
            if (k > 2) {
                check += 1;
            }
            k = 1;
        }
    }
    printf("---------------------------------------------\n");
    printf("Сжалось в %d раз\n", N / check);
}

void unbox(int n[]) {

    int num[N] = {0};
    int means[N] = {0};
    
    int k = 1; 
    int check = 0; 

    for (int j = 0; j < N; j++) {
        if (j < (N - 1) && n[j] == n[j + 1]) {
            k += 1;
        } 
        else {
            if (k > 2) {
                num[check] = k;
                means[check] = n[j];
                check += 1;
            }
            k = 1;
        }
    }
    printf("-------------Обратная распаковка-------------\n");
    int sum = 0;
    int index = 0;
    for (int i = 0; i < check; i++) {
        sum += num[i];
    }
    int unpack[sum];
    for (int i = 0; i < sum; i++) {
        for (int j = 0; j < num[i]; j++) {
            unpack[index] = means[i];
            printf("%d ", unpack[index]);
            index++;
        }
    }
    printf("\n");
    if (unpack == n) {
        printf("Новый массив совпал с исходным\n");
    } else {
        printf("Новый массив не совпадает с исходным\n");
    }
}