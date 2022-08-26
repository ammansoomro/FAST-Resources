#include<stdio.h>
#include<unistd.h>

int main(void) {

	int pipefd[2];
	int pid;
	char buffer[15];
	pipe(pipefd);
	pid = fork();

	if(pid > 0) {

		fflush(stdin);
		printf("unamed_pipe [INFO] Parent Process\n");
		write(pipefd[1],"Hellow Mr.Linux",15);
	}
	else if(pid == 0) {

		fflush(stdin);
		printf("unamed_pipe [INFO] Child Process\n");
		read(pipefd[0], buffer, sizeof(buffer));
		write(1,buffer, sizeof(buffer));
		printf("\n");	
	}
	else {
		printf("unamed_pipe [ERROR] Error in creating child process\n");	
	}

	if(pid > 0)
		wait();
	return 0;
}
	