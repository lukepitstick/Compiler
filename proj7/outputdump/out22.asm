.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t0, 40
li $t2, 20
div $t0, $t0, $t2
li $t2, 2
div $t0, $t0, $t2
add $a0, $t0,0
li $v0, 1
syscall

li   $v0, 10
syscall