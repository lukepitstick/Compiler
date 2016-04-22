.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s2, 40
li $t0, 20
sub $s2, $s2, $t0
li $t0, 2
sub $s2, $s2, $t0
add $a0, $s2,0
li $v0, 1
syscall

li   $v0, 10
syscall