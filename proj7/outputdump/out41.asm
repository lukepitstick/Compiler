.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t8, 1
li $t4, 2
slt $t8, $t8, $t4
li $t4, 3
li $t7, 4
slt $t4, $t4, $t7
or $t8, $t8, $t4
la $s0, False
la $s1, True
movn $a0,$s1,$t8
movz $a0,$s0,$t8
li $v0, 4
syscall
li $t8, 1
li $t4, 2
sgt $t8, $t8, $t4
li $t4, 3
li $t7, 4
slt $t4, $t4, $t7
or $t8, $t8, $t4
la $s0, False
la $s1, True
movn $a0,$s1,$t8
movz $a0,$s0,$t8
li $v0, 4
syscall
li $t8, 1
li $t4, 2
slt $t8, $t8, $t4
li $t4, 3
li $t7, 4
sgt $t4, $t4, $t7
or $t8, $t8, $t4
la $s0, False
la $s1, True
movn $a0,$s1,$t8
movz $a0,$s0,$t8
li $v0, 4
syscall
li $t8, 1
li $t4, 2
sgt $t8, $t8, $t4
li $t4, 3
li $t7, 4
sgt $t4, $t4, $t7
or $t8, $t8, $t4
la $s0, False
la $s1, True
movn $a0,$s1,$t8
movz $a0,$s0,$t8
li $v0, 4
syscall
li   $v0, 10
syscall