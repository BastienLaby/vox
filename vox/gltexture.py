from OpenGL import GL as gl
from PIL import Image


class GLTexture(object):
    def __init__(self, filepath):
        img = Image.open(filepath)
        w, h = img.size
        try:
            data = img.tobytes("raw", "RGBA", 0, -1)
        except SystemError:
            data = img.tobytes("raw", "RGBX", 0, -1)

        self.gl_id = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_ID, self.gl_id)
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, w, h, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, data)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
        gl.glBindTexture(gl.GL_TEXTURE_ID, 0)

    def __enter__(self):
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.gl_id)

    def __exit__(self):
        gl.glBindTexture(gl.GL_TEXTURE_ID, 0)


