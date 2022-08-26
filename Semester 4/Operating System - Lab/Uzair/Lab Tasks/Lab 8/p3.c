#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

int main () 
{
    int nthreads, tid, i;
    float a[100], b[100], c[100];

    for (i=0; i < 100; i++)
        a[i] = b[i] = i * 1.0;

    #pragma omp parallel shared(a,b,c,nthreads) private(i,tid) num_threads(10)
    {
        tid = omp_get_thread_num();
        
        if (tid == 0)
        {
            nthreads = omp_get_num_threads();
            printf("Number of threads = %d\n", nthreads);
        }
        
        printf("Thread %d starting...\n",tid);

        #pragma omp for schedule (static,10) //10 here means divide each thread 10 iterations in seq
        
        for (i=0; i<100; i++)
        { 
            c[i] = a[i] + b[i];
            printf("Thread %d: c[%d]= %f\n",tid,i,c[i]);
        }
    }
}
