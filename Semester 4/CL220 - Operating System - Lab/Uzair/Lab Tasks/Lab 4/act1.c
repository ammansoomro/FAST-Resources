//activity1
#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<unistd.h>
#include<sys/types.h>

int main(){

    int pid = fork();
    int i;
    if( pid > 0 ){

        //wait(NULL);
        sleep(10);

        for(i=1;i<=10;i++){

            if(i%2==0)
                printf("Even num:%d \n",i);
        }
        printf("Parent Ends \n");
    }

    

    else if( pid == 0 ){

        printf("Parent ID: %d \n",getppid());

        for(i=1;i<=10;i++){

            if(i%2!=0)
                printf("Odd num:%d \n",i);
        }
    }
    else {

        printf("Unsuccessful Child Process Creation.");
        exit(1);
    }
}