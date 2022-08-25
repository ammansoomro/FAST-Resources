#include<stdio.h>
#include<unistd.h>

int main(){

    char *bin_path="/bin/ls";
    char *args[]={bin_path,"-a","-s",NULL};//Complete path,then a null pointer.
    execv(bin_path,args);//path then complete array
    return 0;
}