.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t3, 1
li $t5, 1
and $t3, $t3, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li $t3, 1
li $t5, 0
and $t3, $t3, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li $t3, 0
li $t5, 1
and $t3, $t3, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li $t3, 0
li $t5, 0
and $t3, $t3, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li   $v0, 10
syscall