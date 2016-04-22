.data
False: .asciiz "False"
True: .asciiz "True"
b: .word 4
a: .word 4

.text
main:
li $t8, 4
la   $s0, a
sw $t8, ($s0)

li $t8, 6
la   $s0, b
sw $t8, ($s0)

la $s0, a
lw $s4, ($s0)
la $s0, b
lw $s6, ($s0)
slt $s4, $s4, $s6
blez $s4, L1
li $t8, 2
la   $s0, b
sw $t8, ($s0)

L1: nop
la $s0, b
lw $t8, ($s0)
add $a0, $t8,0
li $v0, 1
syscall

li   $v0, 10
syscall