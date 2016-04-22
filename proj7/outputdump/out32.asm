.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s6, 1
li $t4, 0
li $t3, 0
and $t4, $t4, $t3
or $s6, $s6, $t4
la $s0, False
la $s1, True
movn $a0,$s1,$s6
movz $a0,$s0,$s6
li $v0, 4
syscall
li $s6, 0
li $t4, 0
and $s6, $s6, $t4
li $t4, 1
or $s6, $s6, $t4
la $s0, False
la $s1, True
movn $a0,$s1,$s6
movz $a0,$s0,$s6
li $v0, 4
syscall
li   $v0, 10
syscall