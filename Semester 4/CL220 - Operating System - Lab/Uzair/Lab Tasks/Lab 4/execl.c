#include<stdio.h>
#include<unistd.h>

int main(){

    char *bin_path="/bin/ls";
    char *arg1="-a";
    char *arg2="-s";

    execl(bin_path,bin_path,arg1,arg2,NULL);
    return 0;
}