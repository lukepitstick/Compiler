.data
False: .asciiz "False"
True: .asciiz "True"
s: .word 4
p: .word 4
n: .word 4
i: .word 4
stringtmptmp0: .asciiz "\n"
stringtmptmp1: .asciiz "\n"

.text
main:
li $s5, 1
la   $s0, i
sw $s5, ($s0)

li $s5, 0
la   $s0, s
sw $s5, ($s0)

li $s5, 1
la   $s0, p
sw $s5, ($s0)

li $v0, 5
syscall
la $t0, n
sw $v0, 0($t0)

L1: nop
la $s0, i
lw $s3, ($s0)
la $s0, n
lw $t6, ($s0)
slt $s3, $s3, $t6
blez $s3, L2
la $s0, s
lw $s5, ($s0)
la $s0, i
lw $s3, ($s0)
add $s5, $s5, $s3
la   $s0, s
sw $s5, ($s0)

la $s0, p
lw $s5, ($s0)
la $s0, i
lw $s3, ($s0)
mul $s5, $s5, $s3
la   $s0, p
sw $s5, ($s0)

la $s0, i
lw $s5, ($s0)
li $s3, 1
add $s5, $s5, $s3
la   $s0, i
sw $s5, ($s0)

b L1
L2: nop
la $s0, s
lw $s5, ($s0)
add $a0, $s5,0
li $v0, 1
syscall

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, p
lw $s5, ($s0)
add $a0, $s5,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

li   $v0, 10
syscall