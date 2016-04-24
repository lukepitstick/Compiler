.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4
stringtmptmp0: .asciiz "Yes\n"
stringtmptmp1: .asciiz "Done\n"

.text
main:
li $s1, 1
la   $s0, x
sw $s1, ($s0)

la $s0, x
lw $t1, ($s0)
blez $t1, L1
la $a0, stringtmptmp0
li $v0, 4
syscall

L1: nop
la $a0, stringtmptmp1
li $v0, 4
syscall

li   $v0, 10
syscall