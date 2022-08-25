#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

int i = 42;
void *thread(void *vargp)
{
    printf("%d\n",i);
}

void *thread2(void *vargp)
{
    i = 31;
}
int main()
{   
    
    pthread_t tid, tid2;
    pthread_create(&tid2, NULL, thread2, (void*)&i);
    pthread_create(&tid, NULL, thread, (void*)&i);
    pthread_join(tid, (void**)&i);
    pthread_join(tid2, NULL);
}
