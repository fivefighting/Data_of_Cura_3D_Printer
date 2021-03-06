'''OpenGL extension NV.float_buffer

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_float_buffer'
_DEPRECATED = False
GL_FLOAT_R_NV = constant.Constant( 'GL_FLOAT_R_NV', 0x8880 )
GL_FLOAT_RG_NV = constant.Constant( 'GL_FLOAT_RG_NV', 0x8881 )
GL_FLOAT_RGB_NV = constant.Constant( 'GL_FLOAT_RGB_NV', 0x8882 )
GL_FLOAT_RGBA_NV = constant.Constant( 'GL_FLOAT_RGBA_NV', 0x8883 )
GL_FLOAT_R16_NV = constant.Constant( 'GL_FLOAT_R16_NV', 0x8884 )
GL_FLOAT_R32_NV = constant.Constant( 'GL_FLOAT_R32_NV', 0x8885 )
GL_FLOAT_RG16_NV = constant.Constant( 'GL_FLOAT_RG16_NV', 0x8886 )
GL_FLOAT_RG32_NV = constant.Constant( 'GL_FLOAT_RG32_NV', 0x8887 )
GL_FLOAT_RGB16_NV = constant.Constant( 'GL_FLOAT_RGB16_NV', 0x8888 )
GL_FLOAT_RGB32_NV = constant.Constant( 'GL_FLOAT_RGB32_NV', 0x8889 )
GL_FLOAT_RGBA16_NV = constant.Constant( 'GL_FLOAT_RGBA16_NV', 0x888A )
GL_FLOAT_RGBA32_NV = constant.Constant( 'GL_FLOAT_RGBA32_NV', 0x888B )
GL_TEXTURE_FLOAT_COMPONENTS_NV = constant.Constant( 'GL_TEXTURE_FLOAT_COMPONENTS_NV', 0x888C )
GL_FLOAT_CLEAR_COLOR_VALUE_NV = constant.Constant( 'GL_FLOAT_CLEAR_COLOR_VALUE_NV', 0x888D )
glget.addGLGetConstant( GL_FLOAT_CLEAR_COLOR_VALUE_NV, (4,) )
GL_FLOAT_RGBA_MODE_NV = constant.Constant( 'GL_FLOAT_RGBA_MODE_NV', 0x888E )
glget.addGLGetConstant( GL_FLOAT_RGBA_MODE_NV, (1,) )


def glInitFloatBufferNV():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
