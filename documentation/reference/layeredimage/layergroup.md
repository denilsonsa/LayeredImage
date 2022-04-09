# LayerGroup

> Auto-generated documentation for [layeredimage.layergroup](../../../layeredimage/layergroup.py) module.

Base class.

- [Layeredimage](../README.md#layeredimage-index) / [Modules](../MODULES.md#layeredimage-modules) / [Layeredimage](index.md#layeredimage) / LayerGroup
    - [Group](#group)
        - [Group().json](#groupjson)
    - [Layer](#layer)
        - [Layer().json](#layerjson)
    - [LayerGroup](#layergroup)
        - [LayerGroup().\_\_repr\_\_](#layergroup__repr__)
        - [LayerGroup().\_\_str\_\_](#layergroup__str__)
        - [LayerGroup().json](#layergroupjson)

## Group

[[find in source code]](../../../layeredimage/layergroup.py#L129)

```python
class Group(LayerGroup):
    def __init__(
        name: str,
        layers: list[Layer],
        dimensions: tuple[int, int] | None = None,
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType = BlendType.NORMAL,
    ):
```

A representation of an image group.

#### See also

- [LayerGroup](#layergroup)
- [Layer](#layer)

### Group().json

[[find in source code]](../../../layeredimage/layergroup.py#L175)

```python
def json() -> dict[str, Any]:
```

Get the object as a dict.

## Layer

[[find in source code]](../../../layeredimage/layergroup.py#L79)

```python
class Layer(LayerGroup):
    def __init__(
        name: str,
        image: Image.Image,
        dimensions: tuple[int, int] | None = None,
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType = BlendType.NORMAL,
    ):
```

A representation of an image layer.

#### See also

- [LayerGroup](#layergroup)

### Layer().json

[[find in source code]](../../../layeredimage/layergroup.py#L116)

```python
def json() -> dict[str, Any]:
```

Get the object as a dict.

## LayerGroup

[[find in source code]](../../../layeredimage/layergroup.py#L14)

```python
class LayerGroup():
    def __init__(
        name: str,
        dimensions: tuple[int, int],
        offsets: tuple[int, int] = (0, 0),
        opacity: float = 1.0,
        visible: bool = True,
        blendmode: BlendType = BlendType.NORMAL,
        **kwargs: Any,
    ):
```

A representation of an image layer or group.

### LayerGroup().\_\_repr\_\_

[[find in source code]](../../../layeredimage/layergroup.py#L50)

```python
def __repr__():
```

Get the string representation.

### LayerGroup().\_\_str\_\_

[[find in source code]](../../../layeredimage/layergroup.py#L54)

```python
def __str__():
```

Get the string representation.

### LayerGroup().json

[[find in source code]](../../../layeredimage/layergroup.py#L67)

```python
def json() -> dict[str, Any]:
```

Get the object as a dict.