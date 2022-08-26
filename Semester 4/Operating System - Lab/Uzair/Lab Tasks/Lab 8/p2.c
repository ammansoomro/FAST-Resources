#include<omp.h>
#include<stdio.h>

int main(){

    int i,nthreads,tid;

    float a[10],b[10],c[10],d[10];

    for(i=0;i<10;i++){

        a[i]=i+1;
        b[i]=i+2;

    }
    #pragma omp parallel shared(a,b,c,d,nthreads) private(i,tid)//i is private for for loop
    {

        tid=omp_get_thread_num();
        if(tid==0){

            nthreads=omp_get_num_threads();
            printf("Number of threads = %d\n",nthreads);
        }

        #pragma omp sections nowait //nowait is used to rum each section on diff thread
        {
            #pragma omp section
            {
                printf("Thread %d in section 1.\n",tid);
                for(i=0;i<10;i++)
                {

                    c[i]=a[i]+b[i];
                    printf("Thread %d, c[%d]= %f\n",tid,i,c[i]);
                }
            }
            
            #pragma omp section
            {
                printf("Thread %d in section 2.\n",tid);
                for(i=0;i<10;i++)
                {

                    d[i]=a[i]*b[i];
                    printf("Thread %d, d[%d]= %f\n",tid,i,d[i]);
                }
            }
        }
    }
}