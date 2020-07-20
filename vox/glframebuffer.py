from OpenGL import GL as gl


class GLFramebuffer(object):
    def __init__(self):
        self.gl_id = gl.glGenFramebuffer(1)

    def __enter__(self):
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, self.gl_id)

    def __exit__(self):
        gl.glBindFramebuffer(gl.GL_FRAMEBUFFER, 0)

    def __del__(self):
        gl.glDeleteFramebuffers(self.gl_id)

    def attach_texture(self, attachement, tex_id):
        with self:
            gl.glFramebufferTexture2D(gl.GL_FRAMEBUFFER, attachement, gl.GL_TEXTURE_2D, tex_id, 0)