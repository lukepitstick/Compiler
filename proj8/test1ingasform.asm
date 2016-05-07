
test1.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <foo>:
// Test whether you can handle basic function.
// Note: you are not required to have a void type.  (Acceptable
// to just return an int and ignore it.)
#include <stdio.h>

void foo() {
   0:	55                   	push   %rbp
   1:	48 89 e5             	mov    %rsp,%rbp
   4:	48 83 ec 10          	sub    $0x10,%rsp
  int i = 0;
   8:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
  i = i + 1;
   f:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
  printf("In foo: %d.\n", i);
  13:	8b 45 fc             	mov    -0x4(%rbp),%eax
  16:	89 c6                	mov    %eax,%esi
  18:	bf 00 00 00 00       	mov    $0x0,%edi
  1d:	b8 00 00 00 00       	mov    $0x0,%eax
  22:	e8 00 00 00 00       	callq  27 <foo+0x27>
}
  27:	90                   	nop
  28:	c9                   	leaveq 
  29:	c3                   	retq   

000000000000002a <foo2>:

void foo2() {
  2a:	55                   	push   %rbp
  2b:	48 89 e5             	mov    %rsp,%rbp
  printf("In foo2.\n");
  2e:	bf 00 00 00 00       	mov    $0x0,%edi
  33:	e8 00 00 00 00       	callq  38 <foo2+0xe>
}
  38:	90                   	nop
  39:	5d                   	pop    %rbp
  3a:	c3                   	retq   

000000000000003b <main>:

int main() {
  3b:	55                   	push   %rbp
  3c:	48 89 e5             	mov    %rsp,%rbp
  printf("In main.\n");
  3f:	bf 00 00 00 00       	mov    $0x0,%edi
  44:	e8 00 00 00 00       	callq  49 <main+0xe>
  foo();
  49:	b8 00 00 00 00       	mov    $0x0,%eax
  4e:	e8 00 00 00 00       	callq  53 <main+0x18>
  printf("Returned to main.\n");
  53:	bf 00 00 00 00       	mov    $0x0,%edi
  58:	e8 00 00 00 00       	callq  5d <main+0x22>
  foo();
  5d:	b8 00 00 00 00       	mov    $0x0,%eax
  62:	e8 00 00 00 00       	callq  67 <main+0x2c>
  printf("Returned to main. (Again.)\n");
  67:	bf 00 00 00 00       	mov    $0x0,%edi
  6c:	e8 00 00 00 00       	callq  71 <main+0x36>
  foo2();
  71:	b8 00 00 00 00       	mov    $0x0,%eax
  76:	e8 00 00 00 00       	callq  7b <main+0x40>
  printf("Returned to main.\n");
  7b:	bf 00 00 00 00       	mov    $0x0,%edi
  80:	e8 00 00 00 00       	callq  85 <main+0x4a>

  return 0;  // You are not required to provide for a return value
  85:	b8 00 00 00 00       	mov    $0x0,%eax
             // in your main function (assuming you have a main
             // function).
}
  8a:	5d                   	pop    %rbp
  8b:	c3                   	retq   
