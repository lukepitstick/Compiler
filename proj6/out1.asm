.data
.text
main:
li $t3, 5
li $s1, 6
li $t9, 2
div $s1, $s1, $t9
mul $t3, $t3, $s1
add $a0, $t3,0
li $v0, 1
syscall

li $t3, 6
li $s1, 2
div $t3, $t3, $s1
li $s1, 5
mul $t3, $t3, $s1
add $a0, $t3,0
li $v0, 1
syscall

li   $v0, 10
syscall