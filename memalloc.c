//#######################################
// ClearRam
// Holt sich so viel Speicher wie in der Kommandozeile angegeben (wenn möglich)
// Erstellt: 20081218 sky
//#######################################
// Updated: 2011 Andriy Yurchuk
//#######################################
// Compilation:
// $ gcc memalloc.c -o memalloc
// Usage:
// $ ./memalloc 512 15
// will allocate 512 MB of memory and keep it allocated for 15 seconds
//#######################################

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

unsigned char *ptr = NULL;
void sigint_handler(int);

int main(int argc, char **argv)
{
    unsigned long meg = 1024 * 1024;
    unsigned long i = 0;
    unsigned int toalloc = 1;
    unsigned int sleeptime = 0;
    unsigned int j = 0;

    if (argc == 2) {
        toalloc = atoi(argv[1]);
    }
    else if (argc == 3) {
        toalloc = atoi(argv[1]);
        sleeptime = atoi(argv[2]);
    }

    signal(SIGINT, sigint_handler);

    for (j = 0; j < toalloc; j++) {
        printf("Trying to allocate %u MB of RAM...", j + 1);
        ptr = (unsigned char *) realloc(ptr, (j + 1) * meg * sizeof(char));
        if (ptr == NULL) {
            printf("failed\n");
            free(ptr);
            return 1;
        }
        ptr[0] = 0;
        for (i = j * meg; i < (j + 1) * meg; i++) {
            ptr[i] = ptr[i - 1] + 1;
        }
        printf("success\r");
    }
    sleep(sleeptime);
    free(ptr);
    ptr = NULL;
    printf("\n");
    return 0;
}

void sigint_handler(int status)
{
    printf("\nCaught SIGINT\n");
    free(ptr);
    exit(1);
}
