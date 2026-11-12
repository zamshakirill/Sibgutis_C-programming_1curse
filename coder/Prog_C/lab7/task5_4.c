#include <stdio.h>
#include <string.h>

#define MAX_WORDS 100
#define MAX_LEN 50

int comp(char *word1, char *word2) {
    return strcmp(word1, word2);
}

void swap(char *word1, char *word2) {
    char t[MAX_LEN];
    strcpy(t, word1);
    strcpy(word1, word2);
    strcpy(word2, t);
}

void print_words(char words[MAX_WORDS][MAX_LEN], int count) {
    for (int i = 0; i < count; i++) {
        printf("%s\n", words[i]);
    }
}

int main() {
    char text[] = "orange apple banana kiwi";
    int count_word = 0;
    char words[MAX_WORDS][MAX_LEN];

    char *token = strtok(text, " ");
    while (token != NULL && count_word < MAX_WORDS) {
        swap(words[count_word], token);
        count_word++;
        token = strtok(NULL, " ");
    }
    for (int i = 0; i < count_word - 1; i++) {
        for (int j = 0; j < count_word - 1; j++) {
            if (comp(words[j], words[j + 1]) > 0) {
                swap(words[j], words[j + 1]);
            }
        }
    }
    printf("words in alhabet:\n");
    print_words(words, count_word);
    printf("kolichestvo slov: %d\n", count_word);
    return 0;
}
