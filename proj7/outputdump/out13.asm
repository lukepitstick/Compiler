.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t2, 40
li $t6, 20
sub $t2, $t2, $t6
li $t6, 2
sub $t2, $t2, $t6
add $a0, $t2,0
li $v0, 1
syscall

li   $v0, 10
syscall