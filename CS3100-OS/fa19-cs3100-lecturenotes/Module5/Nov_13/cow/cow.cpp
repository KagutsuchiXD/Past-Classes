// Demonstration of Copy-on-Write behavior between a parent & child process

#include <iostream>
#include <iomanip>
#include <chrono>
#include <error.h>
#include <errno.h>
#include <unistd.h>
#include <sys/wait.h>

// Try to tweak this number such that the child proc doesn't crash due to out-of-memory (OOM)
const int HOW_BIG = 90000000;


void timeTrial(double *big_array, double v) {

    // modify our array
    auto modify_s = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < HOW_BIG; ++i) {
        big_array[i] = v;
    }
    auto modify_e = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> modify_duration = modify_e - modify_s;

    std::cout << "MODIFY: It took " << modify_duration.count() << "s to set our array to " << v << "\n";

    // read our array
    double total = 0.0;
    auto read_s = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < HOW_BIG; ++i) {
        total += big_array[i]; // this addition most likely accounts for the extra time this loop takes
    }
    auto read_e = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> read_duration = read_e - read_s;
    std::cout << "READ: It took " << read_duration.count() << "s\n\n";
}

int main(void) {
    std::cout << std::setprecision(8);
    // how long does it take to create our array in the 1st place?
    auto start = std::chrono::high_resolution_clock::now();
    double *big_array = new double[HOW_BIG]; 
    auto new_end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> new_duration = new_end - start;
    std::cout << "creating a new array of double[" << HOW_BIG << "] takes " << new_duration.count() << "s\n";

    // warm up
    timeTrial(big_array, 1.0);
    timeTrial(big_array, 2.0);
    timeTrial(big_array, 3.0);
    timeTrial(big_array, 4.0);

    switch (fork()) {
        case -1:
            error(1, errno, "fork() failed");
            break;

        default:
            // Parent process
            wait(NULL);
            std::cout << "Back in the parent process again\n";
            timeTrial(big_array, 1.0);
            timeTrial(big_array, 2.0);
            timeTrial(big_array, 3.0);
            timeTrial(big_array, 4.0);
            break;

        case 0:
            // Child process
            std::cout << "In the child process now\n";
            timeTrial(big_array, 1.0);
            timeTrial(big_array, 2.0);
            timeTrial(big_array, 3.0);
            timeTrial(big_array, 4.0);
            exit(0);
    }
}
