.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $v0, 5
syscall
la $t0, x
sw $v0, 0($t0)

la $s0, x
lw $s4, ($s0)
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall