.data
x: .word 0
y: .word 0
z: .word 0
a: .word 0

# begin
# read(x, y);
# z := x + y + a;
# write(z);
# end

.text
	li $v0, 5 #read integer
	syscall
	
	la $t0, x
	sw $v0, 0($t0)
	
	li $v0, 5 #read integer
	syscall
	
	la $t0, y
	sw $v0, 0($t0)
	
	li $v0, 5
	syscall
	
	la $t0, a
	sw $v0, 0($t0)
	
	#assign
	la $s0, x
	lw $t1, 0($s0)
	la $s0, y
	lw $t2, 0($s0)
	la $s0, a
	lw $t3, 0($s0)
	add $t0, $t1, $t2
	sw $t0, 0($t1)
	add $t0, $t1, $t3
	la $s0, z
	sw $t0, 0($s0)
	
	li $v0, 1
	la $a0, z
	syscall
	
	li $v0, 10
	syscall
