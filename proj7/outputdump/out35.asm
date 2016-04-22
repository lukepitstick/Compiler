.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s2, 5
li $t3, 10
slt $s2, $s2, $t3
la $s0, False
la $s1, True
movn $a0,$s1,$s2
movz $a0,$s0,$s2
li $v0, 4
syscall
li $s2, 5
li $t3, 5
slt $s2, $s2, $t3
la $s0, False
la $s1, True
movn $a0,$s1,$s2
movz $a0,$s0,$s2
li $v0, 4
syscall
li $s2, 5
li $t3, 0
slt $s2, $s2, $t3
la $s0, False
la $s1, True
movn $a0,$s1,$s2
movz $a0,$s0,$s2
li $v0, 4
syscall
li   $v0, 10
syscall