#include <stdio.h>
#include <semaphore.h>
#include <sys/types.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>


sem_t lock;
int con = 0; //global variable that will be shared in paralel threads
int sum = 0;

void* thread1(void *ptr)
{
	int *arr = (int*) ptr;
	while(1)
	{
		sem_wait(&lock);
		//sleep(5);
		if(con >=25) {
			sem_post(&lock);
			return NULL;
		}
		sum = sum + arr[con++];
		sem_post(&lock);
		return NULL;
	}
}

void* thread2(void *ptr)
{
	int *arr = (int*) ptr;
	while(1)
	{
		sem_wait(&lock);
		//sleep();
		if(con >=25) {
			sem_post(&lock);
			return NULL;
		}
		sum = sum + arr[con++];
		sem_post(&lock);	
	}
	return NULL;
}

void* thread3(void *ptr)
{
	int *arr = (int*) ptr;
	while(1)
	{
		sem_wait(&lock);
		//sleep(1);
		if(con >=25) {
			sem_post(&lock);
			return NULL;
		}
		sum = sum + arr[con++];
		sem_post(&lock);
		return NULL;
	}
}

void* thread4(void *ptr)
{
	int *arr = (int*) ptr;
	while(1)
	{
		sem_wait(&lock);
		//sleep(1);
		if(con >=25) {
			sem_post(&lock);
			return NULL;
		}
		sum = sum + arr[con++];
		sem_post(&lock);
		return NULL;
	}
}

int main()
{
	clock_t initiate, end;
	double total_time;
	int array [25] = {34,2324,123,314,4325,126,47,238,559,211,1642,1233,2314,34,154,1234,11,67,2877,5671,567,22343,6546,297};
	sem_init(&lock, 0, 1);
	pthread_t sum1, sum2, sum3, sum4;
    
        sum=0;
        initiate = clock();
	
            pthread_create(&sum1, 0,  thread1, (void *) array);
            pthread_create(&sum2, 0, thread2, (void *) array);
            pthread_create(&sum3, 0, thread3, (void *) array);
            pthread_create(&sum4, 0, thread4, (void *) array);
            pthread_join(sum1,NULL);
            pthread_join(sum2,NULL);
            pthread_join(sum3,NULL);
            pthread_join(sum4,NULL);
            printf("Sum of the array is: %d\n", sum);

        end = clock();
        total_time = ((double) (end - initiate));
        printf("Time taken for 4 threads: %.2f\n", total_time);

    return 0;
}