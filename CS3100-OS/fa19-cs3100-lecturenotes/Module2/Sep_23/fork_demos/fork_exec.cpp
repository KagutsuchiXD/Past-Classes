#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <sys/wait.h>
#include <vector>


int main(void) {

    bool quittingTime = false;

    while (!quittingTime) {
        char resp;
        std::cout << "Which command do you want to run, and how to run it?\n"
            "\ta) execl(\"/bin/ls\", \"-l\", \"-a\", \"-F\")\n"
            "\tb) execlp(\"ls\", \"-l\", \"-a\", \"-F\")\n"
            "\tc) execv({\"/bin/ps\", \"-e\", \"-f\", \"-x\", NULL})\n"
            "\td) execvp({\"ps\", \"-e\", \"-f\", \"-x\", NULL}) \n"
            "\tt) re-touch the scruoe code for great justice!\n"
            "\tm) execvp({\"make\", NULL}) \n"
            "\tq) Quit this fine program\n"
            "> ";

        std::cin >> resp;

        switch (resp) {
            pid_t kiddo;

            case 'a':
            case 'A':
                std::cout << "Running 'execl(\"/bin/s\", \"-l\", \"-a\", \"-F\")'\n";
                if ((kiddo = fork()) != 0) {
                    wait(NULL);
                }
                else {
                    int retval = execl("/bin/ls", "ls", "-l", "-a", "-F", NULL);
                    std::cerr << "Something went wrong and execl() returned " << retval << std::endl;
                }
                break;

            case 'b':
            case 'B':
                std::cout << "Running 'execlp(\"ls\", \"-l\", \"-a\", \"-F\")'\n";
                if ((kiddo = fork()) != 0) {
                    wait(NULL);
                }
                else {
                    int retval = execlp("ls", "ls", "-l", "-a", "-F", NULL);
                    std::cerr << "Something went wrong and execlp() returned " << retval << std::endl;
                }
                break;

            case 'c':
            case 'C':
                std::cout << "Running 'execv({\"/bin/ps\", \"-e\", \"-f\", \"-x\", NULL})'\n";
                if ((kiddo = fork()) != 0) {
                    wait(NULL);
                }
                else {
                    char* cmd[] = { (char*)"/bin/ps", (char*)"-e", (char*)"-f", (char*)"-x", (char*)NULL };
                    int retval = execv(cmd[0], cmd);
                    std::cerr << "Something went wrong and execv() returned " << retval << std::endl;
                }
                break;

            case 'd':
            case 'D':
                std::cout << "Running 'execvp({\"ps\", \"-e\", \"-f\", \"-x\", NULL})'\n";
                if ((kiddo = fork()) != 0) {
                    wait(NULL);
                }
                else {
                    char* cmd[] = { (char*)"ps", (char*)"-e", (char*)"-f", (char*)"-x", (char*)NULL };
                    int retval = execvp(cmd[0], cmd);
                    std::cerr << "Something went wrong and execvp() returned " << retval << std::endl;
                }
                break;


            case 'm':
            case 'M':
                std::cout << "Running 'execvp({\"make\", \"fork_exec\", NULL})'\n";
                if ((kiddo = fork()) != 0) {
                    wait(NULL);  // parent process waits here
                    std::cout << "re-execing this process!!!!!\n";
                    execl("./fork_exec", "./fork_exec", NULL);
                    std::cerr << "Failed to exec 'fork_exec' :(\n";
                }
                else {
                    char* cmd[] = { (char*)"make", (char*)"fork_exec", (char*)NULL };
                    int retval = execvp(cmd[0], cmd);
                    std::cerr << "Something went wrong and execvp() returned " << retval << std::endl;
                }
                break;

            case 't':
            case 'T':
                std::cout << "Running 'execvp({\"touch\", \"fork_exec.cpp\", NULL})'\n";
                if ((kiddo = fork()) != 0) {
                    wait(NULL);  // parent process waits here
                }
                else {
                    execlp("touch", "touch", "fork_exec.cpp", NULL);
                    std::cerr << "Failed to touch 'fork_exec.cpp' :(\n";
                }
                break;



            case 'q':
            case 'Q':
                quittingTime = true;
                break;


            default:
                std::cout << "I'm not sure what to make of that. I'll just ask again...\n";
                break;
        }
    }

    return 0;
}
