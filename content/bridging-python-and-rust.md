+++
title = "Bridging Python & Rust: A Walkthrough of using Py03"
date = 2025-05-18
updated = 2025-08-30
description = "A practical guide to exposing Rust functions to Python using PyO3."

[taxonomies]
tags = ["rust", "python", "py03"]
+++

- [Bridging Python and Rust: A Practical Guide with PyO3](#bridging-python-and-rust-a-practical-guide-with-pyo3)
- [Project Structure](#project-structure)
- [Step 1: Exposing Rust Functions with PyO3](#step-1-exposing-rust-functions-with-pyo3)
- [Step 2: Building and Packaging](#step-2-building-and-packaging)
- [Step 3: Using the Library from Python](#step-3-using-the-library-from-python)
- [Step 4: Handling Errors](#step-4-handling-errors)
- [Wrapping Up](#wrapping-up)

# Bridging Python and Rust: A Practical Guide with PyO3

Sometimes Python just isn't fast enough, or you want to reuse some Rust code without rewriting it. [PyO3](https://pyo3.rs) makes it surprisingly easy to call Rust from Python (or less commonly vice-versa). Here’s how I created [pngme-python][1] crate, to expose my already existing [pngme][2] Rust crate as a python library.

## Project Structure

```
pngme/
├── src/
│   └── lib.rs
├── Cargo.toml
pngme-python/
├── src/
│   └── lib.rs
├── tests/
│   └── test_pngme.py
├── Cargo.toml
├── pyproject.toml
├── README.md
```

- **pngme/src/lib.rs**: The original Rust code with PNG manipulation functionality, that we want to expose as a Python library
- **pngme-python/src/lib.rs**: The Py03 bindings.
- **test_pngme.py**: Python tests to verify the bindings work correctly
- **pngme-python/src/Cargo.toml**: The build configuration for the Rust portion of the Py03/Maturin build process.
- **pyproject.toml**: Python packaging configuration for Maturin

## Step 1: Exposing Rust Functions with PyO3

PyO3 lets you turn Rust functions into Python-callable methods with minimal fuss. Here’s a trimmed-down version of the `encode`, `decode`, and `remove` functions from [src/lib.rs](https://github.com/sinon/pngme/blob/main/crates/pngme-python/src/lib.rs):

```rust

use pyo3::prelude::*;

#[pymodule]
#[pyo3(name = "pngme")]
mod pngme_python {
    use pyo3::exceptions::{PyFileNotFoundError, PyIOError, PyValueError};
    use pyo3::{prelude::*, PyResult};
    use std::path::PathBuf;

    use pngme_lib::{decode as png_decode, encode as png_encode, remove as png_remove, Error};

    #[pyfunction]
    pub fn encode(path: PathBuf, chunk_type: String, message: String) -> PyResult<()> {
        let result = png_encode(&path, &chunk_type, message);
        match result {
            Ok(_) => Ok(()),
            Err(e) => match e {
                Error::FileNotFound { .. } => Err(PyFileNotFoundError::new_err(e.to_string())),
                Error::Read { source: s } => Err(PyIOError::new_err(s.to_string())),
                Error::PNGParse => Err(PyValueError::new_err(e.to_string())),
                Error::InvalidChunkType { source: s, .. } => Err(PyValueError::new_err(s.to_string())),
                Error::PNGWrite { .. } => Err(PyValueError::new_err(e.to_string())),
                Error::ChunkNotFound { .. } => Err(PyValueError::new_err(e.to_string())),
                Error::StrConversion => Err(PyValueError::new_err(e.to_string())),
            },
        }
    }

    #[pyfunction]
    pub fn decode(path: PathBuf, chunk_type: String) -> PyResult<String> {
        let result = png_decode(&path, &chunk_type);
        match result {
            Ok(msg) => Ok(msg),
            Err(e) => match e {
                Error::FileNotFound { .. } => Err(PyFileNotFoundError::new_err(e.to_string())),
                Error::Read { .. } => Err(PyIOError::new_err(e.to_string())),
                Error::PNGParse => Err(PyValueError::new_err(e.to_string())),
                Error::InvalidChunkType { source: s, .. } => Err(PyValueError::new_err(s.to_string())),
                Error::PNGWrite { .. } => Err(PyValueError::new_err(e.to_string())),
                Error::ChunkNotFound { .. } => Err(PyValueError::new_err(e.to_string())),
                Error::StrConversion => Err(PyValueError::new_err(e.to_string())),
            },
        }
    }

    #[pyfunction]
    pub fn remove(path: PathBuf, chunk_type: String) -> PyResult<()> {
        let result = png_remove(&path, &chunk_type);
        match result {
            Ok(_) => Ok(()),
            Err(e) => match e {
                Error::FileNotFound { .. } => Err(PyFileNotFoundError::new_err(e.to_string())),
                Error::Read { .. } => Err(PyIOError::new_err(e.to_string())),
                Error::PNGParse => Err(PyValueError::new_err(e.to_string())),
                Error::InvalidChunkType { source: s, .. } => Err(PyValueError::new_err(s.to_string())),
                Error::PNGWrite { .. } => Err(PyValueError::new_err(e.to_string())),
                Error::ChunkNotFound { .. } => Err(PyValueError::new_err(e.to_string())),
                Error::StrConversion => Err(PyValueError::new_err(e.to_string())),
            },
        }
    }
}
```

The key parts of this implementation:

- The `#[pymodule]` macro creates a Python module from the Rust module it encloses.
- Each `#[pyfunction]` within the Rust module adds a Rust function to Python the `#[pymodule]`.
- Each Rust error type must be handled and mapped to the appropriate Python exceptions.

## Step 2: Building and Packaging

[Maturin](https://github.com/PyO3/maturin) handles compiling the Rust code and packaging it as a Python wheel. Two configuration files control this process:

**Cargo.toml**
```toml
[package]
name = "pngme-python"
version = "0.1.0"
edition = "2021"

[lib]
name = "pngme"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.18.3", features = ["extension-module"] }
pngme-lib = { path = "../pngme" }
```

**pyproject.toml**
```toml
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"

[project]
name = "pngme"
version = "0.1.0"
description = "Python bindings for pngme"
readme = "README.md"

[tool.maturin]
features = ["pyo3/extension-module"]
```

Building is as simple as:

```bash
maturin develop
```

This creates a Python wheel that you can use directly or publish to PyPI.

## Step 3: Using the Library from Python

Once built, and installed, just import and use the module in Python. An example can be found in [tests/test_pngme.py](https://github.com/sinon/pngme/blob/main/crates/pngme-python/tests/test_pngme.py):

```python

import pngme

def test_pngme_encode():
    file_location = "./crates/pngme-python/tests/dice.png"
    pngme.encode(file_location, "ruSt", "some message")
    output = pngme.decode(file_location, "ruSt")
    assert output == "some message"
    pngme.remove(file_location, "ruSt")
    nothing = pngme.decode(file_location, "ruSt")
    assert nothing == "No secret message found"
```

## Step 4: Handling Errors

PyO3 lets you map Rust errors to Python exceptions, so Python users get idiomatic error messages as shown below:

```python
import pytest

def test_pngme_unknown_file():
    with pytest.raises(FileNotFoundError) as exc:
        pngme.encode("unknown.png", "ruSt", "some message")
    assert 'File not found "unknown.png"' in str(exc.value)
```

## Wrapping Up

PyO3 makes it easy to bring Rust’s speed and safety to Python, with natural error handling and a smooth workflow. If you want to squeeze more performance out of Python or reuse Rust code, give it a try.

---

**References:**
- [PyO3 Documentation](https://pyo3.rs)
- [Maturin Documentation](https://maturin.rs)
- [pngme-python Source Code](https://github.com/sinon/pngme/tree/main/crates/pngme-python)

[1]: https://github.com/sinon/pngme/tree/main/crates/pngme-python
[2]: https://github.com/sinon/pngme/tree/main/crates/pngme