.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t1, 22
li $t0, 4
div $t1, $t1, $t0
add $a0, $t1,0
li $v0, 1
syscall

li   $v0, 10
syscall