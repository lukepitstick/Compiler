.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t3, 20
li $t1, 4
div $t3, $t3, $t1
add $a0, $t3,0
li $v0, 1
syscall

li   $v0, 10
syscall