.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
stringtmptmp0: .asciiz "\n"
stringtmptmp1: .asciiz "Done\n"

.text
main:
li $v0, 5
syscall
la $t0, i
sw $v0, 0($t0)

la $s0, i
lw $t7, ($s0)
li $s4, 0
sge $t7, $t7, $s4
blez $t7, L1
la $s0, i
lw $t7, ($s0)
la $s0, i
lw $s4, ($s0)
mul $t7, $t7, $s4
la   $s0, i
sw $t7, ($s0)

la $s0, i
lw $t7, ($s0)
add $a0, $t7,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

L1: nop
la $a0, stringtmptmp1
li $v0, 4
syscall

li   $v0, 10
syscall