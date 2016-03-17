.data
x: .word 4
aa: .word 4
z: .word 4
ab: .word 4
y: .word 4
.text
main:
li $t0, 4
la   $s0, x
sw   $t0, ($s0)

li $t1, 5
la $s0, x
lw $t2, ($s0)
add $t0,$t1,$t2
la   $s0, y
sw   $t0, ($s0)

la $s0, y
lw $t1, ($s0)
la $s0, x
lw $t2, ($s0)
add $t0,$t1,$t2
li $t1, 6
add $t0,$t1,$t0
la   $s0, z
sw   $t0, ($s0)

la $s0, y
lw $t1, ($s0)
la $s0, x
lw $t2, ($s0)
add $t0,$t1,$t2
la $s0, z
lw $t1, ($s0)
add $t0,$t1,$t0
li $t1, 7
add $t0,$t1,$t0
la   $s0, aa
sw   $t0, ($s0)

la $s0, y
lw $t1, ($s0)
la $s0, x
lw $t2, ($s0)
add $t0,$t1,$t2
la $s0, z
lw $t1, ($s0)
add $t0,$t1,$t0
la $s0, aa
lw $t1, ($s0)
add $t0,$t1,$t0
li $t1, 8
add $t0,$t1,$t0
la   $s0, ab
sw   $t0, ($s0)

li   $v0, 10
syscall