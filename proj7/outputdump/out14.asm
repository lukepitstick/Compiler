.data
False: .asciiz "False"
True: .asciiz "True"
b: .word 4
a: .word 4
stringtmptmp0: .asciiz "a is less than b"
stringtmptmp1: .asciiz "b is less than a"
stringtmptmp2: .asciiz "PROGRAM DIDN'T FALL INTO PANIC!"

.text
main:
li $s2, 4
la   $s0, a
sw $s2, ($s0)

li $s2, 9
la   $s0, b
sw $s2, ($s0)

la $s0, a
lw $t8, ($s0)
la $s0, b
lw $t0, ($s0)
slt $t8, $t8, $t0
blez $t8, L1
la $a0, stringtmptmp0
li $v0, 4
syscall

b L2
L1: nop
la $a0, stringtmptmp1
li $v0, 4
syscall

L2: nop
la $a0, stringtmptmp2
li $v0, 4
syscall

li   $v0, 10
syscall