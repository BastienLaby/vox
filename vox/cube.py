import ctypes

from OpenGL import GL as gl
import numpy as np


class VAO(object):
    def __init__(self):
        self.gl_id = gl.glGenVertexArrays(1)

    def __enter__(self):
        gl.glBindVertexArray(self.gl_id)

    def __exit__(self):
        gl.glBindVertexArray(0)

    def __del__(self):
        if gl.glIsVertexArray(self.gl_id):
            gl.glDeleteVertexArrays(1, (gl.GLuint)(self.gl_id))


class VBO(object):
    def __init__(self, buffer_type):
        self.gl_id = gl.glGenBuffers(1)
        self.buffer_type = buffer_type

    def __enter__(self):
        gl.glBindBuffer(self.buffer_type, self.gl_id)

    def __exit__(self):
        gl.glBindBuffer(self.buffer_type, 0)

    def __del__(self):
        if gl.glIsBuffer(self.gl_id):
            gl.glDeleteBuffer(1, self.gl_id)


class RenderObject(object):
    """
    Must be subclassed with load() implemented.
    """

    poly_mode = gl.GL_FILL
    draw_mode = gl.GL_TRIANGLES

    def __init__(self):
        self.vao = VAO()
        self.vertex_count = 0  # needed to call glDrawElements
        self.load()

    def load(self):
        raise NotImplementedError()

    def draw(self):
        with self.vao:
            gl.glDrawElements(
                self.poly_mode,
                self.vertex_count,
                gl.GL_UNSIGNED_INT,
                ctypes.c_void_p(0),
            )


class Quad2D(RenderObject):
    def __init__(self):
        super(Quad2D, self).__init__()

    def load(self):
        with self.vao:
            with VBO(gl.GL_ELEMENT_ARRAY_BUFFER):
                indices = np.array([0, 1, 2, 2, 0, 3], dtype=np.int32)
                gl.glBufferData(
                    gl.GL_ELEMENT_ARRAY_BUFFER,
                    indices.nbytes,
                    indices,
                    gl.GL_STATIC_DRAW,
                )
                self.vertex_count = len(indices)
            with VBO(gl.GL_ARRAY_BUFFER):
                vertices = np.array(
                    [-1.0, 1.0, 1.0, 1.0, 1.0, -1.0, -1.0, -1.0], dtype=np.float32
                )
                gl.glEnableVertexAttribArray(0)  # shader layout location
                gl.glVertexAttribPointer(0, 2, gl.GL_FLOAT, False, 0, ctypes.c_void_p(0))
                gl.glBufferData(
                    gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW
                )
                gl.glDisableVertexAtribArray(0)
