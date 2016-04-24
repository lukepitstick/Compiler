.data
False: .asciiz "False"
True: .asciiz "True"

.text
main:
li $s4, 1
li $t0, 2
li $s2, 3
li $t1, 4
li $t3, 5
li $t7, 6
li $s6, 7
li $s3, 8
li $t5, 9
add $s3, $s3, $t5
add $s6, $s6, $s3
add $t7, $t7, $s6
add $t3, $t3, $t7
add $t1, $t1, $t3
add $s2, $s2, $t1
add $t0, $t0, $s2
add $s4, $s4, $t0
add $a0, $s4,0
li $v0, 1
syscall

li   $v0, 10
syscall