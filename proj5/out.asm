.data
x: .word 4
.text
la $a0, x
li $v0, 8
syscall