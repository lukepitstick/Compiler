.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s1, 2
li $t9, 3
mul $s1, $s1, $t9
li $t9, 4
add $s1, $s1, $t9
add $a0, $s1,0
li $v0, 1
syscall

li $s1, 4
li $t9, 2
li $s6, 3
mul $t9, $t9, $s6
add $s1, $s1, $t9
add $a0, $s1,0
li $v0, 1
syscall

li   $v0, 10
syscall