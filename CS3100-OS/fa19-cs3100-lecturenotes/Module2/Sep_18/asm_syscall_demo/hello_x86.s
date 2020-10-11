/* hello_x86.s: The obligitory "Hello World" program in x86 ASM */

.section .data
hello:
    .ascii      "Hello x86 World!\n"

/* the length of the string @ 'hello' */
.equ len, . - hello


/* Our application's entry point */
.section .text
.globl _start
_start:

    /* This is signature in C of the syscall I want to use
       write(int fd, const void *buf, size_t count) */

    mov     $4, %eax     /* write is syscall #4 */
    movl    $1, %ebx     /* fd := STDOUT_FILENO */
    movl    $hello, %ecx /* buf := hello */
    movl    $len, %edx   /* count := len */
    int     $0x80        /* Raise interrupt #128 to invoke the syscall */

    /* syscall exit(int status) */
    movl    $1, %eax     /* exit is syscall #1 */
    movl    $0, %ebx     /* status := 0 */
    int     $0x80        /* invoke syscall */
