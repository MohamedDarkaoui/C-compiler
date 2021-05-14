.data
	float0: .float 12.0
.text


	l.s $f9, float0
	s.s $f9, 0($sp)
	addi $sp, $sp, -4
	li $s6, 0
	sw $s6, 0($sp)

label0:
	lw $s6, 0($sp)
	li $s7, 10
	slt $s6, $s6, $s7
	beqz $s6, label1
	li $s6, 2
	sw $s6, -4($sp)

label2:
	lw $s6, 0($sp)
	li $s7, 5
	seq $s6, $s6, $s7
	beqz $s6, label3
	addi $sp, $sp, -8
	lw $s6, 8($sp)
	li $v0, 1
	move $a0, $s6
	syscall
	j label3

label3:
	addi $sp, $sp, 8
	lw $s6, 0($sp)
	li $s7, 1
	add $s6, $s6, $s7
	sw $s6, 0($sp)
	j label0

label1:
	addi $sp, $sp, 4
