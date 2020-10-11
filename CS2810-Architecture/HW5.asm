.data
	array:	.word 5,3,2,4,1,7,6
.text
bubblesort:

 la   $a0,array  #address of the array into $a0
 li      $s0, 1      # boolean swap = false.  0 --> false, 1 --> true
 li      $t1, 0      # j = 0;
 li      $t2, 0      # i = 0;
 li      $s1, 7     # array length
 loop:
     beqz    $s0, print   # exit if swap = false
     li      $s0, 0          # swap = false;
     addiu   $t1, $t1, 1  # j++;
     move   $t2, $0      # i = 0;
     subu    $s2, $s1, $t1  # s2 = length - j
     forLoop:
         bge     $t2, $s2, exitForLoop   # if i>=s2, exit
         lw      $a1, 0($a0)         # a0 = array[i]
         lw      $a2, 4($a0)         # a1 = array[i+1]
         ble     $a1, $a2, update        # if array[i]<=array[i+1] skip
         sw      $a2, 0($a0)         # a[i+1] = a[i]
         sw      $a1, 4($a0)         # a[i] = a[i+1]
         li      $s0, 1                 # swap = true;
         update:
         addiu   $t2, $t2, 1         # i++
         sll     $t3, $t2, 2         # t3 = i*4
         addu    $a0, $a0, $t3        # point to next element -->
         la   $a0,array  #address of the array into $a0
         j       forLoop
     exitForLoop:
         j   loop
 print:
 	beq 	$t0, 28, exit
 	lw	$t6, array($t0)
 	addi	$t0, $t0, 4
 	
 	li	$v0, 1
 	move	$a3, $t6
 	syscall
 exit:
     jr      $ra