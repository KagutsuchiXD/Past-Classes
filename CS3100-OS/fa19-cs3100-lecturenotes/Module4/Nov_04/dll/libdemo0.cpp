#include <iostream>
#include <string>

extern "C" double demo(std::string message) {
	std::cout << "Message is: " << message << std::endl;

	return 1.2345;
}

