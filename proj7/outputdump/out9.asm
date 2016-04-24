.data
False: .asciiz "False"
True: .asciiz "True"
n: .word 4
i: .word 4
stringtmptmp0: .asciiz " "

.text
main:
li $v0, 5
syscall
la $t0, n
sw $v0, 0($t0)

la $s0, n
lw $t4, ($s0)
la   $s0, i
sw $t4, ($s0)

L1: nop
la $s0, i
lw $t8, ($s0)
li $s4, 0
sge $t8, $t8, $s4
blez $t8, L2
la $s0, i
lw $t4, ($s0)
add $a0, $t4,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, i
lw $t4, ($s0)
li $t8, 2
sub $t4, $t4, $t8
la   $s0, i
sw $t4, ($s0)

b L1
L2: nop
li   $v0, 10
syscall