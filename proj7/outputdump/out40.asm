.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 5
li $t2, 5
sne $s4, $s4, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$s4
movz $a0,$s0,$s4
li $v0, 4
syscall
li $s4, 5
li $t2, 10
sne $s4, $s4, $t2
la $s0, False
la $s1, True
movn $a0,$s1,$s4
movz $a0,$s0,$s4
li $v0, 4
syscall
li   $v0, 10
syscall