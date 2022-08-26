#include <unistd.h>
#include <sys/types.h> 
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <semaphore.h> 

sem_t mutex;
int counter;//shared

void handler (void *ptr) {
    
    int x = *((int*)ptr);
    printf("sem [INFO] Thread %d Waiting to enter in critical region. \n", x);
    sem_wait(&mutex);
    //Critical Region Starts
    printf("sem [INFO] Thread %d Enters in Critical Region. \n", x);
    printf("sem [INFO] Thread %d Value of Counter is %d.\n",x,counter);
    printf("sem [INFO] Thread %d Increamenting The Value of counter\n",x);
    counter++;
    printf("sem [INFO] Thread %d New value of counter is: %d\n",x, counter);
    printf("sem [INFO] Thread %d Exiting Critical Region.\n", x);
    //Critical Region Ends
    sem_post(&mutex);
    pthread_exit(0);
}

int main(){

    int i[2] = {0, 1};
    pthread_t thread_a, thread_b;
    counter = 0;
    sem_init(&mutex,0,1);

    pthread_create(&thread_a, 0, (void *) &handler, (void *) &i[0]);
    pthread_create(&thread_b, 0, (void *) &handler, (void *) &i[1]);
    pthread_join(thread_a,NULL);
    pthread_join(thread_b,NULL);
    sem_destroy(&mutex);
    return 0;
}

