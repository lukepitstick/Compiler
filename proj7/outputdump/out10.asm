.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
j: .word 4
x: .word 4
y: .word 4
z: .word 4
stringtmptmp0: .asciiz " "
stringtmptmp1: .asciiz " \n"

.text
main:
li $t5, 0
la   $s0, i
sw $t5, ($s0)

L1: nop
la $s0, i
lw $s5, ($s0)
li $t1, 5
slt $s5, $s5, $t1
blez $s5, L2
li $t5, 0
la   $s0, j
sw $t5, ($s0)

L3: nop
la $s0, j
lw $s5, ($s0)
li $t1, 5
slt $s5, $s5, $t1
blez $s5, L4
la $s0, i
lw $t5, ($s0)
la $s0, j
lw $s5, ($s0)
add $t5, $t5, $s5
li $s5, 3
rem $t5, $t5, $s5
li $s5, 0
seq $t5, $t5, $s5
la   $s0, x
sw $t5, ($s0)

la $s0, i
lw $t5, ($s0)
li $s5, 2
rem $t5, $t5, $s5
li $s5, 0
seq $t5, $t5, $s5
la   $s0, y
sw $t5, ($s0)

la $s0, j
lw $t5, ($s0)
li $s5, 2
rem $t5, $t5, $s5
li $s5, 0
seq $t5, $t5, $s5
la   $s0, z
sw $t5, ($s0)

la $s0, x
lw $s5, ($s0)
la $s0, y
lw $t1, ($s0)
la $s0, z
lw $t9, ($s0)
or $t1, $t1, $t9
and $s5, $s5, $t1
blez $s5, L5
la $s0, i
lw $t5, ($s0)
add $a0, $t5,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, j
lw $t5, ($s0)
add $a0, $t5,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

L5: nop
la $s0, j
lw $t5, ($s0)
li $s5, 1
add $t5, $t5, $s5
la   $s0, j
sw $t5, ($s0)

b L3
L4: nop
la $s0, i
lw $t5, ($s0)
li $s5, 1
add $t5, $t5, $s5
la   $s0, i
sw $t5, ($s0)

b L1
L2: nop
li   $v0, 10
syscall