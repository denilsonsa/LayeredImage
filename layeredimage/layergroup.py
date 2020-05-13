""" Base class """

from enum import Enum
from layeredimage.blend import BlendType

#pylint: disable=too-few-public-methods
#pylint: disable=too-many-arguments
#pylint: disable=too-many-instance-attributes

class LayerGroupTypes(Enum):
	""" Can be a LAYER, GROUP, or UNDEFINED """
	UNDEFINED = 0
	LAYER = 1
	GROUP = 2

class LayerGroup:
	""" A representation of an image layer or group """
	def __init__(self, name, dimensions, offsets=(0, 0), opacity=1.0, visible=True,
	layerGroup=LayerGroupTypes.LAYER, blendmode=BlendType.NORMAL, **kwargs):
		""" A representation of an image layer or group

		Args:
			name (string): Name of the layer or group
			dimensions ((int, int)): A tuple representing the dimensions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
			layerGroup ([type], optional): Type LAYER, GROUP, or UNDEFINED.
			Defaults to LayerGroupTypes.LAYER.
		"""
		self.name = name
		self.offsets = offsets
		self.opacity = opacity
		self.visible = visible
		self.dimensions = dimensions
		self.type = layerGroup
		self.blendmode = blendmode
		self.extras = kwargs

	def __repr__(self):
		return "<LayeredImage " + ("Group" if self.type == LayerGroupTypes.GROUP
		else "Layer") + " \"" + self.name + "\" (" + str(self.dimensions[0]) + "x" + str(
			self.dimensions[1]) + ")>"


class Layer(LayerGroup):
	""" A representation of an image layer """
	def __init__(self, name, image, dimensions=None, offsets=(0, 0), opacity=1.0,
	visible=True, blendmode=BlendType.NORMAL):
		""" A representation of an image layer

		Args:
			name (string): Name of the layer or group
			image (PIL.Image): A PIL Image
			dimensions ((int, int)): A tuple representing the dimensions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		super().__init__(name, dimensions, offsets=offsets, opacity=opacity,
		visible=visible, blendmode=blendmode)
		self.image = image

		# If the user does not specify the dimensions use image.size
		self.dimensions = dimensions
		if dimensions is None:
			self.dimensions = image.size

	def json(self):
		""" Get the object as a dict """
		return {"name": self.name, "offsets": self.offsets, "opacity": self.opacity,
		"visible": self.visible, "dimensions": self.dimensions, "type": self.type.name,
		"blendmode": self.blendmode.name}


class Group(LayerGroup):
	""" A representation of an image group """
	def __init__(self, name, layers, dimensions=None, offsets=(0, 0), opacity=1.0,
	visible=True, blendmode=BlendType.NORMAL):
		""" A representation of an image group

		Args:
			name (string): Name of the layer or group
			layers (layeredimage.Layer[]): A list of layers where the next
			index stacks upon the previous layer
			dimensions ((int, int)): A tuple representing the dimensions in
			pixels
			offsets (tuple, optional): A tuple representing the left and top
			offsets in pixels. Defaults to (0, 0).
			opacity (float, optional): A float representing the alpha value
			where 0 is invisible and 1 is fully visible. Defaults to 1.0.
			visible (bool, optional): Is the layer visible to the user (this
			is often configured per layer or per group by an 'eye' icon).
			Defaults to True.
		"""
		super().__init__(name, dimensions, offsets=offsets, opacity=opacity,
		visible=visible, layerGroup=LayerGroupTypes.GROUP, blendmode=blendmode)
		self.layers = layers

		# If the user does not specify the dimensions use the largest x and y of
		# the layers
		self.dimensions = dimensions
		if dimensions is None:
			layerDimens = [layer.dimensions for layer in layers]
			self.dimensions = (max([dimensions[0] for dimensions in layerDimens]),
			max([dimensions[1] for dimensions in layerDimens]))

	def json(self):
		""" Get the object as a dict """
		layers = [layer.json() for layer in self.layers]
		return {"name": self.name, "offsets": self.offsets, "opacity": self.opacity,
		"visible": self.visible, "dimensions": self.dimensions, "type": self.type.name,
		"blendmode": self.blendmode.name, "layers": layers}
