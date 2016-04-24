.data
False: .asciiz "False"
True: .asciiz "True"
stringtmptmp0: .asciiz "Here\n"

.text
main:
li $s6, 1
blez $s6, L1
li $s7, 1
blez $s7, L3
li $s4, 1
li $s5, 0
or $s4, $s4, $s5
blez $s4, L5
li $s5, 1
li $s2, 1
or $s5, $s5, $s2
blez $s5, L7
li $s2, 1
li $s3, 0
li $s1, 0
and $s3, $s3, $s1
or $s2, $s2, $s3
blez $s2, L9
la $a0, stringtmptmp0
li $v0, 4
syscall

L9: nop
L7: nop
L5: nop
L3: nop
L1: nop
li   $v0, 10
syscall