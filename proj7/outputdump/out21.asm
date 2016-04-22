.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s7, 40
li $t3, 20
sub $s7, $s7, $t3
li $t3, 2
sub $s7, $s7, $t3
add $a0, $s7,0
li $v0, 1
syscall

li   $v0, 10
syscall