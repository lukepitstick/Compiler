.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t0, 40
li $s4, 20
div $t0, $t0, $s4
li $s4, 2
div $t0, $t0, $s4
add $a0, $t0,0
li $v0, 1
syscall

li   $v0, 10
syscall