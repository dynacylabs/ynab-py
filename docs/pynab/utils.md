# Utils



[Pynab Index](../README.md#pynab-index) / [Pynab](./index.md#pynab) / Utils

> Auto-generated documentation for [pynab.utils](../../pynab/utils.py) module.

- [Utils](#utils)
  - [CustomJsonEncoder](#customjsonencoder)
    - [CustomJsonEncoder().default](#customjsonencoder()default)
  - [_dict](#_dict)
    - [_dict().by](#_dict()by)
  - [http_utils](#http_utils)
    - [http_utils().delete](#http_utils()delete)
    - [http_utils().get](#http_utils()get)
    - [http_utils().patch](#http_utils()patch)
    - [http_utils().post](#http_utils()post)
    - [http_utils().put](#http_utils()put)

## CustomJsonEncoder

[Show source in utils.py:129](../../pynab/utils.py#L129)

#### Signature

```python
class CustomJsonEncoder(json.JSONEncoder): ...
```

### CustomJsonEncoder().default

[Show source in utils.py:130](../../pynab/utils.py#L130)

Returns the default JSON representation of an object.

#### Arguments

- `-` *obj* - The object to be serialized.

#### Returns

The JSON representation of the object.

#### Notes

- If the object is an instance of Enum, the value of the Enum is returned.
- If the object is an instance of datetime or date, the ISO formatted string representation is returned.
- For all other objects, the default JSONEncoder's default method is called.

#### Signature

```python
def default(self, obj): ...
```



## _dict

[Show source in utils.py:153](../../pynab/utils.py#L153)

A custom dictionary class that provides additional functionality.

This class extends the built-in `dict` class and adds a `by` method
for filtering the dictionary items based on a specific field and value.

#### Attributes

None

#### Methods

- `by(field` - str = "", value: object = None, first: bool = True) -> Union[object, _dict]:
    Filters the dictionary items based on the specified field and value.

#### Signature

```python
class _dict(dict): ...
```

### _dict().by

[Show source in utils.py:169](../../pynab/utils.py#L169)

Filters the dictionary items based on the specified field and value.

#### Arguments

- `field` *str* - The name of the field to filter on.
- `value` *object* - The value to filter for.
- `first` *bool* - If True, returns the first matching item. If False, returns a new dictionary with all matching items.

#### Returns

- `Union[object,` *_dict]* - If `first` is True, returns the first matching item. If `first` is False, returns a new `_dict` object with all matching items.

#### Signature

```python
def by(self, field: str = "", value: object = None, first: bool = True): ...
```



## http_utils

[Show source in utils.py:10](../../pynab/utils.py#L10)

#### Signature

```python
class http_utils:
    def __init__(self, pynab: pynab = None): ...
```

#### See also

- [Pynab](./pynab.md#pynab)

### http_utils().delete

[Show source in utils.py:107](../../pynab/utils.py#L107)

Sends a DELETE request to the specified endpoint.

#### Arguments

- `endpoint` *str, optional* - The endpoint to send the request to. Defaults to None.

#### Returns

- `requests.Response` - The response object returned by the DELETE request.

#### Signature

```python
def delete(self, endpoint: str = None): ...
```

### http_utils().get

[Show source in utils.py:20](../../pynab/utils.py#L20)

Sends a GET request to the specified endpoint.

#### Arguments

- `endpoint` *str, optional* - The endpoint to send the request to. Defaults to None.

#### Returns

- `Response` - The response object returned by the GET request.

#### Signature

```python
def get(self, endpoint: str = None): ...
```

### http_utils().patch

[Show source in utils.py:63](../../pynab/utils.py#L63)

Sends a PATCH request to the specified endpoint with the provided JSON data.

#### Arguments

- `endpoint` *str, optional* - The endpoint to send the PATCH request to. Defaults to None.
- `json` *dict, optional* - The JSON data to include in the request body. Defaults to {}.

#### Returns

- `Response` - The response object returned by the PATCH request.

#### Signature

```python
def patch(self, endpoint: str = None, json: dict = {}): ...
```

### http_utils().post

[Show source in utils.py:41](../../pynab/utils.py#L41)

Sends a POST request to the specified endpoint with the provided JSON data.

#### Arguments

- `endpoint` *str* - The endpoint to send the request to.
- `json` *dict* - The JSON data to include in the request body.

#### Returns

- `Response` - The response object received from the server.

#### Signature

```python
def post(self, endpoint: str = None, json: dict = {}): ...
```

### http_utils().put

[Show source in utils.py:85](../../pynab/utils.py#L85)

Sends a PUT request to the specified endpoint with the given JSON payload.

#### Arguments

- `endpoint` *str* - The endpoint to send the request to.
- `json` *dict* - The JSON payload to include in the request.

#### Returns

- `Response` - The response object returned by the server.

#### Signature

```python
def put(self, endpoint: str = None, json: dict = {}): ...
```