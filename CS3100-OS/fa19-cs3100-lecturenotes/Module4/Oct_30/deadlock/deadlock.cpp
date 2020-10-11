// adapted from http://www.bogotobogo.com/cplusplus/C11/9_C11_DeadLock.php
#include <iostream>
#include <mutex>
#include <thread>
#include <mutex>


using namespace std;
const int SIZE = 10;


// Global mutex objects
mutex myMutex0;
mutex myMutex1;

// Acquire Mutex #0, then #1
void shared_cout_thread_even(int i) {
    lock_guard<mutex> m0(myMutex0);
    lock_guard<mutex> m1(myMutex1);
    cout << " " << i << " ";
}


// Acquire Mutex #1, then #0
void shared_cout_thread_odd(int i) {
    lock_guard<mutex> m1(myMutex1);   // the problem is that we acquire these mutexen+'s in the opposite order
    lock_guard<mutex> m0(myMutex0);
    cout << " " << i << " ";
}


void f(int n) {
    for (int i = SIZE*(n-1); i < SIZE*n ; i++) {
        if (n % 2 == 0)
            shared_cout_thread_even(i);
        else
            shared_cout_thread_odd(i);
    }
}

int main() {
    cout << "Will it work, or won't it?\nThere's only one way to find out!\n\n";

    thread t1(f, 1);  // 0-9
    thread t2(f, 2);  // 10-19
    thread t3(f, 3);  // 20-29
    thread t4(f, 4);  // 30-39
    thread t5(f, 5);  // 40-49

    for (int i = 0; i > -SIZE; i--)
        cout << " " << i << " ";

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    t5.join();

    cout << "\n\nLooks like you got lucky... this time\n";

    return 0;
}
