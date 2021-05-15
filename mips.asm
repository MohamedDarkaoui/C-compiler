.data
	float0: .float 10.0
	string0: .asciiz "; "
	float1: .float 10.0
	string1: .asciiz "; "
	float2: .float 10.0
	string2: .asciiz "; "
	float3: .float 10.0
	string3: .asciiz "; "
	float4: .float 10.0
	string4: .asciiz "; "
	float5: .float 10.0
	string5: .asciiz "; "
	float6: .float 10.0
	string6: .asciiz "; "
	float7: .float 10.0
	string7: .asciiz "; "
.text


main:
	l.s $f9, float0
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string0
	syscall
	l.s $f9, float1
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string1
	syscall
	l.s $f9, float2
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string2
	syscall
	l.s $f9, float3
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string3
	syscall
	l.s $f9, float4
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string4
	syscall
	l.s $f9, float5
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string5
	syscall
	l.s $f9, float6
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string6
	syscall
	l.s $f9, float7
	li $v0, 2
	mov.s $f12, $f9
	syscall
	li $v0, 4
	la $a0, string7
	syscall
