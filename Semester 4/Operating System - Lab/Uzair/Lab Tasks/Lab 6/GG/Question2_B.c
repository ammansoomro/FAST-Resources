#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>

int main(void) {

	char message[20];
	int fd, retval;
	
	retval = mkfifo("/tmp/1118",0777);
	fd = open("/tmp/1118",O_WRONLY);
	
    while(1){
        
        fflush(stdin);
        memset(message, 0, sizeof(message));
        printf("Enter message:");
        gets(message);
        write(fd,message,sizeof(message));
        if(message[0]=='0')
            break;
    }
	close(fd);
	return 0;
}