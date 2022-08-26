#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>
#include<unistd.h>
#include<string.h>

int main(void) {

	int fd, retval;
	char message[20];
	
	fd = open("/tmp/1118",O_RDONLY);

    while(1){

        fflush(stdin);
        memset(message, 0, sizeof(message));
        read(fd, message, sizeof(message));
        if(message[0]=='0')
            break;

        printf("Message from sender:");
        puts(message);
    }	
	close(fd);
	return 0;
}