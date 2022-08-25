#include<math.h>
#include<pthread.h>
#include<stdlib.h>

long double x,fact[150], pwr[150],s[1];
int i,term;
void *Power(void *temp) {
    
    int k;
    for(k=0;k<150;k++) {
        pwr[k] = pow(x,k);
        //printf("%.2Lf\n",pwr[k]);
    }
    return pwr;
}
void *Fact(void *temp) {
    
    long double f;
    int j;
    fact[0] = 1.0;

    for(term=1;term<150;term++) {
        f = 1.0;
        for(j=term;j>0;j--)
        f = f * j;
        fact[term] = f;
        //printf("%.2Lf\n",fact[term]);
        }
    return fact;
}

void *Exp(void *temp) {
    int t;
    s[0] = 0;
    
    for(t=0;t<150;t++)
        s[0] = s[0] + (pwr[t] / fact[t]);
    
    return s;
}
int main(void) {
    
    pthread_t thread1,thread2,thread3;
    long double **sum;
    printf("Exponential [PROMPT] Enter the value of x (between 0 to 100) (for calculating exp(x)):");
    scanf("%Lf",&x);
    printf("\nExponential [INFO] Threads creating.....\n");
    pthread_create(&thread1,NULL,Power,NULL); //calling power function
    pthread_create(&thread2,NULL,Fact, NULL); //calling factorial function
    printf("Exponential [INFO] Threads created\n");
    pthread_join(thread1,NULL);
    pthread_join(thread2,NULL);
    printf("Exponential [INFO] Master thread and terminated threads are joining\n");
    printf("Exponential [INFO] Result collected in Master thread\n");
    pthread_create(&thread3,NULL,Exp,NULL);
    pthread_join(thread3,sum);
    printf("\neXPONENTIAL [INFO] Value of exp(%.2Lf) is : %Lf\n\n",x,s[0]);
    exit(1);
}