.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t5, 22
li $t9, 4
div $t5, $t5, $t9
add $a0, $t5,0
li $v0, 1
syscall

li   $v0, 10
syscall