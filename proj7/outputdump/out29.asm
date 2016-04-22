.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s7, 1
li $s3, 1
or $s7, $s7, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 1
li $s3, 0
or $s7, $s7, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 0
li $s3, 1
or $s7, $s7, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li $s7, 0
li $s3, 0
or $s7, $s7, $s3
la $s0, False
la $s1, True
movn $a0,$s1,$s7
movz $a0,$s0,$s7
li $v0, 4
syscall
li   $v0, 10
syscall