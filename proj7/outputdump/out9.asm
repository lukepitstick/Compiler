.data
False: .asciiz "False"
True: .asciiz "True"
x: .asciiz 

.text
main:
li   $v0, 10
syscall