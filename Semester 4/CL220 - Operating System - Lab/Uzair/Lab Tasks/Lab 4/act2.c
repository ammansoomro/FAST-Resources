#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

int main(){

    execl("/bin/ls","ls",(char*)0);
    return 0;
}