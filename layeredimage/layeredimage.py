"""LayeredImage class."""
from __future__ import annotations

from typing import Any

# pylint: disable=unused-import
from blendmodes.imagetools import rasterImageOA, rasterImageOffset, renderWAlphaOffset
from deprecation import deprecated
from PIL import Image

from .blend import blendLayers
from .layergroup import Group, Layer


class LayeredImage:
	"""A representation of a layered image such as an ora."""

	def __init__(
		self,
		layersAndGroups: list[Layer | Group],
		dimensions: tuple[int, int] | None = None,
		**kwargs: Any,
	):
		"""LayeredImage - representation of a layered image.

		Args:
			layersAndGroups (list[Layer, Group]): List of layers and groups
			dimensions (tuple[int, int], optional): dimensions of the canvas. Defaults to None.
		"""
		# Write here
		self.layersAndGroups = layersAndGroups
		# Read only
		self.groups = self.extractGroups()
		self.layers = self.extractLayers()
		# If the user does not specify the dimensions use the largest x and y of
		# the layers and groups
		self.dimensions = dimensions or (0, 0)
		if dimensions is None:
			layerDimens = [layerOrGroup.dimensions for layerOrGroup in layersAndGroups]
			self.dimensions = (
				max(layerDimen[0] for layerDimen in layerDimens),
				max(layerDimen[1] for layerDimen in layerDimens),
			)
		self.extras = kwargs

	def __repr__(self):
		"""Get the string representation."""
		return self.__str__()

	def __str__(self):
		"""Get the string representation."""
		return (
			"<LayeredImage ("
			+ str(self.dimensions[0])
			+ "x"
			+ str(self.dimensions[1])
			+ ") with "
			+ str(len(self.layersAndGroups))
			+ " children>"
		)

	def json(self) -> dict[str, Any]:
		"""Get the object as a dict."""
		layersAndGroups = [layerOrGroup.json() for layerOrGroup in self.layersAndGroups]
		return {"dimensions": self.dimensions, "layersAndGroups": layersAndGroups}

	# Get, set and remove layers or groups
	def getLayerOrGroup(self, index: int):
		"""Get a LayerOrGroup."""
		return self.layersAndGroups[index]

	def addLayerOrGroup(self, layerOrGroup: Layer | Group):
		"""Add a LayerOrGroup."""
		self.layersAndGroups.append(layerOrGroup)

	def insertLayerOrGroup(self, layerOrGroup: Layer | Group, index: int):
		"""Insert a LayerOrGroup at a specific index."""
		self.layersAndGroups.insert(index, layerOrGroup)

	def removeLayerOrGroup(self, index: int):
		"""Remove a LayerOrGroup at a specific index."""
		self.layersAndGroups.pop(index)

	# The user may wish to add an image directly
	@deprecated(details="use addImageAsLayer", deprecated_in="2021.2.4")
	def addLayerRaster(
		self, image: Image.Image, name: str
	):  # pylint:disable=missing-function-docstring
		return self.addImageAsLayer(image, name)

	def addImageAsLayer(self, image: Image.Image, name: str):
		"""Resize an image to the canvas and add as a layer."""
		layer = renderWAlphaOffset(image, self.dimensions)
		self.addLayerOrGroup(Layer(name, layer, self.dimensions))

	@deprecated(details="use insertImageAsLayer", deprecated_in="2021.2.4")
	def insertLayerRaster(
		self, image: Image.Image, name: str, index: int
	):  # pylint:disable=missing-function-docstring
		return self.insertImageAsLayer(image, name, index)

	def insertImageAsLayer(self, image: Image.Image, name: str, index: int):
		"""Resize an image to the canvas  and insert the layer."""
		layer = renderWAlphaOffset(image, self.dimensions)
		self.insertLayerOrGroup(Layer(name, layer, self.dimensions), index)

	# The user may want to flatten the layers
	def getFlattenLayers(self, ignoreHidden: bool = True) -> Image.Image:
		"""Return an image for all flattened layers."""
		return flattenAll(self.layersAndGroups, self.dimensions, ignoreHidden)

	def getFlattenTwoLayers(
		self, background: int, foreground: int, ignoreHidden: bool = True
	) -> Image.Image:
		"""Return an image for two flattened layers."""
		flattenedSoFar = flattenLayerOrGroup(
			self.layersAndGroups[background], self.dimensions, ignoreHidden=ignoreHidden
		)
		return flattenLayerOrGroup(
			self.layersAndGroups[foreground],
			self.dimensions,
			flattenedSoFar,
			ignoreHidden=ignoreHidden,
		)

	def flattenTwoLayers(self, background: int, foreground: int, ignoreHidden: bool = True):
		"""Flatten two layers."""
		image = self.getFlattenTwoLayers(background, foreground, ignoreHidden)
		self.removeLayerOrGroup(foreground)
		self.layersAndGroups[background] = Layer(
			self.layersAndGroups[background].name + " (flattened)", image, self.dimensions
		)

	def flattenLayers(self, ignoreHidden: bool = True):
		"""Flatten all layers."""
		image = self.getFlattenLayers(ignoreHidden)
		self.layersAndGroups[0] = Layer(
			self.layersAndGroups[0].name + " (flattened)", image, self.dimensions
		)
		for layer in range(1, len(self.layersAndGroups)):
			self.removeLayerOrGroup(layer)

	# The user may hate groups and just want the layers... or just want the
	# groups
	def extractLayers(self):
		"""Extract the layers from the image."""
		layers = []
		for layerOrGroup in self.layersAndGroups:
			if isinstance(layerOrGroup, Layer):
				layers.append(layerOrGroup)
			else:
				for layer in layerOrGroup.layers:
					# Render the layer
					layers.append(
						Layer(
							layer.name,
							layer.image,
							(
								max(layer.dimensions[0], layerOrGroup.dimensions[0]),
								max(layer.dimensions[1], layerOrGroup.dimensions[1]),
							),
							(
								layerOrGroup.offsets[0] + layer.offsets[0],
								layerOrGroup.offsets[1] + layer.offsets[1],
							),
							layerOrGroup.opacity * layer.opacity,
							layerOrGroup.visible and layer.visible,
						)
					)
		return layers

	def updateLayers(self):
		"""Update the layers from the image."""
		self.layers = self.extractLayers()

	def extractGroups(self):
		"""Extract the groups from the image."""
		return [
			_layerOrGroup
			for _layerOrGroup in self.layersAndGroups
			if isinstance(_layerOrGroup, Group)
		]

	def updateGroups(self):
		"""Update the groups from the image."""
		self.groups = self.extractGroups()


def flattenLayerOrGroup(
	layerOrGroup: Layer | Group,
	imageDimensions: tuple[int, int],
	flattenedSoFar: Image.Image | None = None,
	ignoreHidden: bool = True,
):
	"""Flatten a layer or group on to an image of what has already been flattened.

	Args:
		layerOrGroup (Layer, Group): A layer or a group of layers
		imageDimensions (tuple[int, int]): size of the image
		flattenedSoFar (Image.Image, optional): the image of what has already
		been flattened. Defaults to None.
		ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
		to True.

	Returns:
		Image.Image: Flattened image
	"""
	if ignoreHidden and not layerOrGroup.visible:
		foregroundRender = Image.new("RGBA", imageDimensions)
	elif isinstance(layerOrGroup, Group):
		foregroundRender = renderWAlphaOffset(
			flattenAll(layerOrGroup.layers, imageDimensions, ignoreHidden),
			imageDimensions,
			1,
			layerOrGroup.offsets,
		)
	else:
		# Get a rendered image and apply blending
		foregroundRender = renderWAlphaOffset(
			layerOrGroup.image, imageDimensions, 1, layerOrGroup.offsets
		)
	if flattenedSoFar is None:
		return foregroundRender
	return blendLayers(
		flattenedSoFar, foregroundRender, layerOrGroup.blendmode, layerOrGroup.opacity
	)


def flattenAll(
	layers: list[Layer | Group] | list[Layer],
	imageDimensions: tuple[int, int],
	ignoreHidden: bool = True,
):
	"""Flatten a list of layers and groups.

	Args:
		layers (list[Layer | Group] | list[Layer]): A list of layers and groups
		imageDimensions (tuple[int, int]): size of the image
		been flattened. Defaults to None.
		ignoreHidden (bool, optional): ignore layers that are hidden. Defaults
		to True.

	Returns:
		Image.Image: Flattened image
	"""
	flattenedSoFar = flattenLayerOrGroup(layers[0], imageDimensions, ignoreHidden=ignoreHidden)
	for layer in range(1, len(layers)):
		flattenedSoFar = flattenLayerOrGroup(
			layers[layer], imageDimensions, flattenedSoFar=flattenedSoFar, ignoreHidden=ignoreHidden
		)
	return flattenedSoFar
