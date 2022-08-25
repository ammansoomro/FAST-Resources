#include<stdio.h>
#include<unistd.h>

int main(){

    pid_t ret_val;

    printf("\nThe process id is: %d\n",getpid());

    ret_val=fork();

    if(ret_val==0){

        printf("In Child Process, Process ID: %d\n",getpid());

        char *bin_path="./script.sh";
        char *arg1="10";
        char *arg2="5";

        execlp(bin_path,bin_path,arg1,arg2,NULL);
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