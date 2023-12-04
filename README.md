# decoratorsutility

## Introduction
This Python package provides decorators to handle exceptions, measure execution time, and set timeouts.

## Installation
To install decoratorsutility, simply use pip:

```bash
pip install decoratorsutility

```

## Usage Example

### `exception_dec`

Decorator to handle exceptions by logging errors to a specified file path.

```python
@exception_dec('module_name', '/path/to/logfile.log')
def function_name(*args, **kwargs):
    try:
        # Function execution
        return func(*args, **kwargs)
    except Exception as err:
        # Logs the error to the specified file path
        log_error(module=exc_mod, file_path=exc_path, error=err)
        logging.error(err)
```

### `repeat_on_error`

Decorator to retry function execution a set number of times in case of exceptions.

```python
@repeat_on_error(max_try=3, error_log='log/logfile.log', show_error=True)
def test_dummy(arg1:int):
    return arg1/0
```

### `timeout_decorator`

Decorator to set a timeout for a function.

```python
from decoratorsutility.decorators import timeout_decorator

@timeout_decorator(timeout=5)
def my_function():
    time.sleep(6)  # Simulate a long-running function
    return "Success!"
```


## Documentation
The Sphinx-generated documentation for PathUtils can be found [here](https://anglisanosa.github.io/decoratorsutility/).

## Contribution
Feel free to contribute by submitting issues [here](https://github.com/anglisanosa/decoratorsutility/issues).



