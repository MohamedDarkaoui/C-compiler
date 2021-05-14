.data
	string0: .asciiz "   "
	string1: .asciiz "\n"
.text


	addi $sp, $sp, 0
	li $s6, 0
	sw $s6, 0($sp)

label0:
	lw $s6, 0($sp)
	li $s7, 10
	slt $s6, $s6, $s7
	beqz $s6, label1
	addi $sp, $sp, -4
	li $s6, 0
	sw $s6, 0($sp)

label2:
	lw $s6, 0($sp)
	li $s7, 10
	slt $s6, $s6, $s7
	beqz $s6, label3
	lw $s6, 0($sp)
	lw $s7, 4($sp)
	mul $s6, $s6, $s7
	li $v0, 1
	move $a0, $s6
	syscall
	li $v0, 4
	la $a0, string0
	syscall
	lw $s6, 0($sp)
	li $s7, 1
	add $s6, $s6, $s7
	sw $s6, 0($sp)
	j label2

label3:
	addi $sp, $sp, 4
	li $v0, 4
	la $a0, string1
	syscall
	lw $s6, 0($sp)
	li $s7, 1
	add $s6, $s6, $s7
	sw $s6, 0($sp)
	j label0

label1:
	addi $sp, $sp, 0
