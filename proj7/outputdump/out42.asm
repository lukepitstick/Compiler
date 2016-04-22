.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t4, 1
li $s2, 2
slt $t4, $t4, $s2
li $s2, 3
li $t7, 4
slt $s2, $s2, $t7
or $t4, $t4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li $t4, 1
li $s2, 2
sgt $t4, $t4, $s2
li $s2, 3
li $t7, 4
slt $s2, $s2, $t7
or $t4, $t4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li $t4, 1
li $s2, 2
slt $t4, $t4, $s2
li $s2, 3
li $t7, 4
sgt $s2, $s2, $t7
or $t4, $t4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li $t4, 1
li $s2, 2
sgt $t4, $t4, $s2
li $s2, 3
li $t7, 4
sgt $s2, $s2, $t7
or $t4, $t4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li   $v0, 10
syscall