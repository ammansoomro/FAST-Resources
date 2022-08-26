#include<stdio.h>
#include<unistd.h>

int main(){

    int pid = fork();

    if( pid == 0 ){
    
        int pid1 = fork();
        
        if( pid1 == 0 ){
                
            int pid2 = fork();
            int id=getpid();

            if( pid2 == 0 ){

                int pid3 = fork();

                if( pid3 == 0 ){

                    printf("My Grand Parent's ID: %d\n",id);
                }
                if(pid3 >0){

                    wait();
                }
                printf("Wicked Son./n");
                sleep(7);
                char *bin_path="date";
                execlp(bin_path,bin_path,NULL);
            }
            if(pid2 >0){

                wait();
            }
            printf("Simple Son./n");
            char *bin_path="ifconfig";
            execlp(bin_path,bin_path,NULL);
        }
        if(pid1 >0){

            wait();
        }
        printf("Wise Son.\n");
        sleep(1);
    }
    if(pid >0){

        wait();
    }

   return 0;
}