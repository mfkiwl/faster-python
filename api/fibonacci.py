import numba
import cython
import rusty_python as rp
import build.my_ext as cp
from time import perf_counter


def fib_calc(val: int) -> None:
    # base
    start_time = perf_counter()
    fibBase(val)
    print("python                :", perf_counter() - start_time)
    # numba
    start_time = perf_counter()
    fibNumba(val)
    print("python(numba)         :", perf_counter() - start_time)
    # numba-nopython
    start_time = perf_counter()
    fibNumbaNoPython(val)
    print("python(numba-nopython):", perf_counter() - start_time)
    # cython
    start_time = perf_counter()
    fibCython(val)
    print("python(cython)        :", perf_counter() - start_time)
    # c++
    start_time = perf_counter()
    cp.fib(val)
    print("c++(nanobind)         :", perf_counter() - start_time)
    # rust
    start_time = perf_counter()
    rp.fib(val)
    print("rust(pyo3)            :", perf_counter() - start_time)


def fibBase(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibBase(n-2) + fibBase(n-1)


@numba.jit
def fibNumba(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibNumba(n-2) + fibNumba(n-1)


@numba.jit(nopython=True)
def fibNumbaNoPython(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibNumba(n-2) + fibNumba(n-1)


@cython.cfunc
def fibCython(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibNumba(n-2) + fibNumba(n-1)

