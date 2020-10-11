#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <sys/wait.h>


int main(int argc, char* argv[]) {
    int maxGen = 10;

    if (argc > 1)
        maxGen = std::stoi(argv[1]);

    for (int generation = 1; generation <= maxGen; generation++) {
        std::cout << "Process " << getpid() << " of generation " << generation << " is forking\n";
        fork();
        usleep(500000);
    }

    return 0;
}
