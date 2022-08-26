#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

void *thread(void *vargp){

	int *ptr = (int*)vargp;
	//printf("%d",ptr);
	pthread_exit((void*)*ptr);
}

void *thread2(void *vargp){

	int *ptr = (int*)vargp;
	pthread_exit((void*)31);
}

int main(){

	int i = 42;
	pthread_t tid, tid2;
	pthread_create(&tid, NULL, thread, (void*)&i);
	pthread_create(&tid2, NULL, thread2, (void*)&i);
	pthread_join(tid, (void**)&i);
	printf("%d",i);
	pthread_join(tid2, (void**)&i);
	printf("%d",i);
}
