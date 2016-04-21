.data
False: .asciiz "False"
True: .asciiz "True"
stringtmptmp0: .asciiz "Hello, world"

.text
main:
la $a0, stringtmptmp0
li $v0, 4
syscall

li   $v0, 10
syscall