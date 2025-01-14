"""Do file io - ORA."""
from __future__ import annotations

from ..blend import BlendType
from ..layeredimage import LayeredImage
from ..layergroup import Group, Layer
from .common import blendModeLookup

# pylint: disable=invalid-name
# pylint: disable=import-outside-toplevel


#### ORA ####
def openLayer_ORA(file: str) -> LayeredImage:
	"""Open an .ora file into a layered image."""
	from pyora import TYPE_LAYER, Project

	blendLookup = {
		"svg:src-over": BlendType.NORMAL,
		"svg:multiply": BlendType.MULTIPLY,
		"svg:color-burn": BlendType.COLOURBURN,
		"svg:color-dodge": BlendType.COLOURDODGE,
		"svg:": BlendType.REFLECT,
		"svg:overlay": BlendType.OVERLAY,
		"svg:difference": BlendType.DIFFERENCE,
		"svg:lighten": BlendType.LIGHTEN,
		"svg:darken": BlendType.DARKEN,
		"svg:screen": BlendType.SCREEN,
		"svg:hard-light": BlendType.HARDLIGHT,
		"svg:soft-light": BlendType.SOFTLIGHT,
		"svg:hue": BlendType.HUE,
		"svg:saturation": BlendType.SATURATION,
		"svg:color": BlendType.COLOUR,
		"svg:luminosity": BlendType.LUMINOSITY,
		"svg:plus": BlendType.ADDITIVE,
		"svg:dst-in": BlendType.DESTIN,
		"svg:dst-out": BlendType.DESTOUT,
		"svg:dst-atop": BlendType.DESTATOP,
		"svg:src-atop": BlendType.SRCATOP,
	}
	layersAndGroups = []
	project = Project.load(file)
	for layerOrGroup in project.children[::-1]:
		if layerOrGroup.type == TYPE_LAYER:
			layersAndGroups.append(
				Layer(
					layerOrGroup.name,
					layerOrGroup.get_image_data(True),
					layerOrGroup.dimensions,
					layerOrGroup.offsets,
					layerOrGroup.opacity,
					layerOrGroup.visible,
					blendModeLookup(layerOrGroup.composite_op, blendLookup),
				)
			)
		else:
			layers = []
			for layer in list(layerOrGroup.children)[::-1]:
				layers.append(
					Layer(
						layer.name,
						layer.get_image_data(True),
						layer.dimensions,
						layer.offsets,
						layer.opacity,
						layer.visible,
						blendModeLookup(layerOrGroup.composite_op, blendLookup),
					)
				)
			layersAndGroups.append(
				Group(
					layerOrGroup.name,
					layers,
					project.dimensions,
					layerOrGroup.offsets,
					layerOrGroup.opacity,
					layerOrGroup.visible,
					blendModeLookup(layerOrGroup.composite_op, blendLookup),
				)
			)
	return LayeredImage(layersAndGroups, project.dimensions)


def saveLayer_ORA(fileName: str, layeredImage: LayeredImage) -> None:
	"""Save a layered image as .ora."""
	from pyora import Project

	blendLookup = {
		BlendType.NORMAL: "svg:src-over",
		BlendType.MULTIPLY: "svg:multiply",
		BlendType.COLOURBURN: "svg:color-burn",
		BlendType.COLOURDODGE: "svg:color-dodge",
		BlendType.REFLECT: "svg:",
		BlendType.OVERLAY: "svg:overlay",
		BlendType.DIFFERENCE: "svg:difference",
		BlendType.LIGHTEN: "svg:lighten",
		BlendType.DARKEN: "svg:darken",
		BlendType.SCREEN: "svg:screen",
		BlendType.SOFTLIGHT: "svg:soft-light",
		BlendType.HARDLIGHT: "svg:hard-light",
		BlendType.HUE: "svg:hue",
		BlendType.SATURATION: "svg:saturation",
		BlendType.COLOUR: "svg:color",
		BlendType.LUMINOSITY: "svg:luminosity",
		BlendType.ADDITIVE: "svg:plus",
		BlendType.DESTIN: "svg:dst-in",
		BlendType.DESTOUT: "svg:dst-out",
		BlendType.DESTATOP: "svg:dst-atop",
		BlendType.SRCATOP: "svg:src-atop",
	}
	project = Project.new(layeredImage.dimensions[0], layeredImage.dimensions[1])
	for layerOrGroup in layeredImage.layersAndGroups:
		if isinstance(layerOrGroup, Layer):
			project = addLayer_ORA(project, layerOrGroup, blendLookup)
		else:
			group = project.add_group(
				layerOrGroup.name,
				offsets=layerOrGroup.offsets,
				opacity=layerOrGroup.opacity,
				visible=layerOrGroup.visible,
				composite_op=blendModeLookup(layerOrGroup.blendmode, blendLookup, "svg:src-over"),
			)
			for layer in layerOrGroup.layers:
				group = addLayer_ORA(group, layer, blendLookup)
	project.save(fileName)


def addLayer_ORA(project, layer, blendLookup):
	"""Update the project with a shiny new layer."""
	project.add_layer(
		layer.image,
		layer.name,
		offsets=layer.offsets,
		opacity=layer.opacity,
		visible=layer.visible,
		composite_op=blendModeLookup(layer.blendmode, blendLookup, "svg:src-over"),
	)
	return project
