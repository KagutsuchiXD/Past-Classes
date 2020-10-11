#include <cstdio>
#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <termios.h>

using namespace std;

void usage(void) {
    cout << 
        "\nINSTRUCTIONS:\n"
        "=============\n"
        "press 'w' to call wait()\n"
        "press 'q' to quit\n"
        "press '?' to read these instructions again\n"
        "press the any key to spawn a new zombie\n\n";
}

int main(void) {
	char c;
	pid_t child = -1;

	struct termios oldt, newt;
	tcgetattr(STDIN_FILENO, &oldt);
	newt = oldt;
	newt.c_lflag &= ~(ICANON | ECHO);
	tcsetattr(STDIN_FILENO, TCSANOW, &newt);

	usage();

	while (1) {
        c = getchar();

        switch (c) {
            case 'w':
            case 'q':
                {
                    int count = 0;
                    while ( (child = waitpid(-1, NULL, WNOHANG)) > 0)
                        cout << "Reaped child #" << ++count << " PID: " << child << endl;
                }
                break;
            case '?':
                usage();
                break;
            default:
                child = fork();
                if (child == 0)
                    c = 'q';
                else
                    cout << "Forked a child " << child << endl;
        }
        if (c == 'q')
            break;
	}

	if (child != 0)
			tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

	return 0;
}
