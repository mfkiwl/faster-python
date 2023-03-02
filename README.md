# faster-python

Rust is so fast, and python can leverage power of rust.

By the way, you know, python is too slow ??

> This is not what proves that rust is better than cpp.  
> Apparently, cpp(nanobind) is able to become even faster.  
> 
> [link](https://github.com/terib0l/faster-python/issues/1)

## Usage

```bash
$ git clone <repo> && cd <repo>
$ poetry install
$ poetry shell
$ cmake -S . -B build
$ cmake --build build

#############
# benchmark #
#############
$ python main.py --fibonacci 40

python                : 21.961166224995395
python(numba)         : 0.7921977119985968
python(numba-nopython): 0.7205598769942299
python(cython)        : 0.6859547469939571
c++(nanobind)         : 0.3306063709896989
rust(pyo3)            : 0.21601284098869655
```

## How to make each of python bindings

* How to use nanobind
  * `$ pip install nanobind`
  * edit CMakeLists.txt
  * edit <file_name>.cpp
  * `$ cmake -S . -B build`
  * `$ cmake --build build`
* How to use pyo3
  * `$ pip install maturin`
  * `$ maturin new -b pyo3 rusty-python`
  * `$ cd rusty-python`
  * edit src/lib.rs
  * and back to base directory of poetry
  * `$ pip install ./rusty-python/`

## Other ways to make python faster

> First of all, you need to identify bottlenecks using either of ways which cProfile, time.perfcounter(), %%timeit.

* improve time-complexity in terms of Big O Notation
* use multi thread or process
* use PyPy

## Reference

* [pyo3](https://betterprogramming.pub/improving-python-with-rust-ed12bffd2ca4)
* [numba](https://numba.pydata.org/numba-doc/latest/user/5minguide.html)
* [cython](https://www.infoworld.com/article/3648539/faster-python-made-easier-with-cythons-pure-python-mode.html)
* [nanobind](https://nanobind.readthedocs.io/en/latest/index.html)
