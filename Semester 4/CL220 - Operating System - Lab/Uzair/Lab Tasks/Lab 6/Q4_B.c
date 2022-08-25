#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void main(){

    int number;

    key_t Val2 = 0007;
  
    int shmid = shmget(Val2,1024,0666|IPC_CREAT); 
   
    int *string =  shmat(shmid,(void*)0,0); 
    
    *string=1;   

    while(*string!='b');
  
    shmdt(string); 
    
    shmctl(shmid,IPC_RMID,NULL); 
   
    return; 
}