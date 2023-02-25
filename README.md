# fastor-python

Rust is so fast, and python can leverage power of rust.

By the way, you know, python is too slow ??

## Usage

```bash
$ python main.py --fibonacci 40

python main.py --fibonacci 40
python                : 22.503003358004207
python(numba)         : 0.8012343700029305
python(numba-nopython): 0.7329909489999409
python(cython)        : 0.6923800079966895
c++(nanobind)         : 0.6267670020024525
rust(pyo3)            : 0.2173983950051479
```

## Setup

* How to start poetry project
  * `$ poetry init -q`
* How to use nanobind
  * `cmake -S . -B build`
  * `cmake --build build`
* How to use pyo3
  * `$ poetry add maturin`
  * `$ poetry run maturin new -b pyo3 rusty-python`
  * `$ cd rusty-python`
  * edit src/lib.rs
  * and back to base directory of poetry
  * `poetry add ./rusty-python/`

## Reference

* [pyo3](https://betterprogramming.pub/improving-python-with-rust-ed12bffd2ca4)
* [numba](https://numba.pydata.org/numba-doc/latest/user/5minguide.html)
* [cython](https://www.infoworld.com/article/3648539/faster-python-made-easier-with-cythons-pure-python-mode.html)
* [nanobind](https://nanobind.readthedocs.io/en/latest/index.html)
