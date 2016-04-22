.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t6, 6
li $t9, 7
mul $t6, $t6, $t9
add $a0, $t6,0
li $v0, 1
syscall

li   $v0, 10
syscall