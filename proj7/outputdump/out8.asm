.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
p: .word 4
n: .word 4
s: .word 4
stringtmptmp0: .asciiz "\n"
stringtmptmp1: .asciiz "\n"

.text
main:
li $t9, 1
la   $s0, i
sw $t9, ($s0)

li $t9, 0
la   $s0, s
sw $t9, ($s0)

li $t9, 1
la   $s0, p
sw $t9, ($s0)

li $v0, 5
syscall
la $t0, n
sw $v0, 0($t0)

L1: nop
la $s0, i
lw $t4, ($s0)
la $s0, n
lw $t1, ($s0)
slt $t4, $t4, $t1
blez $t4, L2
la $s0, s
lw $t9, ($s0)
la $s0, i
lw $t4, ($s0)
add $t9, $t9, $t4
la   $s0, s
sw $t9, ($s0)

la $s0, p
lw $t9, ($s0)
la $s0, i
lw $t4, ($s0)
mul $t9, $t9, $t4
la   $s0, p
sw $t9, ($s0)

la $s0, i
lw $t9, ($s0)
li $t4, 1
add $t9, $t9, $t4
la   $s0, i
sw $t9, ($s0)

b L1
L2: nop
la $s0, s
lw $t9, ($s0)
add $a0, $t9,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, p
lw $t9, ($s0)
add $a0, $t9,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

li   $v0, 10
syscall