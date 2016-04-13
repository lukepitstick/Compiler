.data
s2: .asciiz False
.text
main:
li $s3, 5
li $s5, 6
li $t7, 2
div $s5, $s5, $t7
mul $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li $s3, 6
li $s5, 2
div $s3, $s3, $s5
li $s5, 5
mul $s3, $s3, $s5
add $a0, $s3,0
li $v0, 1
syscall

li   $v0, 10
syscall