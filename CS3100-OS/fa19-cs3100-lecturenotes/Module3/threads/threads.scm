#!/usr/bin/csi -s

;; This is an example of a runtime system which provides "green-threads".

;; In order to run this program on your own Raspberry Pi,
;; you will need to run the following commands:
;;
;; $ sudo apt update
;; $ sudo apt install chicken-bin
;;
;; You may run this program via the Chicken Scheme interpreter:
;;
;; $ ./threads.scm
;;
;; If you run this program through the interpreter, you cannot terminate it
;; with Ctrl-C (SIGINT). You'll need to kill it with Ctrl-\ (SIGABRT), which
;; will cause it to dump core.
;;
;; Or, you may compile this into a standalone executable and run that:
;;
;; $ make threads_scm
;; $ ./threads_scm
;;
;; As a standalone executable, it will respond favorably to SIGINT.


(import
  ;; Import the posix library (gives us low-level C-like file I/O functions)
  (chicken file posix)
  (chicken process-context)

  ;; Import Scheme's threading library
  srfi-18)


;; Global variable for referring to our "slow" I/O device
(define *IO-DEV* 
  (if (not (zero? (length (command-line-arguments))))
    (car (command-line-arguments))
    "/dev/sda"))


;; A function which increments the variable 'a' forever
(define (maths i)
  (let loop ((a 0))
    (loop (add1 a))))


;; A function which copies 8k from our slow I/O device to /dev/null
(define *BUFSIZE* 8192)
(define (slowio dev)
  (print "\n\nWasting time with a cutting-edge I/O-Bound algorithm on the slow data source "
         dev ",\n" *BUFSIZE* " bytes at a time.")

  (let loop ((dev dev))
    (let ((buf (make-string *BUFSIZE*)))

      (let ((slow (file-open dev open/rdonly)))
        (file-read slow *BUFSIZE* buf)
        (file-close slow))

      (let ((null (file-open "/dev/null" open/wronly)))
        (file-write null buf *BUFSIZE*)
        (file-close null)))
    (loop dev)))



;; Create a vector (array) of 6 thread objects running the the 'maths' function
(define *THREADS* 6)
(define tmaths 
  (do ((vec (make-vector *THREADS*))
       (i 0 (add1 i)))
    ((= i *THREADS*) vec)
    (vector-set! vec i (make-thread (lambda () (maths i))))
    (thread-start! (vector-ref vec i))
    (print "Spawned maths thread #" i)))


;; Create a thread object running the 'slowio' function
(define tio (make-thread (lambda () (slowio *IO-DEV*))))
(thread-start! tio)
(print "Spawned Slow/IO thread on device " *IO-DEV*)

(print "Press Ctrl-C or Ctrl-\\ to quit")

;; Join the threads...
;; though this won't happen in our program because our threads are running
;; never-ending functions.
(do ((i 0 (add1 i)))
  ((= i *THREADS*))
  (thread-join! (vector-ref tmaths i))
  (print "Joined maths thread #" i))
(thread-join! tio)
(print "Joined Slow I/O thread")
