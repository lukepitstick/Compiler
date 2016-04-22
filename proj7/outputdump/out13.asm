.data
False: .asciiz "False"
True: .asciiz "True"
b: .word 4
a: .word 4

.text
main:
li $s6, 4
la   $s0, a
sw $s6, ($s0)

li $s6, 6
la   $s0, b
sw $s6, ($s0)

la $s0, a
lw $t3, ($s0)
la $s0, b
lw $t1, ($s0)
slt $t3, $t3, $t1
blez $t3, L1
li $s6, 2
la   $s0, b
sw $s6, ($s0)

L1: nop
la $s0, b
lw $s6, ($s0)
add $a0, $s6,0
li $v0, 1
syscall

li   $v0, 10
syscall