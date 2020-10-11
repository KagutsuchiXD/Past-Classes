#!/usr/bin/csi -ss

(import
  (chicken process-context)
  (chicken sort)
  (chicken string))

(define inexact exact->inexact)

;; Given a sequence of CPU Burst times, create a list of (Pn . Burst time) pairs
(define (bursts->procs . bursts)
  (let loop ((i 1) (bursts bursts))
    (if (null? bursts)
      bursts
      (let ((P-name (string->symbol (conc "P" i))))
        (cons (cons P-name (car bursts)) (loop (add1 i) (cdr bursts)))))))


;; Given a sequence of processes, compute the average delay under a First-Come,
;; First-Served scheduler
(define (fcfs-avg-delay procs)
  (let ((n (length procs)))
    (if (zero? n)
        0
        (let loop ((so-far 0) (procs procs))
          (if (null? (cdr procs))
              (inexact (/ so-far n))
              (loop (+ so-far (* (cdar procs) (length (cdr procs)))) (cdr procs)))))))


;; Compare two procs based on their CPU burst time
(define (proc-<? a b)
  (< (cdr a) (cdr b)))

;; What order would the Shortest-Job-First scheduler take these procs?
(define (sjf-order . bursts)
  (sort (apply bursts->procs bursts) proc-<?))

;; What's the avg. delay of these procs under SJF?
(define (sjf-avg-delay procs)
  (fcfs-avg-delay (sort procs proc-<?)))


(define (compare-schedulers . bursts)
  (let ((procs (apply bursts->procs bursts)))
    (print "FCFS avg delay: " (fcfs-avg-delay procs))
    (print "SJF avg delay:  " (sjf-avg-delay procs))))


;; Compute maximum theoretical speedup per Amdahl's law,
;; or the max speedup given a number of cores
(define (amdahl p #!optional cores)
  (/ (+ (- 1.0 p)
        (if cores
            (/ p cores)
            0))))

(define (help)
  (display #<<USAGE
(compare-schedulers b0 b1 ...) ;  Compare outcome of FCFS and SJF scheduling
(bursts->procs bursts)         ;  Convert list of burst times into procs
(sjf-order b0 b1 ...)          ;  In what order would SJF schedule these bursts?


USAGE
))

(define (main args)
  (apply compare-schedulers (map string->number args)))
