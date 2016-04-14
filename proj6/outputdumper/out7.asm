.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 5
li $t0, 3
add $s4, $s4, $t0
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall