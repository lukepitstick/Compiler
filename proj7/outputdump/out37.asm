.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t5, 5
li $t7, 10
sgt $t5, $t5, $t7
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 5
li $t7, 5
sgt $t5, $t5, $t7
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li $t5, 5
li $t7, 0
sgt $t5, $t5, $t7
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li   $v0, 10
syscall