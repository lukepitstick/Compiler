.text
.global GetIP

GetIP:
move $a0, $ra
li $v0, 1
syscall