.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t2, 20
li $s5, 4
div $t2, $t2, $s5
add $a0, $t2,0
li $v0, 1
syscall

li   $v0, 10
syscall