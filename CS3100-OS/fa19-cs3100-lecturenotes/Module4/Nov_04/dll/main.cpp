#include <iostream>
#include <cstdlib>
#include <string>
#include <dlfcn.h>


int main(void) {

    char again;

    do { 
        std::string lib;
        void* handle = nullptr;
        do {
            std::cout << "Which library do you want to load?> ";
            std::cin >> lib;

            if (std::cin.eof())
                return 0;

            handle = dlopen(lib.c_str(), RTLD_LAZY);
            if (!handle) {
                std::cout << "Couldn't open the shared library, error: " << dlerror() << std::endl;
            }
        } while (!handle);



        double (*msgFunc)(std::string) = (double(*)(std::string))dlsym(handle, "demo");
        char* error;
        if ((error = dlerror()) != NULL) {
            std::cout << "Error: " << error << std::endl;
            exit(1);
        }

        std::cout << "What do you have to say for yourself?> ";
        std::string message;
        std::getline(std::cin, message); // discard the \n at the end of the last read
        std::getline(std::cin, message);

        double value = (*msgFunc)(message);
        std::cout << "Returned Value: " << value << std::endl;

        dlclose(handle);

        std::cout << "Go again? [y/n] ";
        std::cin >> again;
        std::getline(std::cin, message); // discard the \n at the end of the last read
    } while ((again & 0x59) == 'Y');     // Case insensitive comparison in ASCII

    return 0;
}
