.data
False: .asciiz "False"
True: .asciiz "True"
z: .word 4
x: .word 4
y: .word 4

.text
main:
li $s4, 1
la   $s0, x
sw $s4, ($s0)

li $s4, 2
la   $s0, y
sw $s4, ($s0)

li $s4, 3
la   $s0, z
sw $s4, ($s0)

la $s0, x
lw $s4, ($s0)
la $s0, y
lw $s2, ($s0)
add $s4, $s4, $s2
la $s0, z
lw $s2, ($s0)
mul $s4, $s4, $s2
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall