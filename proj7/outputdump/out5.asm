.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s3, 1
la $s0, False
la $s1, True
movn $a0,$s1,$s3
movz $a0,$s0,$s3
li $v0, 4
syscall
li   $v0, 10
syscall