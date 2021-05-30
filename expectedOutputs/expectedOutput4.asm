

	addi $sp, $sp, 0
	j $funcmain

$funcfibonacci:
	sw $ra, -4($sp)

label0:
	addi $sp, $sp, -8
	lw $s6, 8($sp)
	li $s7, 2
	slt $s6, $s6, $s7
	beqz $s6, label1
	li $s6, 1
	move $v0, $s6
	lw $ra, 4($sp)
	addi $sp, $sp, 8
	jr $ra
	j label1

label1:
	addi $sp, $sp, 8
	lw $s6, 0($sp)
	li $s7, 1
	sub $s6, $s6, $s7
	sw $s6, -8($sp)
	addi $sp, $sp, -8
	jal $funcfibonacci
	addi $sp, $sp, 8
	move $s6, $v0
	sw $s6, -8($sp)
	lw $s7, 0($sp)
	li $s4, 2
	sub $s7, $s7, $s4
	sw $s7, -12($sp)
	addi $sp, $sp, -12
	jal $funcfibonacci
	addi $sp, $sp, 12
	move $s7, $v0
	lw $s6, -8($sp)
	add $s6, $s6, $s7
	move $v0, $s6
	lw $ra, -4($sp)
	addi $sp, $sp, 0
	jr $ra
	lw $ra, -4($sp)
	jr $ra
$funcmain:
	li $s6, 5
	sw $s6, -4($sp)
	addi $sp, $sp, -4
	jal $funcfibonacci
	addi $sp, $sp, 4
	move $s6, $v0
	sw $s6, 0($sp)
	lw $s6, 0($sp)
	li $v0, 1
	move $a0, $s6
	syscall
	li $v0, 10
	syscall
	li $v0, 10
	syscall
