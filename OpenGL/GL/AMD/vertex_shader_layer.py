'''OpenGL extension AMD.vertex_shader_layer

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.vertex_shader_layer to provide a more 
Python-friendly API

Overview (from the spec)
	
	The gl_Layer built-in shading language variable was introduced with the
	ARB_geometry_shader extension and subsequently promoted to core OpenGL
	in version 3.2. This variable is an output from the geometry shader stage
	that allows rendering to be directed to a specific layer of an array
	texture, slice of a 3D texture or face of a cube map or cube map array
	attachment of the framebuffer. Thus, this extremely useful functionality is
	only available if a geometry shader is present - even if the geometry shader
	is not otherwise required by the application. This adds overhead to the
	graphics processing pipeline, and complexity to applications. It also
	precludes implementations that cannot support geometry shaders from
	supporting rendering to layered framebuffer attachments.
	
	This extension exposes the gl_Layer built-in variable in the vertex shader,
	allowing rendering to be directed to layered framebuffer attachments with
	only a vertex and fragment shader present. Combined with features such
	as instancing, or static vertex attributes and so on, this allows a wide
	variety of techniques to be implemented without the requirement for a
	geometry shader to be present.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/vertex_shader_layer.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.vertex_shader_layer import *
### END AUTOGENERATED SECTION