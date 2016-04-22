.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t9, 5
li $t5, 5
seq $t9, $t9, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t9
movz $a0,$s0,$t9
li $v0, 4
syscall
li $t9, 5
li $t5, 10
seq $t9, $t9, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t9
movz $a0,$s0,$t9
li $v0, 4
syscall
li   $v0, 10
syscall