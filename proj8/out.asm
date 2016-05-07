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

la $a0, stringtmptmp4
li $v0, 4
syscall

la $a0, stringtmptmp5
li $v0, 4
syscall

la $a0, stringtmptmp6
li $v0, 4
syscall



func4:
la $a0, stringtmptmp0
li $v0, 4
syscall

la $s0, i
lw $s3, ($s0)
add $a0, $s3,0
li $v0, 1
syscall

la $a0, stringtmptmp1
li $v0, 4
syscall



func3:
la $s0, i
lw $s3, ($s0)
li $t0, 1
add $s3, $s3, $t0
la   $s0, i
sw $s3, ($s0)



func2:
li $s3, 0
la   $s0, i
sw $s3, ($s0)



func5:
la $a0, stringtmptmp2
li $v0, 4
syscall

