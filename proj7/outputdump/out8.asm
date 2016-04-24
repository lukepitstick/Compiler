.data
False: .asciiz "False"
True: .asciiz "True"
n: .word 4
p: .word 4
i: .word 4
s: .word 4
stringtmptmp0: .asciiz "\n"
stringtmptmp1: .asciiz "\n"

.text
main:
li $t5, 1
la   $s0, i
sw $t5, ($s0)

li $t5, 0
la   $s0, s
sw $t5, ($s0)

li $t5, 1
la   $s0, p
sw $t5, ($s0)

li $v0, 5
syscall
la $t0, n
sw $v0, 0($t0)

L1: nop
la $s0, i
lw $t1, ($s0)
la $s0, n
lw $s6, ($s0)
slt $t1, $t1, $s6
blez $t1, L2
la $s0, s
lw $t5, ($s0)
la $s0, i
lw $t1, ($s0)
add $t5, $t5, $t1
la   $s0, s
sw $t5, ($s0)

la $s0, p
lw $t5, ($s0)
la $s0, i
lw $t1, ($s0)
mul $t5, $t5, $t1
la   $s0, p
sw $t5, ($s0)

la $s0, i
lw $t5, ($s0)
li $t1, 1
add $t5, $t5, $t1
la   $s0, i
sw $t5, ($s0)

b L1
L2: nop
la $s0, s
lw $t5, ($s0)
add $a0, $t5,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, p
lw $t5, ($s0)
add $a0, $t5,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

li   $v0, 10
syscall