.data
	$string0: .asciiz "; "
.text




	addi $sp, $sp, 0
	j $funcmain

$funcmain:
	li $s6, 0
	sw $s6, 0($sp)
	addi $sp, $sp, -4

label0:
	lw $s6, 4($sp)
	li $s7, 5
	slt $s6, $s6, $s7
	beqz $s6, label1
	lw $s6, 4($sp)
	li $s7, 1
	add $s6, $s6, $s7
	sw $s6, 4($sp)
	lw $s6, 4($sp)
	mtc1 $s6, $f9
	cvt.s.w $f9, $f9
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, $string0
	syscall
	j label0

label1:
	addi $sp, $sp, 4
	li $v0, 10
	syscall
	li $v0, 10
	syscall
