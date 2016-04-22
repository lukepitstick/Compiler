.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t5, 5
li $t2, 10
sle $t5, $t5, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 5
li $t2, 5
sle $t5, $t5, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 5
li $t2, 0
sle $t5, $t5, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li   $v0, 10
syscall