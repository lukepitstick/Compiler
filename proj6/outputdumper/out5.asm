.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $s4, 41
li $t0, 1
add $s4, $s4, $t0
la   $s0, x
sw $s4, ($s0)

la $s0, x
lw $s4, ($s0)
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall