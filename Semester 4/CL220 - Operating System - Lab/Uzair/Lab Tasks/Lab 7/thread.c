#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

void * thread1(){

    while(1){

        printf("Hello!!\n");
    }
}

void * thread2(){

    while(1){

        printf("How are you?\n");
    }
}
int main(){

    int status;
    pthread_t tid1,tid2;
    pthread_create(&tid1,NULL,thread1,NULL);
    pthread_create(&tid2,NULL,thread2,NULL);
    pthread_join(tid1,NULL);
    pthread_join(tid2,NULL);
    return 0;
}