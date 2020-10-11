#include <iostream>
#include <fstream>
#include <string>

#include <cstdlib>

using namespace std;

bool isUpper(char c) {
	return (c >= 'A' && c <= 'Z');
}

bool isLower(char c) {
	return (c >= 'a' && c <= 'z');
}

char rotate(char c, int n) {
	if (isLower(c)) {
		if (c + n > 'z')
			return c + n - 26;
		else
			return c + n;
	}
	else if (isUpper(c)) {
		if (c + n > 'Z')
			return c + n - 26;
		else
			return c + n;
	}
	else
		return c;
}

void unscramble(string file, int dist) {
	cout << endl
		<< "=========================" << endl
		<< "Rotating by " << dist << " positions" << endl
		<< "=========================" << endl;

	ifstream secret(file.c_str());

	char c = secret.get();
	while (!secret.eof()) {
		cout << rotate(c, dist); 
		c = secret.get();
	}

	secret.close();
}


int main(int argc, char* argv[]) {
	string filename = "secretMessage.txt"; 
	int rotation = 0;

	if (argc > 2) {
		filename = string(argv[1]);
		rotation = atoi(argv[2]);
		unscramble(filename, rotation);
	}
	else if (argc > 1) {
		rotation = atoi(argv[1]);
		unscramble(filename, rotation);
	}
	else {
		while (rotation <= 26)
			unscramble(filename, rotation++);
	}
}
