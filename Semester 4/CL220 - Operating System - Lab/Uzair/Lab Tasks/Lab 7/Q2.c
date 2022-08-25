#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>

void *registration(void* particinat){

    printf("Particinat Number:%d-Congrats you have been registered!\n",(int *)particinat);
}

void *announcements(void* particinat){

    printf("Particinat Number:%d-The starts at 9:00 am , 29th of August!\n",(int *)particinat);
}

void *sponsors(void* particinat){

    printf("Particinat Number:%d-Thankyou for sponsoring the event!\n",(int *)particinat);
}

void *queries(void* particinat){

    printf("Particinat Number:%d-Please write down your queries!\n",(int *)particinat);
}

void main(){

    pthread_t thread[4];
    int i,j;

   srand(time(NULL));

    for(i=0;i<100;i++){

        j= rand() % 4 + 1;

        if(j==1){

            pthread_create(&thread[0],NULL,registration,(void *)i);
        }
        else if(j==2){

            pthread_create(&thread[1],NULL,announcements,(void *)i);
        }
        else if(j==3){

            pthread_create(&thread[2],NULL,sponsors,(void *)i);
        }
        else if(j==4){

            pthread_create(&thread[3],NULL,queries,(void *)i);
        }

    }
    pthread_join(thread[0],NULL);
    pthread_join(thread[1],NULL);
    pthread_join(thread[2],NULL);
    pthread_join(thread[3],NULL);
}