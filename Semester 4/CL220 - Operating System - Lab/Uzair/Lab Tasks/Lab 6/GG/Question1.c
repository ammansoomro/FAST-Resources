#include<stdio.h>
#include<unistd.h>

int main(){

    int pipefd[2];
    int pid;
    char buffer[20]={""};

    pipe(pipefd);
    pid=fork();

    if(pid == 0){

        fflush(stdin);
        printf("Write a message to parent\n");
        gets(buffer);
        write(pipefd[1],buffer, sizeof(buffer));
    }
    else if(pid > 0){

        wait();
        fflush(stdin);
        printf("Message from Child: \n");
        read(pipefd[0],buffer,sizeof(buffer));
        puts(buffer);
    }
    else{

        printf("Error in creating child process\n");
    }
    return 0;
}