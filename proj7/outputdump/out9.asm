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
lw $t5, ($s0)
la   $s0, i
sw $t5, ($s0)

L1: nop
la $s0, i
lw $s4, ($s0)
li $t4, 0
sge $s4, $s4, $t4
blez $s4, L2
la $s0, i
lw $t5, ($s0)
add $a0, $t5,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, i
lw $t5, ($s0)
li $s4, 2
sub $t5, $t5, $s4
la   $s0, i
sw $t5, ($s0)

b L1
L2: nop
li   $v0, 10
syscall