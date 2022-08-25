#include <stdio.h>
#include <pthread.h>
#include <signal.h>
#include <semaphore.h>
#include <unistd.h>

sem_t s;

void *singsong1(void *param)
{
    sem_wait(&s);
    printf("tid had to wait until your signal released me!\n");
}

void handler(int signal)
{
    sem_post(&s); /* Release the Kraken! */
    printf("OK BAAAYE!\n");
}

void *singsong(void *param)
{
    sem_wait(&s);
    printf("t had to wait until your signal released me!\n");
}

int main()
{
    sem_init(&s,0,2);
    signal(SIGINT, handler); // Too simple! See note below
    
    pthread_t tid,t;
    
    pthread_create(&tid, NULL, singsong, NULL);
    pthread_create(&t, NULL, singsong1, NULL);
    pthread_join(tid,NULL);
    pthread_join(t,NULL);
}