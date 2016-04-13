.data
s2: .asciiz False
.text
main:
li $s3, 1
li $s5, 1
or $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li $s3, 1
li $s5, 0
and $s5, $s5, 
add $a0, $s5,0
li $v0, 1
syscall

li $s3, 0
li $s5, 1
or $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li $s3, 0
li $s5, 0
and $s5, $s5, 
add $a0, $s5,0
li $v0, 1
syscall

li   $v0, 10
syscall