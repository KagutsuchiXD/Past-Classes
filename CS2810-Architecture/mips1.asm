.data

.text
	
	li 	$t1,0xfff
backtostart:
	beq	$t1,$zero,done
	srl	$t1,$t1,1
	j	backtostart
		   
done: 
