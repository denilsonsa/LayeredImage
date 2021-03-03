# tiff

> Auto-generated documentation for [layeredimage.io.tiff](../../../layeredimage/io/tiff.py) module.

Do file io - TIFF.

- [Layeredimage](../../README.md#layeredimage-index) / [Modules](../../README.md#layeredimage-modules) / [layeredimage](../index.md#layeredimage) / [io](index.md#io) / tiff
    - [openLayer_TIFF](#openlayer_tiff)
    - [saveLayer_TIFF](#savelayer_tiff)

## openLayer_TIFF

[[find in source code]](../../../layeredimage/io/tiff.py#L14)

```python
def openLayer_TIFF(file: str) -> LayeredImage:
```

Open a .tiff or a .tif file into a layered image.

## saveLayer_TIFF

[[find in source code]](../../../layeredimage/io/tiff.py#L47)

```python
def saveLayer_TIFF(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .tiff or .tif.