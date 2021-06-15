.data
	true: .byte 1
	false: .byte 0
	str0: .asciiz ";\n"
.text
main:
	li $s1, 0
	li $s0, 11
L0:
	la $t0, false
	bge $s1, $s0, SKIP0
	la $t0, true
SKIP0:
	la $t1, true
	beq $t1, $t0, if0
	j L1
L1:
	j END
if0:
	li $t1, 1
	addu $t1, $s1, $t1
	move $s1, $t1
	li $v0, 4
	la $a0, str0
	syscall
	li.s $f1, 1.0
	add.s $f0, $f12, $f1
	mov.s $f12, $f0
	j L0
END:
