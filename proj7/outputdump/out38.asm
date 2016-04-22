.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s7, 5
li $t2, 10
sge $s7, $s7, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 5
li $t2, 5
sge $s7, $s7, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 5
li $t2, 0
sge $s7, $s7, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li   $v0, 10
syscall