.data
x: .word 4
.text
main:
li $t1, 10
li $t2, 5
add $t0,$t1,$t2
li $t2, 20
sub $t0,$t0,$t2
li $t1, 40
li $t2, 30
add $t0,$t1,$t2
sub $t0,$t0,$t0
la   $s0, x
sw   $t0, ($s0)

li   $v0, 10
syscall