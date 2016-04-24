.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 5
li $s2, 6
li $t2, 2
div $s2, $s2, $t2
mul $s4, $s4, $s2
add $a0, $s4,0
li $v0, 1
syscall

li $s4, 8
li $s2, 2
div $s4, $s4, $s2
li $s2, 5
mul $s4, $s4, $s2
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall