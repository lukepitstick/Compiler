.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $s1, 1
la   $s0, x
sw $s1, ($s0)

la $s0, x
lw $s1, ($s0)
add $a0, $s1,0
li $v0, 1
syscall

li   $v0, 10
syscall