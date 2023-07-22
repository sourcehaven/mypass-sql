## SQL language for MyPass

This README explains how this project is put together, 
what are the main ideas, considerations.
I highly recommend reading this if you are planning to work on this code.

### Project layout

Every package contains `tokens.py` and `parser.py`

1. **tokens.py**

Defines individual tokens and their corresponding
pattern matching **function** or **variable** with a `t_` prefix.

2. **parser.py**

Contains the grammar (production functions). 

**NOTE:** Make sure to import the **tokens** collection from the `tokens.py` module.
It is required for PLY and it must be called **tokens**, otherwise you will get an error!

#### Example:
```python
# parser.py

from .tokens import tokens

def p_func1(p):
    """
    ... : ...
        | ...
    """
    p[0] = ...

# rest of the code ...
```