.data
False: .asciiz "False"
True: .asciiz "True"
stringtmptmp0: .asciiz "Here\n"

.text
main:
li $t2, 1
blez $t2, L1
li $t5, 1
blez $t5, L3
li $s1, 1
li $s6, 0
or $s1, $s1, $s6
blez $s1, L5
li $s6, 1
li $t0, 1
or $s6, $s6, $t0
blez $s6, L7
li $t0, 1
li $t4, 0
li $s7, 0
and $t4, $t4, $s7
or $t0, $t0, $t4
blez $t0, L9
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