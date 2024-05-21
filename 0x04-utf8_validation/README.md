# UTF-8 Validation

This script provides a function to determine if a given data set represents a valid UTF-8 encoding.

## Function

### `validUTF8(data)`

Determines if a given data set represents a valid UTF-8 encoding.

- **Parameters:**
  - `data` (list of int): A list of integers representing the data set, where each integer represents a byte (only the 8 least significant bits are considered).

- **Returns:**
  - `bool`: True if the data set is a valid UTF-8 encoding, False otherwise.

### Encoding Rules
UTF-8 encoding can be from 1 to 4 bytes long. The encoding rules are:
- 1-byte character: 0xxxxxxx
- 2-byte character: 110xxxxx 10xxxxxx
- 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
- 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

### Examples

```python
>>> validUTF8([65])
True

>>> validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32,
               99, 111, 111, 108, 33])
True

>>> validUTF8([229, 65, 127, 256])
False
