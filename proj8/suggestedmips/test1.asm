.data
inmain: .asciiz "In main.\n"
returned: .asciiz "Returned to main.\n"
returned2: .asciiz "Returned to main. (Again.)\n"
foostring: .asciiz "In foo: %d.\n" ;Do we need formatted string?
foostring2: .asciiz "In foo2.\n"

.text
main:
la $a0, inmain
li $v0, 4
syscall

;before calling j foo
;we need to get the current stack pointer
;so that the function or subroutine can
;return after it ends

;j foo

la $a0, returned
li $v0, 4
syscall

;j foo2

la $a0, returned2
li $v0, 4
syscall

;j foo

la $a0, returned
li $v0, 4
syscall

li $v0, 10
syscall
