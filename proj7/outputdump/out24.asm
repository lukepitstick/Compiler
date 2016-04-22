.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t0, 5
li $t7, 6
li $t4, 2
div $t7, $t7, $t4
mul $t0, $t0, $t7
add $a0, $t0,0
li $v0, 1
syscall

li $t0, 6
li $t7, 2
div $t0, $t0, $t7
li $t7, 5
mul $t0, $t0, $t7
add $a0, $t0,0
li $v0, 1
syscall

li   $v0, 10
syscall