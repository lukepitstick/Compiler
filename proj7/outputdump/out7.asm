.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t0, 1
la $s0, False
la $s1, True
movn $a0,$s1,$t0
movz $a0,$s0,$t0
li $v0, 4
syscall
li   $v0, 10
syscall