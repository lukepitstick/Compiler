.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 20
li $t0, 10
add $s4, $s4, $t0
li $t0, 9
li $s2, 3
add $t0, $t0, $s2
add $s4, $s4, $t0
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall