.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t3, 1
li $s5, 1
or $t3, $t3, $s5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li $t3, 1
li $s5, 0
or $t3, $t3, $s5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li $t3, 0
li $s5, 1
or $t3, $t3, $s5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li $t3, 0
li $s5, 0
or $t3, $t3, $s5
la $s0, False
la $s1, True
movn $a0,$s1,$t3
movz $a0,$s0,$t3
li $v0, 4
syscall
li   $v0, 10
syscall