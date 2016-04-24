.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 1
li $s2, 1
or $s4, $s4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$s4
movz $a0,$s0,$s4
li $v0, 4
syscall
li $s4, 1
li $s2, 0
and $s4, $s4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$s4
movz $a0,$s0,$s4
li $v0, 4
syscall
li $s4, 0
li $s2, 1
or $s4, $s4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$s4
movz $a0,$s0,$s4
li $v0, 4
syscall
li $s4, 0
li $s2, 0
and $s4, $s4, $s2
la $s0, False
la $s1, True
movn $a0,$s1,$s4
movz $a0,$s0,$s4
li $v0, 4
syscall
li   $v0, 10
syscall