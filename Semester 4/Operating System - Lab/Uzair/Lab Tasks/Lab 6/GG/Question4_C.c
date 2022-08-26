#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<stdio.h>
#include<stdlib.h>

void main(){

    int Num1,Num2,n;
 
    key_t Val1 = 0000;
    key_t Val2 = 0007;
 
    int shmid1 = shmget(Val1,1024,0666|IPC_CREAT);
    int shmid2 = shmget(Val2,1024,0666|IPC_CREAT);
     
    int *string1 =  shmat(shmid1,(void*)0,0); 
    int *string2 =  shmat(shmid2,(void*)0,0); 

    printf("Enter the value:");
    scanf("%d",&n);
    
    printf("%d ",*string1);
    printf("%d ",*string2);

    while(n){

        Num1=*string1;
        Num2=*string2; 
        printf("%d ",Num1+Num2);
        *string1=*string2;
        *string2=Num1+Num2;
        n--;
    }

    *string1='Num2';
    *string2='Num2';
    //detach from shared memory  
    shmdt(string1); 
    shmdt(string2);

    // destroy the shared memory 
    shmctl(shmid1,IPC_RMID,NULL); 
    shmctl(shmid2,IPC_RMID,NULL);
    return; 
}