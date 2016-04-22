.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t9, 2
li $t2, 3
add $t9, $t9, $t2
li $t2, 4
mul $t9, $t9, $t2
add $a0, $t9,0
li $v0, 1
syscall

li $t9, 6
li $t2, 2
li $t7, 3
mul $t2, $t2, $t7
div $t9, $t9, $t2
add $a0, $t9,0
li $v0, 1
syscall

li   $v0, 10
syscall