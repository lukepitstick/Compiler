.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
stringtmptmp0: .asciiz "Done\n"
stringtmptmp1: .asciiz "Done\n"
.text
main:
la $a0, stringtmptmp0
li $v0, 4
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

