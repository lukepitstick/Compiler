.data
.text
main:
li $s1, 1
li $t2, 1
or $s1, $s1, $t2
add $a0, $s1,0
li $v0, 1
syscall

li $s1, 1
li $t2, 0
and $t2, $t2, 
add $a0, $t2,0
li $v0, 1
syscall

li $s1, 0
li $t2, 1
or $s1, $s1, $t2
add $a0, $s1,0
li $v0, 1
syscall

li $s1, 0
li $t2, 0
and $t2, $t2, 
add $a0, $t2,0
li $v0, 1
syscall

li   $v0, 10
syscall