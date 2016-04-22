.data
False: .asciiz "False"
True: .asciiz "True"
x: .asciiz "Hello, world"

.text
main:
la $a0, x
li $v0, 4
syscall

li   $v0, 10
syscall