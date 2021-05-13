.data
	float0: .float 12.0
.text



	li $t0, 4
	sw $t0, -4($sp)
	l.s $f0, float0
	s.s $f0, -8($sp)
