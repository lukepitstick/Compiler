.data
False: .asciiz "False"
True: .asciiz "True"
y: .word 4
z: .word 4
x: .word 4
stringtmptmp0: .asciiz "foo1: "
stringtmptmp1: .asciiz "\n"
stringtmptmp2: .asciiz "foo2: "
stringtmptmp3: .asciiz "\n"
stringtmptmp4: .asciiz "foo3: "
stringtmptmp5: .asciiz "\n"
stringtmptmp6: .asciiz "foo4: "
stringtmptmp7: .asciiz "\n"
stringtmptmp8: .asciiz "main: "
stringtmptmp9: .asciiz "\n"
stringtmptmp10: .asciiz "main: "
stringtmptmp11: .asciiz "\n"


.text
main:
li $s2, 1
la   $s0, x
sw $s2, ($s0)

la $a0, stringtmptmp8
li $v0, 4
syscall

la $s0, x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp9
li $v0, 4
syscall

la $a0, stringtmptmp10
li $v0, 4
syscall

la $s0, x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp11
li $v0, 4
syscall


j close


func2:
li $s2, 3
la   $s0, z
sw $s2, ($s0)



func5:
li $s2, 2
la   $s0, y
sw $s2, ($s0)



func9:
li $s2, 3
la   $s0, x
sw $s2, ($s0)



func3:
la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, z
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall



func14:
la $a0, stringtmptmp6
li $v0, 4
syscall

la $s0, x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp7
li $v0, 4
syscall



func7:
la $a0, stringtmptmp2
li $v0, 4
syscall

la $s0, y
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp3
li $v0, 4
syscall



func10:
la $a0, stringtmptmp4
li $v0, 4
syscall

la $s0, x
lw $s2, ($s0)
add $a0, $s2,0
li $v0, 1
syscall

la $a0, stringtmptmp5
li $v0, 4
syscall



func12:
li $s2, 2
la   $s0, x
sw $s2, ($s0)


close:
li $v0, 10
syscall
