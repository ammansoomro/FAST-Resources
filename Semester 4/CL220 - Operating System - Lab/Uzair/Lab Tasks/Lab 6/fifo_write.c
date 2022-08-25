#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<fcntl.h>
#include<unistd.h>

int main(void) {

	int fd, retval;
	char buffer[] = "Hello!!";
	
	fflush(stdin);
	retval = mkfifo("/tmp/uzair",0777);
	fd = open("/tmp/uzair",O_WRONLY);
	write(fd,buffer,sizeof(buffer));
	close(fd);
	return 0;
}