.data
False: .asciiz "False"
True: .asciiz "True"
x: .word 4
stringtmptmp0: .asciiz "hey !@#$%^&*()_+-=`~;:'/?,.<>|   "

.text
main:
li $t1, 7
la   $s0, x
sw $t1, ($s0)

la $s0, x
lw $t1, ($s0)
li $t5, 2
rem $t1, $t1, $t5
la   $s0, x
sw $t1, ($s0)

la $s0, x
lw $t1, ($s0)
add $a0, $t1,0
li $v0, 1
syscall

li $t1, 1
li $t5, 0
or $t1, $t1, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t1
movz $a0,$s0,$t1
li $v0, 4
syscall
li $t1, 2
li $t5, 1
sne $t1, $t1, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t1
movz $a0,$s0,$t1
li $v0, 4
syscall
li $t1, 2
li $t5, 1
slt $t1, $t1, $t5
la $s0, False
la $s1, True
movn $a0,$s1,$t1
movz $a0,$s0,$t1
li $v0, 4
syscall
la $a0, stringtmptmp0
li $v0, 4
syscall

li   $v0, 10
syscall