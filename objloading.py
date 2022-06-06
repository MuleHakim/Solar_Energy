import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from ObjLoader import ObjLoader
import pickle
from TextureLoader import load_texture

vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;
uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;
out vec2 v_texture;
void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, v_texture);
}
"""


# glfw callback functions


def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# set the callback function for window resize
glfw.set_window_size_callback(window, window_resize)

# make the context current
glfw.make_context_current(window)

# load here the 3d meshes
chibi_indices, chibi_buffer = ObjLoader.load_model("road.obj")
monkey_indices, monkey_buffer = ObjLoader.load_model("floor.obj")
solarpanel_indices, solarpanel_buffer = ObjLoader.load_model("solarpanelobj.obj")
tree_indices, tree_buffer = ObjLoader.load_model("tree.obj")
home_indices, home_buffer = ObjLoader.load_model("home.obj")
door_indices, door_buffer = ObjLoader.load_model("door.obj")
window_indices, window_buffer = ObjLoader.load_model("window.obj")
hotel_indices, hotel_buffer = ObjLoader.load_model("hotel.obj")
window2_indices, window2_buffer = ObjLoader.load_model("window2.obj")
hotel2_indices, hotel2_buffer = ObjLoader.load_model("hotel2.obj")
hotel3_indices, hotel3_buffer = ObjLoader.load_model("hotel3.obj")
leg_indices, leg_buffer = ObjLoader.load_model("leg.obj")

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

# VAO and VBO
VAO = glGenVertexArrays(12)
VBO = glGenBuffers(12)
# EBO = glGenBuffers(1)

# Chibi VAO
glBindVertexArray(VAO[0])
# Chibi Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
glBufferData(GL_ARRAY_BUFFER, chibi_buffer.nbytes, chibi_buffer, GL_STATIC_DRAW)

# glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
# glBufferData(GL_ELEMENT_ARRAY_BUFFER, chibi_indices.nbytes, chibi_indices, GL_STATIC_DRAW)

# chibi vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(0))
# chibi textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(12))
# chibi normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, chibi_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# Monkey VAO
glBindVertexArray(VAO[1])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
glBufferData(GL_ARRAY_BUFFER, monkey_buffer.nbytes, monkey_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, monkey_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# Monkey VAO
glBindVertexArray(VAO[2])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[2])
glBufferData(GL_ARRAY_BUFFER, solarpanel_buffer.nbytes, solarpanel_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# Monkey VAO
glBindVertexArray(VAO[3])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[3])
glBufferData(GL_ARRAY_BUFFER, tree_buffer.nbytes, tree_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, tree_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, tree_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, tree_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# Monkey VAO
glBindVertexArray(VAO[4])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[4])
glBufferData(GL_ARRAY_BUFFER, home_buffer.nbytes, home_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(5)

# Monkey VAO
glBindVertexArray(VAO[5])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[5])
glBufferData(GL_ARRAY_BUFFER, door_buffer.nbytes, door_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(6)

# Monkey VAO
glBindVertexArray(VAO[6])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[6])
glBufferData(GL_ARRAY_BUFFER, window_buffer.nbytes, window_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(7)

# Monkey VAO
glBindVertexArray(VAO[7])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[7])
glBufferData(GL_ARRAY_BUFFER, hotel_buffer.nbytes, hotel_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(8)

# Monkey VAO
glBindVertexArray(VAO[8])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[8])
glBufferData(GL_ARRAY_BUFFER, window2_buffer.nbytes, window2_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(9)

# Monkey VAO
glBindVertexArray(VAO[9])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[9])
glBufferData(GL_ARRAY_BUFFER, hotel2_buffer.nbytes, hotel2_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(10)

# Monkey VAO
glBindVertexArray(VAO[10])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[10])
glBufferData(GL_ARRAY_BUFFER, hotel3_buffer.nbytes, hotel3_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(11)

# Monkey VAO
glBindVertexArray(VAO[11])
# Monkey Vertex Buffer Object
glBindBuffer(GL_ARRAY_BUFFER, VBO[11])
glBufferData(GL_ARRAY_BUFFER, leg_buffer.nbytes, leg_buffer, GL_STATIC_DRAW)

# monkey vertices
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(0))
# monkey textures
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(12))
# monkey normals
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(12)

textures = glGenTextures(7)
load_texture("road.jpg", textures[0])
load_texture("floor.jpeg", textures[1])
load_texture("solarpanel.jpg", textures[2])
load_texture("tree.jpeg", textures[3])
load_texture("home.jpeg", textures[4])
load_texture("door.jpeg", textures[5])
load_texture("window.jpeg", textures[6])

glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
chibi_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
monkey_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
solarpanel_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
tree_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
home_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
door_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
window_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
hotel_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
window2_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
hotel2_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
hotel3_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
leg_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))

# eye, target, up
view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_y = pyrr.Matrix44.from_y_rotation(0.1 * glfw.get_time())
    model = pyrr.matrix44.multiply(rot_y, chibi_pos)

    # draw the chibi character
    glBindVertexArray(VAO[0])
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(chibi_indices))

    model = pyrr.matrix44.multiply(rot_y, monkey_pos)
    glBindVertexArray(VAO[1])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(monkey_indices))

    model = pyrr.matrix44.multiply(rot_y, solarpanel_pos)
    glBindVertexArray(VAO[2])
    glBindTexture(GL_TEXTURE_2D, textures[2])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(solarpanel_indices))

    model = pyrr.matrix44.multiply(rot_y, tree_pos)
    glBindVertexArray(VAO[3])
    glBindTexture(GL_TEXTURE_2D, textures[3])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(tree_indices))

    model = pyrr.matrix44.multiply(rot_y, home_pos)
    glBindVertexArray(VAO[4])
    glBindTexture(GL_TEXTURE_2D, textures[4])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(home_indices))

    model = pyrr.matrix44.multiply(rot_y, window_pos)
    glBindVertexArray(VAO[5])
    glBindTexture(GL_TEXTURE_2D, textures[5])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window_indices))

    model = pyrr.matrix44.multiply(rot_y, window_pos)
    glBindVertexArray(VAO[6])
    glBindTexture(GL_TEXTURE_2D, textures[6])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window_indices))

    model = pyrr.matrix44.multiply(rot_y, hotel_pos)
    glBindVertexArray(VAO[7])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel_indices))

    model = pyrr.matrix44.multiply(rot_y, window2_pos)
    glBindVertexArray(VAO[8])
    glBindTexture(GL_TEXTURE_2D, textures[6])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window2_indices))

    model = pyrr.matrix44.multiply(rot_y, hotel2_pos)
    glBindVertexArray(VAO[9])
    glBindTexture(GL_TEXTURE_2D, textures[4])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel2_indices))

    glBindVertexArray(VAO[10])
    glBindTexture(GL_TEXTURE_2D, textures[4])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel3_indices))

    glBindVertexArray(VAO[11])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(leg_indices))

    glfw.swap_buffers(window)

glfw.terminate()
