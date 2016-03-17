.data
z: .word 4
y: .word 4
x: .word 4
.text
main:
li $v0, 5
syscall
la $t0, x
sw $v0, 0($t0)

li $v0, 5
syscall
la $t0, y
sw $v0, 0($t0)

li $v0, 5
syscall
la $t0, z
sw $v0, 0($t0)

li   $v0, 10
syscall