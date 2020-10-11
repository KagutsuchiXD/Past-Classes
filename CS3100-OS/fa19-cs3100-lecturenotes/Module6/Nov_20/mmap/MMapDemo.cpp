#include <iostream>
#include <cstring>
#include <sys/mman.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>


int main (int argc, char** argv) {
    char* file = (char*)"TestFile.txt";
    int fdFile = open(file, O_RDWR);
    int length = lseek(fdFile, 0, SEEK_END);

    char* fileArray;

    if (argc > 1) {
        fileArray = static_cast<char*>(mmap(0, length, PROT_READ|PROT_WRITE, MAP_PRIVATE, fdFile, 0));
        std::cout << "Mapping " << file << " in PRIVATE mode\n";
    }
    else {
        fileArray = static_cast<char*>(mmap(0, length, PROT_READ|PROT_WRITE, MAP_SHARED, fdFile, 0));
        std::cout << "Mapping " << file << " in SHARED mode\n";
    }

    // File handle may now be closed
    close(fdFile);

    std::cout << "Before:\n" << fileArray << std::endl;

    // modify the file's data as though it were an array
    strncpy(fileArray,      "Hi Mom", 6);
    strncpy(fileArray + 35, "hack", 4);

    std::cout << "After:\n" << fileArray << "\nCheck the contents of " << file << ", then Press enter to continue\n";
    std::string input;
    std::getline(std::cin, input);

    // unmap the file from memory
    munmap(fileArray, length);

    return 0;
}
