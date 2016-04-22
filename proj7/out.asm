.data
False: .asciiz "False"
True: .asciiz "True"
s: .word 4
b: .word 4

.text
main:
li $s3, 0
la   $s0, s
sw $s3, ($s0)

la $s0, s
lw $s3, ($s0)
la   $s0, b
sw $s3, ($s0)

la $s0, b
lw $s3, ($s0)
la $s0, False
la $s1, True
movn $a0,$s1,$s3
movz $a0,$s0,$s3
li $v0, 4
syscall
li   $v0, 10
syscall