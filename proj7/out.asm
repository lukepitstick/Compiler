.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4
stringtmptmp0: .asciiz "Yes\n"
stringtmptmp1: .asciiz "No\n"

.text
main:
li $s7, 0
la   $s0, x
sw $s7, ($s0)

la $s0, x
lw $s3, ($s0)
blez $s3, L1
la $a0, stringtmptmp0
li $v0, 4
syscall

b L2
L1: nop
la $a0, stringtmptmp1
li $v0, 4
syscall

L2: nop
li   $v0, 10
syscall