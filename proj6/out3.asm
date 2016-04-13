.data
.text
main:
li $t2, 5
li $t1, 10
sge $t2, $t2, $t1
add $a0, $t2,0
li $v0, 1
syscall

li $t2, 5
li $t1, 10
sle $t2, $t2, $t1
add $a0, $t2,0
li $v0, 1
syscall

li $t2, 5
li $t1, 10
seq $t2, $t2, $t1
add $a0, $t2,0
li $v0, 1
syscall

li   $v0, 10
syscall