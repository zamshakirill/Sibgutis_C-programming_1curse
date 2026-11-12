#include <stdio.h>

double determ(int N, double matrix[N][N]) {
    if (N == 1) {
        return matrix[0][0];
    }
    if (N == 2) {
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    }
    double det = 0.0;
    double sub_matrix[N-1][N-1];

    for (int i = 0; i < N; i++) {
        int mn_row_ix = 0;
        for (int row = 1; row < N; row++) {
            int mn_col_ix = 0;
            for (int col = 0; col < N; col++) {
                if (col == i) {
                    continue;
                }
                sub_matrix[mn_row_ix][mn_col_ix] = matrix[row][col];
                mn_col_ix++;
            }
            mn_row_ix++;
        }
        double sign;
        if (i % 2 == 0) {
            sign = 1.0;
        } else {
            sign = -1.0;
        }
        det += sign * matrix[0][i] * determ(N - 1, sub_matrix);
    }
    return det;
}

int main() {
    int N;
    printf("Write matrix size (NxN): ");
    if (scanf("%d", &N) != 1 || N <= 0) {
        printf("Error!\n");
        return 1;
    }
    double matrix[N][N];
    double const_term[N];

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("Write coeff X%d (row %d, col %d): ", j + 1, i + 1, j + 1);
            scanf("%lf", &matrix[i][j]);
        }
        printf("Write constant term %d equation: ", i + 1);
        scanf("%lf", &const_term[i]);
        printf("\n");
    }
    printf("\nCheck the entered system:\n");
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%0.2f ", matrix[i][j]);
        }
        printf("| %0.2f\n", const_term[i]);
    }
    double main_det = determ(N, matrix);
    printf("Determination: %0.2f\n", main_det);
    if (main_det == 0) {
        printf("It is not possible to apply Cramer's rule\n");
        return 0;
    }
    for (int i = 0; i < N; i++) {
        double term_matrix[N][N];
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (col == i) {
                    term_matrix[row][col] = const_term[row];
                    continue;
                }
                term_matrix[row][col] = matrix[row][col];
            }
        }
        printf("X%d = %0.2f\n", i + 1, determ(N, term_matrix) / main_det);
    }
    return 0;
}