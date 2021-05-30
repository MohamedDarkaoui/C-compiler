

	addi $sp, $sp, 0
	j $funcmain

$funcmain:
	li $s6, 97
	sb $s6, 0($sp)
	li $s6, 98
	sb $s6, -4($sp)
	li $s6, 99
	sb $s6, -8($sp)
	li $s6, 100
	sb $s6, -12($sp)
	li $s6, 101
	sb $s6, -16($sp)
	li $s6, 100
	sb $s6, -8($sp)
	li $v0, 10
	syscall
	li $v0, 10
	syscall
