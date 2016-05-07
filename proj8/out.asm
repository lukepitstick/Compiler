.data
False: .asciiz "False"
True: .asciiz "True"
t: .word 4
ref-x: .word 4
y: .word 4
z: .word 4
stringtmptmp0: .asciiz "main: "
stringtmptmp1: .asciiz "\n"
stringtmptmp2: .asciiz "main: "
stringtmptmp3: .asciiz "\n"
stringtmptmp4: .asciiz "main: "
stringtmptmp5: .asciiz "\n"
.text
main:
li $v0, 5
syscall
la $t0, ref-x
sw $v0, 0($t0)

la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, ref-x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall

la $a0, stringtmptmp2
li $v0, 4
syscall

la $s0, ref-x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp3
li $v0, 4
syscall

la $a0, stringtmptmp4
li $v0, 4
syscall

la $s0, ref-x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp5
li $v0, 4
syscall

