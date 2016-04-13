.data
s2: .asciiz False
.text
main:
li $s3, 5
li $s5, 10
sge $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li $s3, 5
li $s5, 10
sle $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li $s3, 5
li $s5, 10
seq $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li   $v0, 10
syscall