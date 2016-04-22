.data
False: .asciiz "False"
True: .asciiz "True"
s: .word 4
b: .word 4

.text
main:
li $t9, 0
la   $s0, s
sw $t9, ($s0)

la $s0, s
lw $t9, ($s0)
la   $s0, b
sw $t9, ($s0)

la $s0, b
lw $t9, ($s0)
la $s0, False
la $s1, True
movn $a0,$s1,$t9
movz $a0,$s0,$t9
li $v0, 4
syscall
li   $v0, 10
syscall