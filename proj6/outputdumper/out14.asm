.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $s4, 6
la   $s0, x
sw $s4, ($s0)

li $s4, 5
li $t0, 5
sub $s4, $s4, $t0
add $a0, $s4,0
li $v0, 1
syscall

li $s4, 1
add $a0, $s4,0
li $v0, 1
syscall

la $s0, x
lw $s4, ($s0)
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall