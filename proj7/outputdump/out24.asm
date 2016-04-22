.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t7, 5
li $s2, 6
li $t6, 2
div $s2, $s2, $t6
mul $t7, $t7, $s2
add $a0, $t7,0
li $v0, 1
syscall

li $t7, 6
li $s2, 2
div $t7, $t7, $s2
li $s2, 5
mul $t7, $t7, $s2
add $a0, $t7,0
li $v0, 1
syscall

li   $v0, 10
syscall