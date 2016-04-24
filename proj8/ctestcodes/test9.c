// Complex pass by reference
#include <stdio.h>

int foo(int* x, int* y) {
  *x = *x + 1;
  *y = *y + 1;
  return *x + *y;
}

int main() {
  int a = 0;
  int c = 3;
  int b = foo(&a, &c);
  printf("%d\t%d\n", a, b);

  return 0;
}
