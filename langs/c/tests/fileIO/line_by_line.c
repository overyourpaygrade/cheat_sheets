#include <stdio.h>
#include <stdlib.h>

//http://stackoverflow.com/questions/3501338/c-read-file-line-by-line

int main(void)
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("/etc/motd", "r");

    if (fp == NULL)

        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        //printf("Retrieved line of length %zu :\n", read);
        printf("%s", line);
    }

    fclose(fp);

    if (line)

        free(line);

    exit(EXIT_SUCCESS);
}
