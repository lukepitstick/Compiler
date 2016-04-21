.data
False: .asciiz "False"
True: .asciiz "True"
s: .word 4
b: .word 4

.text
main:
li $t2, 0
la   $s0, s
sw $t2, ($s0)

la $s0, s
lw $t2, ($s0)
la   $s0, b
sw $t2, ($s0)

la $s0, b
lw $t2, ($s0)
la $s0, False
la $s1, True
movn $a0,$s1,$t2
movz $a0,$s0,$t2
li $v0, 4
syscall
li   $v0, 10
syscall