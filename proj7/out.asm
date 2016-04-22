.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
s: .word 4
p: .word 4
n: .word 4
nn: .word 4
j: .word 4
stringtmptmp0: .asciiz "even!"
stringtmptmp1: .asciiz "\n"
stringtmptmp2: .asciiz "\n"

.text
main:
li $t3, 1
la   $s0, j
sw $t3, ($s0)

li $t3, 4
la   $s0, nn
sw $t3, ($s0)

li $t3, 1
la   $s0, i
sw $t3, ($s0)

li $t3, 0
la   $s0, s
sw $t3, ($s0)

li $t3, 1
la   $s0, p
sw $t3, ($s0)

li $v0, 5
syscall
la $t0, n
sw $v0, 0($t0)

L1: nop
la $s0, i
lw $t0, ($s0)
la $s0, n
lw $t5, ($s0)
slt $t0, $t0, $t5
blez $t0, L2
la $s0, s
lw $t3, ($s0)
la $s0, i
lw $t0, ($s0)
add $t3, $t3, $t0
la   $s0, s
sw $t3, ($s0)

la $s0, p
lw $t3, ($s0)
la $s0, i
lw $t0, ($s0)
mul $t3, $t3, $t0
la   $s0, p
sw $t3, ($s0)

la $s0, i
lw $t3, ($s0)
li $t0, 1
add $t3, $t3, $t0
la   $s0, i
sw $t3, ($s0)

la $s0, i
lw $t0, ($s0)
li $t5, 2
rem $t0, $t0, $t5
li $t5, 1
seq $t0, $t0, $t5
blez $t0, L3
la $a0, stringtmptmp0
li $v0, 4
syscall

L3: nop
L5: nop
la $s0, j
lw $t3, ($s0)
la $s0, nn
lw $t0, ($s0)
slt $t3, $t3, $t0
blez $t3, L6
la $s0, nn
lw $t3, ($s0)
li $t0, 1
add $t3, $t3, $t0
add $a0, $t3,0
li $v0, 1
syscall

la $s0, j
lw $t3, ($s0)
li $t0, 1
add $t3, $t3, $t0
la   $s0, j
sw $t3, ($s0)

b L5
L6: nop
b L1
L2: nop
la $s0, s
lw $t3, ($s0)
add $a0, $t3,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

la $s0, p
lw $t3, ($s0)
add $a0, $t3,0
li $v0, 1
syscall

la $a0, stringtmptmp2
li $v0, 4
syscall

li   $v0, 10
syscall