

	addi $sp, $sp, 0
	j $funcmain

$funcmain:
	li $s6, 24
	sw $s6, 0($sp)
	li $v0, 10
	syscall
	li $v0, 10
	syscall
