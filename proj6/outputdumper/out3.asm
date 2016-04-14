.data
False: .asciiz "False"
True: .asciiz "True"
y: .word 4
x: .word 4

.text
main:
li $s4, 16
la   $s0, x
sw $s4, ($s0)

la $s0, x
lw $s4, ($s0)
la   $s0, y
sw $s4, ($s0)

la $s0, y
lw $s4, ($s0)
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall