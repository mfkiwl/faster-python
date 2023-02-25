#include <nanobind/nanobind.h>

int fib(int n) {
  if (n == 0 || n == 1) {
    return n;
  } else {
    return fib(n-2) + fib(n-1);
  }
}

NB_MODULE(my_ext, m) {
  m.def("fib", &fib);
}
