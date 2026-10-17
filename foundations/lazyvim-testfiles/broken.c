/* Deliberately broken: the missing semicolon below is the point.
   F5 should show a compiler error and run nothing. */
#include <stdio.h>

int main() {
  puts("This line never runs")
  return 0;
}
