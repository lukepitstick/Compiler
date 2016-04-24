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
lw $s7, ($s0)
li $t3, 5
sge $s7, $s7, $t3
blez $s7, L1
la $s0, i
lw $s7, ($s0)
la $s0, i
lw $t3, ($s0)
mul $s7, $s7, $t3
la   $s0, i
sw $s7, ($s0)

la $s0, i
lw $s7, ($s0)
add $a0, $s7,0
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