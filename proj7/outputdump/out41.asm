.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t0, 1
li $s2, 2
slt $t0, $t0, $s2
li $s2, 3
li $s1, 4
slt $s2, $s2, $s1
or $t0, $t0, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t0
movz $a0,$s0,$t0
li $v0, 4
syscall
li $t0, 1
li $s2, 2
sgt $t0, $t0, $s2
li $s2, 3
li $s1, 4
slt $s2, $s2, $s1
or $t0, $t0, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t0
movz $a0,$s0,$t0
li $v0, 4
syscall
li $t0, 1
li $s2, 2
slt $t0, $t0, $s2
li $s2, 3
li $s1, 4
sgt $s2, $s2, $s1
or $t0, $t0, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t0
movz $a0,$s0,$t0
li $v0, 4
syscall
li $t0, 1
li $s2, 2
sgt $t0, $t0, $s2
li $s2, 3
li $s1, 4
sgt $s2, $s2, $s1
or $t0, $t0, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$t0
movz $a0,$s0,$t0
li $v0, 4
syscall
li   $v0, 10
syscall