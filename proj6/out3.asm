.data
.text
main:
li $s6, 5
li $s5, 10
sge $s6, $s6, $s5
add $a0, $s6,0
li $v0, 1
syscall

li $s6, 5
li $s5, 10
sle $s6, $s6, $s5
add $a0, $s6,0
li $v0, 1
syscall

li $s6, 5
li $s5, 10
seq $s6, $s6, $s5
add $a0, $s6,0
li $v0, 1
syscall

li   $v0, 10
syscall