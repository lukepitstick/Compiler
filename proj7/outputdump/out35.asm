.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t4, 5
li $s4, 10
slt $t4, $t4, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li $t4, 5
li $s4, 5
slt $t4, $t4, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li $t4, 5
li $s4, 0
slt $t4, $t4, $s4
la $s0, False
la $s1, True
movn $a0,$s1,$t4
movz $a0,$s0,$t4
li $v0, 4
syscall
li   $v0, 10
syscall