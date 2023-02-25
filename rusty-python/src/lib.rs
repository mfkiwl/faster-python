use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod logger;

#[pyfunction]
fn say_hello(name: &str) {
    println!("Hello there {name}!");
}

#[pyfunction]
fn fib(n: i32) -> i32 {
    if n == 0 || n == 1 {
        return n;
    } else{
        return fib(n-2) + fib(n-1)
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn rusty_python(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(say_hello, m)?)?;
    m.add_function(wrap_pyfunction!(fib, m)?)?;
    Ok(())
}
