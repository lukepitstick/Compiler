.data
x: .word 4
.text
main:
li $t1, 2
li $t2, 1
add $t0,$t1,$t2
li $t1, 2
add $t0,$t1,$t0
li $t1, 3
add $t0,$t1,$t0
li $t1, 4
add $t0,$t1,$t0
li $t1, 5
add $t0,$t1,$t0
li $t1, 6
add $t0,$t1,$t0
li $t1, 7
add $t0,$t1,$t0
li $t1, 8
add $t0,$t1,$t0
li $t1, 9
add $t0,$t1,$t0
li $t1, 10
add $t0,$t1,$t0
la   $s0, x
sw   $t0, ($s0)

li   $v0, 10
syscall