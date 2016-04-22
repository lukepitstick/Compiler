.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t3, 2
li $t9, 3
mul $t3, $t3, $t9
li $t9, 4
add $t3, $t3, $t9
add $a0, $t3,0
li $v0, 1
syscall

li $t3, 4
li $t9, 2
li $s2, 3
mul $t9, $t9, $s2
add $t3, $t3, $t9
add $a0, $t3,0
li $v0, 1
syscall

li   $v0, 10
syscall