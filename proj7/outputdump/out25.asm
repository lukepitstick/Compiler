.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s6, 2
li $s2, 3
add $s6, $s6, $s2
li $s2, 4
mul $s6, $s6, $s2
add $a0, $s6,0
li $v0, 1
syscall

li $s6, 6
li $s2, 2
li $s7, 3
mul $s2, $s2, $s7
div $s6, $s6, $s2
add $a0, $s6,0
li $v0, 1
syscall

li   $v0, 10
syscall