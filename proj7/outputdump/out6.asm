.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4

.text
main:
li $t5, 0
la   $s0, x
sw $t5, ($s0)

la $s0, x
lw $t5, ($s0)
la $s0, False
la $s1, True
movn $a0,$s1,$t5
movz $a0,$s0,$t5
li $v0, 4
syscall
li   $v0, 10
syscall