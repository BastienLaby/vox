from OpenGL import GL as gl


class Viewport(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        gl.glClearColor(1.0, 0.0, 0.0, 1.0)

    def render(self):

        # clear

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # bind programs and send uniforms

        # draw
