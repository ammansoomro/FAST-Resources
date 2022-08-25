#include<stdio.h>
#include<unistd.h>

int main(){

    pid_t ret_val;

    printf("\nThe process id is: %d\n",getpid());

    ret_val=fork();

    if(ret_val==0){

        printf("In Child Process, Process ID: %d\n",getpid());
    }
    else if(ret_val>0){

        wait();//To avoid zombie process (defunking to child process)
        printf("In Prent Process, Process ID: %d\n",getpid());
    }   
    else{

        printf("Process creation failure!\n");
    }
    return 0;
}