#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// проверяем занята ли клетка с индексом idx змейкой
int is_on_snake(const int *snake, int lenght, int idx) {
    for (int i = 0; i < lenght; i++) {
        if (snake[i] == idx) {
            return 1;
        }
    }
    return 0;
}

// генерация еды в случайной свободной клетке
int spawn_food(int rows, int cols, const int *snake, int lenght) {
    int total_cells = rows * cols;
    int food_idx;
    do {
        food_idx = rand() % total_cells;
    } while (is_on_snake(snake, lenght, food_idx));
    return food_idx;
}

// процесс игры
void draw_frame(char *canvas, int rows, int cols,
     const int *snake, int length, int food_idx, int score, int delay) {
    int total_cells = rows * cols;

    for (int i = 0; i < total_cells; i++) {
        canvas[i] = ' ';
    }

    if (food_idx >= 0 && food_idx < total_cells) {
        canvas[food_idx] = '*';
    }

    for (int i = 0; i < length - 1; i++) {
        int idx = snake[i];
        if (idx >= 0 && idx < total_cells) {
            canvas[idx] = 'o';
        }
    }

    int head_idx = snake[length - 1];
    if (head_idx >= 0 && head_idx < total_cells) {
        canvas[head_idx] = '#';
    }

    // создание игрового поля
    printf("+");
    for (int x = 0; x < cols; x++) {
        printf("-");
    }
    printf("+\n");
    for (int y = 0; y < rows; y++) {
        printf("|");
        for (int x = 0; x < cols; x++) {
            printf("%c", canvas[y * cols + x]);
        }
        printf("|\n");
    }
    printf("+");
    for (int x = 0; x < cols; x++) {
        printf("-");
    }
    printf("+\n");

    //печатаем счет после каждого кадра
    printf("Score: %d | Speed delay: %d ms\n", score, delay);
    printf("Commands (w/a/s/d — moving, q — exit): ");
}

int step_snake(int **snake_ptr, int *length, int rows, int cols, int dx, int dy, int *food_idx, int *score, int *delay) {
    int *snake = *snake_ptr;
    int len = *length;

    int head_idx = snake[len - 1]; 
    int head_x = head_idx % cols;
    int head_y = head_idx / cols;

    int new_x = head_x + dx;
    int new_y = head_y + dy;

    //проверка столкновения со стеной
    if (new_x < 0 || new_x >= cols || new_y < 0 || new_y >= rows) {
        return 0;
    }

    int new_head_idx = new_y * cols + new_x;
    int ate_food = (new_head_idx == *food_idx);

    int chek_start = ate_food ? 0 : 1;
    for (int i = chek_start; i < len; i++) {
        if (snake[i] == new_head_idx) {
            return 0;
        }
    }

    //Обновляем змейку
    if (ate_food) {
        int new_len = len + 1;
        int *resized = realloc(snake, (size_t)new_len * sizeof(int));
        if (!resized) {
            perror("Error realloc at update snake");
            return -1;
        }
        snake = resized;
        *snake_ptr = resized;
        
        snake[new_len - 1] = new_head_idx;
        *length = new_len;

        *score += 10;
        if (*delay > 50) {
            *delay -= 10;
        }
        *food_idx = spawn_food(rows, cols, snake, *length);
    } else {
        for (int i = 0; i < len - 1; i++) {
            snake[i] = snake[i + 1];
        }
        snake[len - 1] = new_head_idx;
     }
    return 1;
}

int main () {
    srand((unsigned int)time(NULL));

    int rows, cols;
    int length = 4;
    if (scanf("%d %d", &rows, &cols) != 2 || rows < length || cols < length) {
        fprintf(stderr, "Incorrect field dimensions (need to rows >= 5 и cols >= 6).\n");
        return 1;
    }

    // выделяем память под массив и строим его
    char *canvas = malloc((size_t)(rows * cols) * sizeof (char));
    if (!canvas) {
        perror("error allocating memory for a field");
        return 1;
    }

    // строим начальную змейку и выделяем под нее память 
    int *snake = malloc((size_t)length * sizeof(int));
    if (!snake) {
        perror("Error allocating memory for the snake");
        free(canvas);
        return 1;
    }

    // положение змейки и ее начальное заполнение
    int start_y = rows / 2;
    int start_x = cols / 2 - 1;
    for (int i = 0; i < length;  i++) {
        int x = start_x + i;
        snake[i] = start_y * cols + x;
    }
    
    int food_idx = spawn_food(rows, cols, snake, length);
    int score = 0;
    int delay = 200;

    printf("Initialization complete!\n");
    printf("Do you want to start the game(Y/N)?\n");
    char ans;
    if (scanf(" %c", &ans) != 1 || ans == 'N' || ans == 'n') {
        printf("Good luck!");
        free(snake);
        free(canvas);
        return 0;
    }

    int dx = 1;
    int dy = 0;
    int game_over = 0;
    while (!game_over) {
        draw_frame(canvas, rows, cols, snake, length, food_idx, score, delay);
        char cmd;
        if (scanf(" %c", &cmd) != 1) {
            break;
        }
        if ((cmd == 'w' || cmd == 'W') && dy != 1) {
            dx = 0;
            dy = -1;
        } else if ((cmd == 's' || cmd == 'S') && dy != -1) {
            dx = 0;
            dy = 1;
        } else if ((cmd == 'a' || cmd == 'A') && dx != 1) {
            dx = -1;
            dy = 0;
        } else if ((cmd == 'd' || cmd == 'D') && dx != -1) {
            dx = 1;
            dy = 0;
        } else if (cmd == 'q' || cmd == 'Q') {
            break;
        }

        int status = step_snake(&snake, &length, rows, cols, dx, dy, &food_idx, &score, &delay);
        if (status == 0) {
            game_over = 1;
        } else if (status < 0) {
            game_over = 1;
            fprintf(stderr, "Игра прервана из-за ошибки или заполнения поля.\n");
        } 
    }

    printf("\nGame Over! Итоговый счет: %d, длина змейки: %d\n", score, length);

    free(snake);
    free(canvas);
    return 0;
}
