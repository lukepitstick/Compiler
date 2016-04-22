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
li $s4, 4
la   $s0, a
sw $s4, ($s0)

li $s4, 9
la   $s0, b
sw $s4, ($s0)

la $s0, a
lw $s1, ($s0)
la $s0, b
lw $t3, ($s0)
slt $s1, $s1, $t3
blez $s1, L1
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