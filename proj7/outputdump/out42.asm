.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t5, 1
li $s4, 2
slt $t5, $t5, $s4
li $s4, 3
li $s5, 4
slt $s4, $s4, $s5
or $t5, $t5, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 1
li $s4, 2
sgt $t5, $t5, $s4
li $s4, 3
li $s5, 4
slt $s4, $s4, $s5
or $t5, $t5, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 1
li $s4, 2
slt $t5, $t5, $s4
li $s4, 3
li $s5, 4
sgt $s4, $s4, $s5
or $t5, $t5, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 1
li $s4, 2
sgt $t5, $t5, $s4
li $s4, 3
li $s5, 4
sgt $s4, $s4, $s5
or $t5, $t5, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li   $v0, 10
syscall