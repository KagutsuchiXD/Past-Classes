#include <iostream>
#include <pthread.h>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <errno.h>

// A function which increments the variable 'a' forever
void* maths(__attribute__((unused)) void *threadid) {
    int a = 0;
    while (true)
        a++;
    return (void*)NULL;
}



// A function which copies 8k from our slow I/O device to /dev/null
void* slowio(__attribute__((unused)) void* vp_dev) {
    char* dev = (char*)vp_dev;

    std::cout << "\n\nWasting time with a cutting-edge I/O-Bound algorithm on the slow data source "
        << dev << ",\n" << BUFSIZ << " bytes at a time.\n";

    char buffer[BUFSIZ];

    while (true) {
        // open a slow device for read
        FILE *slow = fopen(dev, "r");
        if (slow) {
            // read BUFSIZ bytes from slow device
            fread(buffer, BUFSIZ, sizeof(char), slow);
            // close the slow device
            fclose(slow);

            // open /dev/null for write
            FILE *null = fopen("/dev/null", "w");
            if (null) {
                // write BUFSIZ to null
                fwrite(buffer, BUFSIZ, sizeof(char), null);
                // close null
                fclose(null);
            }
        }
        else {
            std::cerr << "\nFailed to open " << dev << "!!\n";
            return (void*)NULL;
        }
    }

    return (void*)NULL;
}



int main(int argc, char** argv) {
    // variable for referring to our "slow" I/O device
    char* IO_DEV = (char*)"/dev/sda";
    char *device;

    if (argc > 1 )
        device = argv[1];
    else
        device = IO_DEV;


    // Create an array of 6 thread objects running the the 'maths' function
    pthread_t tmaths[6];
    for (int i = 0; i < 6; ++i)
        if (pthread_create(&(tmaths[i]), NULL, maths, NULL)) {
            perror("pthread_create() failed on maths");
            exit(EXIT_FAILURE);
        }
        else {
            std::cout << "Spawned maths thread #" << i << std::endl;
        }


    // Create a thread object running the 'slowio' function
    pthread_t tio;
    if (pthread_create(&tio, NULL, slowio, (void*)device)) {
        perror("pthread_create() failed on slowio");
        exit(EXIT_FAILURE);
    }
    else {
        std::cout << "Spawned Slow I/O thread on device " << device << std::endl;
    }

    std::cout << "Press Ctrl-C to quit\n";

    for (int i = 0; i < 6; ++i) {
        pthread_join(tmaths[i], NULL);
        std::cout << "Joined maths thread #" << i << std::endl;
    }
    pthread_join(tio, NULL);
    std::cout << "Joined Slow I/O thread\n";

    return 0;
}
