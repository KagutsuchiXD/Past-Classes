#include <iostream>
#include <sys/sem.h>


const int SEMAPHORE_KEY		= 1234;
const short ADD_KEY			= 1;
const short WAIT_KEY		= -1;


int main(__attribute__((unused))int argc, __attribute__((unused))char* argv[]) {
	int semId = semget(SEMAPHORE_KEY, 1, 0666 | IPC_CREAT);
    semctl(semId, 0, SETVAL, 1);

	std::cout << "Press enter to take the key";
	std::string input;
	std::getline(std::cin, input, '\n');

	std::cout << "Waiting on the key to enter the critical section...";
	std::cout.flush();

	sembuf buf;

	buf.sem_num = 0;
	buf.sem_flg = 0;
	buf.sem_op = WAIT_KEY;
	semop(semId, &buf, 1);

    /* CRITICAL SECTION */
	std::cout << "We've got the key, now in the CRITICAL SECTION" << std::endl;
	std::cout << "Press enter to return the key" << std::endl;
	std::getline(std::cin, input, '\n');

	buf.sem_op = ADD_KEY;
	semop(semId, &buf, 1);
    /* END OF CRITICAL SECTION */

	std::cout << "Key has been returned" << std::endl;

	return 0;
}
