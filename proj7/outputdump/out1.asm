.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4
stringtmptmp0: .asciiz "Yes\n"
stringtmptmp1: .asciiz "Done\n"

.text
main:
li $t2, 0
la   $s0, x
sw $t2, ($s0)

la $s0, x
lw $t8, ($s0)
blez $t8, L1
la $a0, stringtmptmp0
li $v0, 4
syscall

L1: nop
la $a0, stringtmptmp1
li $v0, 4
syscall

li   $v0, 10
syscall