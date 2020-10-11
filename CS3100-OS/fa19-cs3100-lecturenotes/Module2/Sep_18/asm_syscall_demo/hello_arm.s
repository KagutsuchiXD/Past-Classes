/* hello_arm.s: The obligitory "Hello World" program in ARM ASM */

.section .data
hello:
    .ascii      "Hello ARM World!\n"

/* the length of the string @ 'hello' */
.equ len, . - hello


/* Our application's entry point */
.section .text
.globl _start
_start:

    /* This is signature in C of the syscall I want to use
       write(int fd, const void *buf, size_t count) */

    mov     %r7, $4      /* write is syscall #4 */
    mov     %r0, $1      /* fd := STDOUT_FILENO */
    ldr     %r1, =hello  /* buf := msg */
    ldr     %r2, =len    /* count := len */
    swi     $0           /* Raise interrupt #0 to invoke the syscall */

    /* syscall exit(int status) */
    mov     %r7, $1      /* exit is syscall #1 */
    mov     %r0, $0      /* status := 0 */
    swi     $0           /* invoke syscall */
