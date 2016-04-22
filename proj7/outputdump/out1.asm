.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li   $v0, 10
syscall