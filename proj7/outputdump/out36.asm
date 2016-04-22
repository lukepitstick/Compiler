.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $t2, 5
li $s3, 10
sle $t2, $t2, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$t2
movz $a0,$s0,$t2
li $v0, 4
syscall
li $t2, 5
li $s3, 5
sle $t2, $t2, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$t2
movz $a0,$s0,$t2
li $v0, 4
syscall
li $t2, 5
li $s3, 0
sle $t2, $t2, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$t2
movz $a0,$s0,$t2
li $v0, 4
syscall
li   $v0, 10
syscall