#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

    FILE * fp;

    int i = 0;

    fp = fopen("file_arg.txt", "w+");


    for(i = 1; i < argc; i++) {

        fprintf(fp, "%s ", argv[i]);

    }

    fprintf(fp, "\n");

    fclose(fp);

    return(0);

}
