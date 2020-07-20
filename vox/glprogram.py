from OpenGL import GL as gl


class ShaderCompilationFailed(Exception):
    pass


class ShaderLinkingFailed(Exception):
    pass


def create_and_compile_shader(filepath, shader_type):
    """
    Create a new shader with given source, compile it and returns the gl_id.
    Raises a ShaderCompilationFailed if the compilation failed.
    """
    shader_id = gl.glCreateShader(shader_type)
    with open(filepath, "r") as f:
        gl.glShaderSource(shader_id, f.read())
    gl.glCompileShader(shader_id)
    status = gl.glGetShaderiv(shader_id, gl.GL_COMPILE_STATUS)
    loglength = gl.glGetShaderiv(shader_id, gl.GL_INFO_LOG_LENGTH)
    if loglength > 1:
        print("Error compiling %s." % str(shader_type))
        print("Status = %s" % str(status))
        print(gl.glGetShaderInfoLog(shader_id))
        raise ShaderCompilationFailed()
    return shader_id


class GLProgram(object):
    def __init__(self, vs_filepath, fs_filepath):
        """
        Load and compile shaders and store the gl pogram id.
        """
        self.gl_id = gl.glCreateProgram()
        vs_id = create_and_compile_shader(vs_filepath)
        gl.glAttachShader(self.gl_id, vs_id)
        fs_id = create_and_compile_shader(fs_filepath)
        gl.glAttachShader(self.gl_id, fs_id)

        gl.glLinkProgram(self.gl_id)
        gl.glDeleteShader(vs_id)
        gl.glDeleteShader(fs_id)

        status = gl.glGetProgramiv(self.gl_id, gl.GL_LINK_STATUS)
        loglength = gl.glGetShaderiv(self.gl_id, gl.GL_INFO_LOG_LENGTH)
        if loglength > 1:
            print("Error linking shaders.")
            print("Status = %s" % str(status))
            print(gl.glGetProgramInfoLog(self.gl_id))
            raise ShaderLinkingFailed()

    def __del__(self):
        if gl.glIsProgram(self.gl_id):
            gl.glDeleteProgram(self.gl_id)

    def __enter__(self):
        gl.glUseProgram(self.gl_id)

    def __exit__(self):
        gl.glUseProgram(0)
