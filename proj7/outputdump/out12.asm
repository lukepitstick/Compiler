.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t2, 22
li $t6, 4
div $t2, $t2, $t6
add $a0, $t2,0
li $v0, 1
syscall

li   $v0, 10
syscall