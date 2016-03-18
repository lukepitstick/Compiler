.data
a: .word 4
c: .word 4
b: .word 4
e: .word 4
d: .word 4
f: .word 4
.text
main:
li $t1, 2
li $t2, 1
add $t0,$t1,$t2
li $t2, 3
sub $t0,$t0,$t2
la   $s0, a
sw   $t0, ($s0)

la $s0, a
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li $t1, 2
li $t2, 1
add $t0,$t1,$t2
li $t2, 3
sub $t0,$t0,$t2
la   $s0, b
sw   $t0, ($s0)

la $s0, b
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li $t1, 2
li $t2, 3
sub $t0,$t1,$t2
li $t2, 1
add $t0,$t0,$t2
la   $s0, c
sw   $t0, ($s0)

la $s0, c
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li $t1, 1
li $t2, 2
sub $t0,$t1,$t2
li $t1, 3
add $t0,$t1,$t0
la   $s0, d
sw   $t0, ($s0)

la $s0, d
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li $t1, 1
li $t2, 2
sub $t0,$t1,$t2
li $t1, 3
add $t0,$t1,$t0
la   $s0, e
sw   $t0, ($s0)

la $s0, e
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li $t1, 3
li $t2, 2
add $t0,$t1,$t2
li $t1, 1
sub $t0,$t1,$t0
la   $s0, f
sw   $t0, ($s0)

la $s0, f
lw $t0, ($s0)
add $a0, $t0,0
li $v0, 1
syscall

li   $v0, 10
syscall