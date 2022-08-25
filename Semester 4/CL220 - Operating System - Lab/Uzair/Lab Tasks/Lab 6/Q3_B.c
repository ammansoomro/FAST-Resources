#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
  
void main() 
{   
    int Value,i,Result;
 
    key_t key = ftok("key_file",10); 
  
    int shmid = shmget(key,1024,0666|IPC_CREAT); 
   
    int *string = shmat(shmid,(void*)0,0); 
    
    printf("Value in memory %d\n",*string); 
    Value=*string;
    *string='x';
    
    i=1;

    while(1){
        
        sleep(1);

        if(*string=='*'){

            *string=Value*i;
            i++;
        }
        if(i>11){

            *string='a';
            break;
        }
    }
    
    shmdt(string); 
    
    shmctl(shmid,IPC_RMID,NULL); 
     
    return; 
} 