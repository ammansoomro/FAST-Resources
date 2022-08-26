#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void *theThread(void *parm){

    printf("Entered the thread\n");
    return NULL;
}

int main(int argc, char **argv){

    pthread_attr_t attr;
    pthread_t thread;
    int rc;

    printf("Create a default thread attributes object\n");
    pthread_attr_init(&attr);
    printf("Set the detach state thread attribute\n");
    pthread_attr_setdetachstate(&attr,PTHREAD_CREATE_DETACHED);
    printf("Create a thread using the new attributes\n"); pthread_create(&thread, &attr, theThread, NULL);
    printf("Destroy thread attributes object\n"); pthread_attr_destroy(&attr);
    
    rc = pthread_join(thread, NULL);
    printf("Join now fails because the detach state attribute was changed\n pthread_join returns non zerovalue %d",rc);
    printf("Main completed\n");
    return 0;
}