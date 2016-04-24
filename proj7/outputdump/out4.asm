.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
stringtmptmp0: .asciiz "Yes\n"
stringtmptmp1: .asciiz "No\n"

.text
main:
li $v0, 5
syscall
la $t0, i
sw $v0, 0($t0)

la $s0, i
lw $s3, ($s0)
li $s4, 15
slt $s3, $s3, $s4
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