# UTF-8 Validation

This project provides a function to determine if a given data set represents a valid UTF-8 encoding.

## Function

### `validUTF8(data)`

Determines if a given data set represents a valid UTF-8 encoding.

- **Parameters:**
  - `data` (list of int): A list of integers representing the data set, where each integer represents a byte (only the 8 least significant bits are considered).

- **Returns:**
  - `bool`: True if the data set is a valid UTF-8 encoding, False otherwise.

## Examples

```python
>>> validUTF8([65])
True

>>> validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33])
True

>>> validUTF8([229, 65, 127, 256])
False
