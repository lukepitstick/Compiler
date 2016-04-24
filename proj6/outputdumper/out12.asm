.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 1
li $t0, 2
li $s2, 1
add $t0, $t0, $s2
add $s4, $s4, $t0
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall