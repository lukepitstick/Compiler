.data
x: .word 4
.text
main:
li $t0, 5
la   $s0, x
sw   $t0, ($s0)

la $s0, x
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li   $v0, 10
syscall