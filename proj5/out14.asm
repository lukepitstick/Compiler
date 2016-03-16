.data
aa: .word 4
ba: .word 4
.text
main:
li $v0, 5
syscall
la $t0, ba
sw $v0, 0($t0)

li $v0, 5
syscall
la $t0, aa
sw $v0, 0($t0)

li   $v0, 10
syscall