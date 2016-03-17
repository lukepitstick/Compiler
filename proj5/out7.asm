.data
x: .word 4
.text
main:
li $v0, 5
syscall
la $t0, x
sw $v0, 0($t0)

li $v0, 5
syscall
la $t0, x
sw $v0, 0($t0)

li   $v0, 10
syscall