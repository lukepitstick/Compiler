.data
False: .asciiz "False"
True: .asciiz "True"
j: .word 4
x: .word 4
y: .word 4
i: .word 4
z: .word 4
stringtmptmp0: .asciiz " "
stringtmptmp1: .asciiz " \n"

.text
main:
li $t9, 0
la   $s0, i
sw $t9, ($s0)

L1: nop
la $s0, i
lw $t3, ($s0)
li $t1, 5
slt $t3, $t3, $t1
blez $t3, L2
li $t9, 0
la   $s0, j
sw $t9, ($s0)

L3: nop
la $s0, j
lw $t3, ($s0)
li $t1, 5
slt $t3, $t3, $t1
blez $t3, L4
la $s0, i
lw $t9, ($s0)
la $s0, j
lw $t3, ($s0)
add $t9, $t9, $t3
li $t3, 3
rem $t9, $t9, $t3
li $t3, 0
seq $t9, $t9, $t3
la   $s0, x
sw $t9, ($s0)

la $s0, i
lw $t9, ($s0)
li $t3, 2
rem $t9, $t9, $t3
li $t3, 0
seq $t9, $t9, $t3
la   $s0, y
sw $t9, ($s0)

la $s0, j
lw $t9, ($s0)
li $t3, 2
rem $t9, $t9, $t3
li $t3, 0
seq $t9, $t9, $t3
la   $s0, z
sw $t9, ($s0)

la $s0, x
lw $t3, ($s0)
la $s0, y
lw $t1, ($s0)
la $s0, z
lw $t4, ($s0)
or $t1, $t1, $t4
and $t3, $t3, $t1
blez $t3, L5
la $s0, i
lw $t9, ($s0)
add $a0, $t9,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, j
lw $t9, ($s0)
add $a0, $t9,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

L5: nop
la $s0, j
lw $t9, ($s0)
li $t3, 1
add $t9, $t9, $t3
la   $s0, j
sw $t9, ($s0)

b L3
L4: nop
la $s0, i
lw $t9, ($s0)
li $t3, 1
add $t9, $t9, $t3
la   $s0, i
sw $t9, ($s0)

b L1
L2: nop
li   $v0, 10
syscall