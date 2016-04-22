.data
False: .asciiz "False"
True: .asciiz "True"
b: .word 4
s: .word 4

.text
main:
li $s6, 0
la   $s0, s
sw $s6, ($s0)

la $s0, s
lw $s6, ($s0)
la   $s0, b
sw $s6, ($s0)

la $s0, b
lw $s6, ($s0)
la $s0, False
la $s1, True
movn $a0,$s1,$s6
movz $a0,$s0,$s6
li $v0, 4
syscall
li   $v0, 10
syscall