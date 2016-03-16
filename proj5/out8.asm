.data
x: .word 4
.text
main:
li $t0, 5
la   $s0, x
sw   $t0, ($s0)

li   $v0, 10
syscall