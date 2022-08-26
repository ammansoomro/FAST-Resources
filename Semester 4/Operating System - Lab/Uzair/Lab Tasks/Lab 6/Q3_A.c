#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void main(){

    int value;

    
    key_t key = ftok("key_file",10); 
  
    
    int shmid = shmget(key,1024,0666|IPC_CREAT); 
   
    int *string =  shmat(shmid,(void*)0,0); 
    
    printf("Enter Value:");
    scanf("%d",&value);
    *string=value;   
    printf("Memory: %d\n",*string);
    while(*string==value);

    while(1){

        sleep(1);

        if(*string=='x'){
                
            printf("Data in Memory: %c\n",(char)*string);
            *string='*';
        }
        else if(*string=='a')
            break;

        else if(*string!='*'){

            printf("%d",*string);
            printf("\n");
            *string='*';
        }     
    }
      
    shmdt(string); 
 
    shmctl(shmid,IPC_RMID,NULL); 
    return; 
} 