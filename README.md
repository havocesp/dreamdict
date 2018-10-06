# DreamDict

Just a Dict like class enhanced with some "magic" methods.

## Installation

Install through **pip** (directly from github)

```bash
$ pip install git+https://github.com/havocesp/dreamdict.git
```

## Usage

Create object when you need them.

```python
from dreamdict import DreamDict

dd = DreamDict(item='book', value=13.50)

print("{data.value:.2f} {data.item}".format(data=dd))
# Book 13.50
```

### Explicit Mode

By default the explicit is OFF.

That means if you try to get a value that doesn't exists, a AttributeError get raised.

```python
dd = DreamDict(item="book")
# price does not exist
print(dd.price)

# AttributeError: Property 'age' not found"
```

Now when you try to access a property that doesn't exists, `None` get returned.

You can turn the explicit mode ON, by:

```python
dd = DreamDict(strict=False)
dd.price = 13.50
dd.item = "book"

print('{}: {:.2f} EUR'.format(dd.item, dd.price))
# book: 13.50 EUR
```

## Changelog

### 0.1.0

 - Initial version.

## TODO
 - Add more util methods.
