.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s7, 1
li $t1, 1
and $s7, $s7, $t1
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 1
li $t1, 0
and $s7, $s7, $t1
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 0
li $t1, 1
and $s7, $s7, $t1
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 0
li $t1, 0
and $s7, $s7, $t1
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li   $v0, 10
syscall