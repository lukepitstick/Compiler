.data
y: .word 4
x: .word 4
.text
main:
li $v0, 5
syscall
la $t0, x
sw $v0, 0($t0)

li $t1, 3
la $s0, x
lw $t2, ($s0)
add $t0,$t1,$t2
la   $s0, y
sw   $t0, ($s0)

la $s0, y
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li   $v0, 10
syscall