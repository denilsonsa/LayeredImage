# io

> Auto-generated documentation for [layeredimage.io](../../layeredimage/io.py) module.

- [Layeredimage](../README.md#layeredimage-index) / [Modules](../README.md#layeredimage-modules) / [layeredimage](index.md#layeredimage) / io
    - [addLayer_ORA](#addlayer_ora)
    - [blendModeLookup](#blendmodelookup)
    - [exportFlatImage](#exportflatimage)
    - [extNotRecognised](#extnotrecognised)
    - [getRasterLayers](#getrasterlayers)
    - [grabLayer_LAYERED](#grablayer_layered)
    - [openLayerImage](#openlayerimage)
    - [openLayer_GIF](#openlayer_gif)
    - [openLayer_LAYERED](#openlayer_layered)
    - [openLayer_LAYEREDC](#openlayer_layeredc)
    - [openLayer_LSR](#openlayer_lsr)
    - [openLayer_ORA](#openlayer_ora)
    - [openLayer_PDN](#openlayer_pdn)
    - [openLayer_PSD](#openlayer_psd)
    - [openLayer_TIFF](#openlayer_tiff)
    - [openLayer_WEBP](#openlayer_webp)
    - [openLayer_XCF](#openlayer_xcf)
    - [saveLayerImage](#savelayerimage)
    - [saveLayer_GIF](#savelayer_gif)
    - [saveLayer_LAYERED](#savelayer_layered)
    - [saveLayer_LAYEREDC](#savelayer_layeredc)
    - [saveLayer_LSR](#savelayer_lsr)
    - [saveLayer_ORA](#savelayer_ora)
    - [saveLayer_PDN](#savelayer_pdn)
    - [saveLayer_PSD](#savelayer_psd)
    - [saveLayer_TIFF](#savelayer_tiff)
    - [saveLayer_WEBP](#savelayer_webp)
    - [saveLayer_XCF](#savelayer_xcf)
    - [writeImage_LAYERED](#writeimage_layered)

## addLayer_ORA

[[find in source code]](../../layeredimage/io.py#L140)

```python
def addLayer_ORA(project, layer, blendLookup):
```

Update the project with a shiny new layer

## blendModeLookup

[[find in source code]](../../layeredimage/io.py#L70)

```python
def blendModeLookup(
    blendmode: Any,
    blendLookup: dict[(Any, Any)],
    default: BlendType = BlendType.NORMAL,
) -> BlendType:
```

Get the blendmode from a lookup table

#### See also

- [BlendType](blend.md#blendtype)

## exportFlatImage

[[find in source code]](../../layeredimage/io.py#L66)

```python
def exportFlatImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Export the layered image to a unilayer image file

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## extNotRecognised

[[find in source code]](../../layeredimage/io.py#L21)

```python
def extNotRecognised(fileName: str):
```

Output the file extension not recognised error

## getRasterLayers

[[find in source code]](../../layeredimage/io.py#L360)

```python
def getRasterLayers(layeredImage: LayeredImage, imageFormat: str):
```

Return layers and throw a warning if the image has groups

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## grabLayer_LAYERED

[[find in source code]](../../layeredimage/io.py#L435)

```python
def grabLayer_LAYERED(
    zipFile: ZipFile,
    layer: dict[(str, Any)],
    blendLookup: dict[(str, Any)],
):
```

Grab an image from .layered

## openLayerImage

[[find in source code]](../../layeredimage/io.py#L27)

```python
def openLayerImage(file: str) -> LayeredImage:
```

Open a layer image file into a layer image object

#### Arguments

- `file` *str* - path/ filename

#### Returns

- `LayeredImage` - a layered image object

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_GIF

[[find in source code]](../../layeredimage/io.py#L324)

```python
def openLayer_GIF(file: str) -> LayeredImage:
```

Open a .gif file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_LAYERED

[[find in source code]](../../layeredimage/io.py#L404)

```python
def openLayer_LAYERED(file: str) -> LayeredImage:
```

Open a .layered file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_LAYEREDC

[[find in source code]](../../layeredimage/io.py#L474)

```python
def openLayer_LAYEREDC(file: str) -> LayeredImage:
```

Open a .layeredc file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_LSR

[[find in source code]](../../layeredimage/io.py#L372)

```python
def openLayer_LSR(file: str) -> LayeredImage:
```

Open a .lsr file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_ORA

[[find in source code]](../../layeredimage/io.py#L79)

```python
def openLayer_ORA(file: str) -> LayeredImage:
```

Open an .ora file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_PDN

[[find in source code]](../../layeredimage/io.py#L265)

```python
def openLayer_PDN(file: str) -> LayeredImage:
```

Open a .pdn file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_PSD

[[find in source code]](../../layeredimage/io.py#L148)

```python
def openLayer_PSD(file: str) -> LayeredImage:
```

Open a .psd file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_TIFF

[[find in source code]](../../layeredimage/io.py#L290)

```python
def openLayer_TIFF(file: str) -> LayeredImage:
```

Open a .tiff or a .tif file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_WEBP

[[find in source code]](../../layeredimage/io.py#L343)

```python
def openLayer_WEBP(file: str) -> LayeredImage:
```

Open a .webp file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## openLayer_XCF

[[find in source code]](../../layeredimage/io.py#L192)

```python
def openLayer_XCF(file: str) -> LayeredImage:
```

Open an .xcf file into a layered image

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayerImage

[[find in source code]](../../layeredimage/io.py#L49)

```python
def saveLayerImage(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image to a file

#### Arguments

- `fileName` *str* - path/ filename
- `layeredImage` *LayeredImage* - the layered image to save

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_GIF

[[find in source code]](../../layeredimage/io.py#L336)

```python
def saveLayer_GIF(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .gif

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_LAYERED

[[find in source code]](../../layeredimage/io.py#L443)

```python
def saveLayer_LAYERED(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .layered

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_LAYEREDC

[[find in source code]](../../layeredimage/io.py#L478)

```python
def saveLayer_LAYEREDC(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layeredc image as .layered

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_LSR

[[find in source code]](../../layeredimage/io.py#L384)

```python
def saveLayer_LSR(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .lsr

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_ORA

[[find in source code]](../../layeredimage/io.py#L113)

```python
def saveLayer_ORA(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .ora

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_PDN

[[find in source code]](../../layeredimage/io.py#L283)

```python
def saveLayer_PDN(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .pdn

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_PSD

[[find in source code]](../../layeredimage/io.py#L185)

```python
def saveLayer_PSD(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .psd

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_TIFF

[[find in source code]](../../layeredimage/io.py#L317)

```python
def saveLayer_TIFF(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .tiff or .tif

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_WEBP

[[find in source code]](../../layeredimage/io.py#L354)

```python
def saveLayer_WEBP(fileName: str, layeredImage: LayeredImage):
```

Save a layered image as .webp

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## saveLayer_XCF

[[find in source code]](../../layeredimage/io.py#L256)

```python
def saveLayer_XCF(fileName: str, layeredImage: LayeredImage) -> None:
```

Save a layered image as .xcf

#### See also

- [LayeredImage](layeredimage.md#layeredimage)

## writeImage_LAYERED

[[find in source code]](../../layeredimage/io.py#L463)

```python
def writeImage_LAYERED(
    image: Image.Image,
    zipFile: ZipFile,
    path: str,
    compressed: bool = False,
):
```

Write an image to the archive