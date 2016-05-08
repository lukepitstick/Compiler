.data
False: .asciiz "False"
True: .asciiz "True"
i: .word 4
stringtmptmp0: .asciiz "In foo: "
stringtmptmp1: .asciiz ".\n"
stringtmptmp2: .asciiz "In foo2.\n"
stringtmptmp3: .asciiz "In main.\n"
stringtmptmp4: .asciiz "Returned to main.\n"
stringtmptmp5: .asciiz "Returned to man. (Again.)\n"
stringtmptmp6: .asciiz "Returned to main.\n"


.text
main:
la $a0, stringtmptmp3
li $v0, 4
syscall

j func3

la $a0, stringtmptmp4
li $v0, 4
syscall

j func2

la $a0, stringtmptmp5
li $v0, 4
syscall

j func5

la $a0, stringtmptmp6
li $v0, 4
syscall


j close


func3:
la $s0, i
lw $t0, ($s0)
li $t1, 1
add $t0, $t0, $t1
la   $s0, i
sw $t0, ($s0)



func5:
la $a0, stringtmptmp2
li $v0, 4
syscall



func4:
la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, i
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall



func2:
li $t0, 0
la   $s0, i
sw $t0, ($s0)


close:
li $v0, 10
syscall
