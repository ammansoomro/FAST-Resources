#include<omp.h>
#include<stdio.h>

int main(){

    int nthreads,tid;

    #pragma omp parallel private(tid,nthreads) num_threads(10)
    {

        tid=omp_get_thread_num();

        printf("Thread = %d\n",tid);

        if(tid==0){

            nthreads=omp_get_num_threads();
            printf("The number of threads are: %d\n",nthreads);

        }
    }
}