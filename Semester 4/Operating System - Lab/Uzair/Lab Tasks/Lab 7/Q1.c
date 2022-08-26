#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

void * thread1(){

    int i;

    for(i=1;i<=1000;i++){

        printf("%d\n",i*5);
    }
    pthread_exit(NULL);
}

void * thread2(){

    int j;

    for(j=1;j<=1000;j++){

        printf("%d\n",j*6);
    }
    pthread_exit(NULL);
}

void * thread3(){

    int k;

    for(k=1;k<=1000;k++){

        printf("%d\n",k*7);
    }
    pthread_exit(NULL);
}

void * thread4(){

    int l;

    for(l=1;l<=1000;l++){

        printf("%d\n",l*8);
    }
    pthread_exit(NULL);
}

int main(){

    pthread_t td1,td2,td3,td4;
    pthread_create(&td1,NULL,thread1,NULL);
    pthread_create(&td2,NULL,thread2,NULL);
    pthread_create(&td3,NULL,thread3,NULL);
    pthread_create(&td4,NULL,thread4,NULL);
    pthread_join(td1,NULL); 
    pthread_join(td2,NULL);
    pthread_join(td3,NULL);
    pthread_join(td4,NULL);
}