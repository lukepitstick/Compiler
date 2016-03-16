.data
x: .word 4
.text
main:
li $t1, 2
li $t2, 1
add $t0,$t1,$t2
li $t2, 3
sub $t0,$t0,$t2
li $t1, 6
li $t2, 5
add $t0,$t1,$t2
li $t2, 7
sub $t0,$t0,$t2
li $t1, 8
add $t0,$t1,$t0
add $t0,$t0,$t0
li $t1, 9
add $t0,$t1,$t0
la   $s0, x
sw   $t0, ($s0)

li   $v0, 10
syscall