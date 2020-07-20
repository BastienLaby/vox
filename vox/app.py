import glfw

from vox.viewport import Viewport


def main():

    if not glfw.init():
        print("not init")
        return # in wich case ?

    window = glfw.create_window(200, 200, "hello", None, None)

    if not window:
        glfw.terminate()
        print("not window")
        return

    glfw.make_context_current(window)
    viewport = Viewport(400, 400)

    # loop
    while not glfw.window_should_close(window):

        # render here

        viewport.render()

        # swap buffer
        glfw.swap_buffers(window)

        # poll for process events

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()