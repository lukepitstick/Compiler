.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s7, 6
li $s5, 7
mul $s7, $s7, $s5
add $a0, $s7,0
li $v0, 1
syscall

li   $v0, 10
syscall