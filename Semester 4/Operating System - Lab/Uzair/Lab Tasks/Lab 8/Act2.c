#include<omp.h>
#include<stdio.h>
#include <math.h>
#include<stdlib.h>

long double power(long double x,long double i){
    
    long double res=1;

    while (i != 0) {
        res *= x;
        --i;
    }

    return res;
}

int main(){

    long double fact[20], pwr[20],s[20];
    int i,term,tid;

    for(i=0;i<20;i++){

        s[i]=0;
    }

    #pragma omp parallel private(i,tid)
    {
        tid=omp_get_thread_num();

        #pragma omp sections nowait 
        {   
            #pragma omp section
            {
                for(i=0;i<20;i++) 
                {
                    pwr[i] = power(2,i);
                    printf("Thread: %d,  Power, %.2Lf\n",tid,pwr[i]);
                }
            }

            #pragma omp section
            {   
                long double f;
                fact[0]=1.0;
                for(term=1;term<20;term++)
                {
                    f = 1.0;
                    for(i=term;i>0;i--)
                    f = f * i;
                    fact[term] = f;
                    printf("Thread: %d,Fact, %.2Lf\n",tid,fact[term]);
                }
            }
        }
    }

    #pragma omp parallel num_threads(5)
    {
        s[0] = 1;
        #pragma omp for
        for(i=1;i<20;i++)
        {   
            s[i] = s[i] + (pwr[i] / fact[i]);
            printf("Thread: %d, %Lf\n",tid,s[i]);
        }
                   
        #pragma omp for
        for(i=1;i<20;i++)
        {   
            s[0] = s[0] + s[i];
        }
    }
    printf("Answer: %Lf\n",s[0]);
}