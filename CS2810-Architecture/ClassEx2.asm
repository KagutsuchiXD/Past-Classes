	.data
A:	.space 64
X:	.word 15
Y:	.word 8



	.text
	la	$t0,A
	lw	$t1,X
	lw	$t2,Y
	addi	$zero,$t2,4
	add	$t3,$t1,$t2
	sub	$t4,$t2,$t1
	sub	$t1,$t1,$t1
	sw	$t4,8($t0)
	