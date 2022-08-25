#include<stdio.h>
#include<unistd.h>

int main(){

    char *bin_path="ls";
    char *arg1="-a";
    char *arg2="-s";

    execlp(bin_path,bin_path,arg1,arg2,NULL);
    return 0;
}