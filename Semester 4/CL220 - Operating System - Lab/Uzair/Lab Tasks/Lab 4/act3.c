#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<sys/wait.h>

int main(){

    int pid = fork();

    if( pid == 0 ){
    
        int pid1 = fork();
        wait(NULL);
        
        if( pid1 == 0 ){
                
            int pid2 = fork();
            wait(NULL);

            if( pid2 == 0 ){

                execlp("ps","ps",NULL);
                perror("execl");
            }
            printf("P3 has executed wait is over");
        }
    }
    return 0;
}