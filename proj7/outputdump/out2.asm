.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s1, 1
la $s0, False
la $s1, True
movn $a0,$s1,$s1
movz $a0,$s0,$s1
li $v0, 4
syscall
li   $v0, 10
syscall