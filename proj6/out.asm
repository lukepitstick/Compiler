.data
False: .asciiz "False"
True: .asciiz "True"
b: .word 4
s: .word 4

.text
main:
li $t8, 0
la   $s0, s
sw $t8, ($s0)

la $s0, s
lw $t8, ($s0)
la   $s0, b
sw $t8, ($s0)

la $s0, b
lw $t8, ($s0)
la $s0, False
la $s1, True
movn $a0,$s1,$t8
movz $a0,$s0,$t8
li $v0, 4
syscall
li   $v0, 10
syscall