.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t6, 5
li $t3, 10
sgt $t6, $t6, $t3
la $s0, False
la $s1, True
movn $a0,$s1,$t6
movz $a0,$s0,$t6
li $v0, 4
syscall
li $t6, 5
li $t3, 5
sgt $t6, $t6, $t3
la $s0, False
la $s1, True
movn $a0,$s1,$t6
movz $a0,$s0,$t6
li $v0, 4
syscall
li $t6, 5
li $t3, 0
sgt $t6, $t6, $t3
la $s0, False
la $s1, True
movn $a0,$s1,$t6
movz $a0,$s0,$t6
li $v0, 4
syscall
li   $v0, 10
syscall