.data
.text
main:
li $t6, 1
li $s3, 1
or $t6, $t6, $s3
add $a0, $t6,0
li $v0, 1
syscall

li $t6, 1
li $s3, 0
and $s3, $s3, 
add $a0, $s3,0
li $v0, 1
syscall

li $t6, 0
li $s3, 1
or $t6, $t6, $s3
add $a0, $t6,0
li $v0, 1
syscall

li $t6, 0
li $s3, 0
and $s3, $s3, 
add $a0, $s3,0
li $v0, 1
syscall

li   $v0, 10
syscall