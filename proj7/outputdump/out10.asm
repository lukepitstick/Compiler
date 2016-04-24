.data
False: .asciiz "False"
True: .asciiz "True"
j: .word 4
y: .word 4
z: .word 4
x: .word 4
i: .word 4
stringtmptmp0: .asciiz " "
stringtmptmp1: .asciiz " \n"

.text
main:
li $t8, 0
la   $s0, i
sw $t8, ($s0)

L1: nop
la $s0, i
lw $t9, ($s0)
li $s1, 5
slt $t9, $t9, $s1
blez $t9, L2
li $t8, 0
la   $s0, j
sw $t8, ($s0)

L3: nop
la $s0, j
lw $t9, ($s0)
li $s1, 5
slt $t9, $t9, $s1
blez $t9, L4
la $s0, i
lw $t8, ($s0)
la $s0, j
lw $t9, ($s0)
add $t8, $t8, $t9
li $t9, 3
rem $t8, $t8, $t9
li $t9, 0
seq $t8, $t8, $t9
la   $s0, x
sw $t8, ($s0)

la $s0, i
lw $t8, ($s0)
li $t9, 2
rem $t8, $t8, $t9
li $t9, 0
seq $t8, $t8, $t9
la   $s0, y
sw $t8, ($s0)

la $s0, j
lw $t8, ($s0)
li $t9, 2
rem $t8, $t8, $t9
li $t9, 0
seq $t8, $t8, $t9
la   $s0, z
sw $t8, ($s0)

la $s0, x
lw $t9, ($s0)
la $s0, y
lw $s1, ($s0)
la $s0, z
lw $s7, ($s0)
or $s1, $s1, $s7
and $t9, $t9, $s1
blez $t9, L5
la $s0, i
lw $t8, ($s0)
add $a0, $t8,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, j
lw $t8, ($s0)
add $a0, $t8,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

L5: nop
la $s0, j
lw $t8, ($s0)
li $t9, 1
add $t8, $t8, $t9
la   $s0, j
sw $t8, ($s0)

b L3
L4: nop
la $s0, i
lw $t8, ($s0)
li $t9, 1
add $t8, $t8, $t9
la   $s0, i
sw $t8, ($s0)

b L1
L2: nop
li   $v0, 10
syscall