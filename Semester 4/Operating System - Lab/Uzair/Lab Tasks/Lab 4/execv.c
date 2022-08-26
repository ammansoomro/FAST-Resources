#include<stdio.h>
#include<unistd.h>

int main(){


    printf("\nIn execv.c file!n");
    char *args[]={"./hello",NULL};//Complete path,then a null pointer.
    execv(args[0],args);//path then complete array
    printf("Coming back to execv.c!\n");//will not be executed
    return 0;    
}