.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t9, 1
li $t0, 0
li $t4, 0
and $t0, $t0, $t4
or $t9, $t9, $t0
la $s0, False
la $s1, True
movn $a0,$s1,$t9
movz $a0,$s0,$t9
li $v0, 4
syscall
li $t9, 0
li $t0, 0
and $t9, $t9, $t0
li $t0, 1
or $t9, $t9, $t0
la $s0, False
la $s1, True
movn $a0,$s1,$t9
movz $a0,$s0,$t9
li $v0, 4
syscall
li   $v0, 10
syscall