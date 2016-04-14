.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 1
add $a0, $s4,0
li $v0, 1
syscall

li $s4, 5
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall