.data
.text
main:
li $s7, 5
li $s6, 6
li $t3, 2
div $s6, $s6, $t3
mul $s7, $s7, $s6
add $a0, $s7,0
li $v0, 1
syscall

li $s7, 6
li $s6, 2
div $s7, $s7, $s6
li $s6, 5
mul $s7, $s7, $s6
add $a0, $s7,0
li $v0, 1
syscall

li   $v0, 10
syscall