.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $t4, 1
la   $s0, x
sw $t4, ($s0)

la $s0, x
lw $t4, ($s0)
add $a0, $t4,0
li $v0, 1
syscall

li   $v0, 10
syscall