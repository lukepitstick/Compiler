.data
False: .asciiz "False"
True: .asciiz "True"
b: .word 4
stringtmptmp0: .asciiz "First level"
stringtmptmp1: .asciiz "Second level"
stringtmptmp2: .asciiz "Thrid level"
stringtmptmp3: .asciiz "Fourth level"
stringtmptmp4: .asciiz "Exit fourth level"
stringtmptmp5: .asciiz "Exit third level"
stringtmptmp6: .asciiz "Exit second level"
stringtmptmp7: .asciiz "Exit first level"
stringtmptmp8: .asciiz "The program ended successfully!@#%#!@^$@#^"

.text
main:
li $t7, 1
la   $s0, b
sw $t7, ($s0)

la $s0, b
lw $s2, ($s0)
blez $s2, L1
la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, b
lw $t7, ($s0)
blez $t7, L3
la $a0, stringtmptmp1
li $v0, 4
syscall

la $s0, b
lw $t7, ($s0)
blez $t7, L5
la $a0, stringtmptmp2
li $v0, 4
syscall

la $s0, b
lw $t7, ($s0)
blez $t7, L7
la $a0, stringtmptmp3
li $v0, 4
syscall

la $a0, stringtmptmp4
li $v0, 4
syscall

L7: nop
la $a0, stringtmptmp5
li $v0, 4
syscall

L5: nop
la $a0, stringtmptmp6
li $v0, 4
syscall

L3: nop
la $a0, stringtmptmp7
li $v0, 4
syscall

L1: nop
la $a0, stringtmptmp8
li $v0, 4
syscall

li   $v0, 10
syscall