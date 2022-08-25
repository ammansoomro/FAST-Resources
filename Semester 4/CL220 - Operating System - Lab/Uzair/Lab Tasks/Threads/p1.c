#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>


void *thread(void *vargp){
	
	int i=42;

 //   pthread_exit(i);
	printf("%ld",pthread_self());
}

int main(){
        
    int i;
    pthread_t tid;
    pthread_create(&tid, NULL, thread, NULL);
    pthread_join(tid, NULL);
//    printf("%d\n",i);
	
}
