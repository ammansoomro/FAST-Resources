#include<omp.h>
#include<stdio.h>
#include<stdio.h>
#define MAX 5

// reduction
// void main()
// {
//     double ave=0.0, A[MAX]={2,1,3,4,5}; int i;
    
//     #pragma omp parallel for reduction(+:ave)
//     for (i=0;i< MAX; i++)
//     {
//         ave += A[i];
//         printf(" A[i]= %f  average %f with thread %d \n",A[i],ave,omp_get_thread_num());
//     }
//     ave = ave/MAX;
//     printf("final average %f \n",ave);
// }

//priority 
// void main(){
    
//     omp_set_num_threads(10);
//     #pragma omp parallel  num_threads(5)
//     {
//         int ID =omp_get_thread_num();
//         printf(" hello(%d) ", ID);
//         printf(" world(%d) \n", ID);
//     }
// }

//sync
float consume(float b, float r){
        
    return b+r;

}

void main()
{

    float res=231.2;
    #pragma omp parallel
    {
        float B=1.9; int i, id, nthrds;
        id = omp_get_thread_num();
        
        nthrds = omp_get_num_threads();
        
        for(i=id;i<nthrds;i++){

            #pragma omp critical
            printf(":%f\n",consume (B, res));
        }
    }
}
