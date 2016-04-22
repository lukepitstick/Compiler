.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $s2, 1
la   $s0, x
sw $s2, ($s0)

la $s0, x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

li   $v0, 10
syscall