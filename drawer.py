import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import pyrr
from Solar_Energy.ObjLoader1 import ObjLoader
import pickle
from Solar_Energy.texture_loader import load_texture

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




def window_resize(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)


if not glfw.init():
    raise Exception("glfw can not be initialized!")

window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

glfw.set_window_pos(window, 400, 200)

glfw.set_window_size_callback(window, window_resize)

glfw.make_context_current(window)


road_verts, road_buff = ObjLoader.load_model("road.obj")
floor_verts, floor_buff = ObjLoader.load_model("floor.obj")
solarpanel_verts, solarpanel_buffer = ObjLoader.load_model("solarpanelobj.obj")
tree_verts, tree_verts = ObjLoader.load_model("tree.obj")
home_indices, home_buffer = ObjLoader.load_model("home.obj")
door_indices, door_buffer = ObjLoader.load_model("door.obj")
window_indices, window_buffer = ObjLoader.load_model("window.obj")
hotel_indices, hotel_buffer = ObjLoader.load_model("hotel.obj")
window2_indices, window2_buffer = ObjLoader.load_model("window2.obj")
hotel2_indices, hotel2_buffer = ObjLoader.load_model("hotel2.obj")
hotel3_indices, hotel3_buffer = ObjLoader.load_model("hotel3.obj")
leg_indices, leg_buffer = ObjLoader.load_model("leg.obj")
sun_indices, sun_buffer = ObjLoader.load_model("sun.obj")


shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))


VAO = glGenVertexArrays(13)
VBO = glGenBuffers(13)


# road
glBindVertexArray(VAO[0])
glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
glBufferData(GL_ARRAY_BUFFER, road_buff.nbytes, road_buff, GL_STATIC_DRAW)



glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, road_buff.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, road_buff.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, road_buff.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# floor 
glBindVertexArray(VAO[1])

glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
glBufferData(GL_ARRAY_BUFFER, floor_buff.nbytes, floor_buff, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, floor_buff.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, floor_buff.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, floor_buff.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# solar_panel 
glBindVertexArray(VAO[2])
glBindBuffer(GL_ARRAY_BUFFER, VBO[2])
glBufferData(GL_ARRAY_BUFFER, solarpanel_buffer.nbytes, solarpanel_buffer, GL_STATIC_DRAW)

glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, solarpanel_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# tree
glBindVertexArray(VAO[3])

glBindBuffer(GL_ARRAY_BUFFER, VBO[3])
glBufferData(GL_ARRAY_BUFFER, tree_verts.nbytes, tree_verts, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, tree_verts.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, tree_verts.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, tree_verts.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(4)

# home
glBindVertexArray(VAO[4])

glBindBuffer(GL_ARRAY_BUFFER, VBO[4])
glBufferData(GL_ARRAY_BUFFER, home_buffer.nbytes, home_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, home_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(5)

# door
glBindVertexArray(VAO[5])

glBindBuffer(GL_ARRAY_BUFFER, VBO[5])
glBufferData(GL_ARRAY_BUFFER, door_buffer.nbytes, door_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, door_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(6)

# window
glBindVertexArray(VAO[6])

glBindBuffer(GL_ARRAY_BUFFER, VBO[6])
glBufferData(GL_ARRAY_BUFFER, window_buffer.nbytes, window_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, window_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(7)

# hotel
glBindVertexArray(VAO[7])

glBindBuffer(GL_ARRAY_BUFFER, VBO[7])
glBufferData(GL_ARRAY_BUFFER, hotel_buffer.nbytes, hotel_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(8)

# window2
glBindVertexArray(VAO[8])

glBindBuffer(GL_ARRAY_BUFFER, VBO[8])
glBufferData(GL_ARRAY_BUFFER, window2_buffer.nbytes, window2_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, window2_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(9)

# hotel2
glBindVertexArray(VAO[9])

glBindBuffer(GL_ARRAY_BUFFER, VBO[9])
glBufferData(GL_ARRAY_BUFFER, hotel2_buffer.nbytes, hotel2_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel2_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(10)

# hotel3
glBindVertexArray(VAO[10])

glBindBuffer(GL_ARRAY_BUFFER, VBO[10])
glBufferData(GL_ARRAY_BUFFER, hotel3_buffer.nbytes, hotel3_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, hotel3_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(11)

# solarpanel leg
glBindVertexArray(VAO[11])

glBindBuffer(GL_ARRAY_BUFFER, VBO[11])
glBufferData(GL_ARRAY_BUFFER, leg_buffer.nbytes, leg_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, leg_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(12)



# sun
glBindVertexArray(VAO[12])

glBindBuffer(GL_ARRAY_BUFFER, VBO[12])
glBufferData(GL_ARRAY_BUFFER, sun_buffer.nbytes, sun_buffer, GL_STATIC_DRAW)


glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, sun_buffer.itemsize * 8, ctypes.c_void_p(0))

glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, sun_buffer.itemsize * 8, ctypes.c_void_p(12))

glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, sun_buffer.itemsize * 8, ctypes.c_void_p(20))
glEnableVertexAttribArray(13)






textures = glGenTextures(12)
load_texture("road.png", textures[0])
load_texture("floor.jpeg", textures[1])
load_texture("solarpanel.jpg", textures[2])
load_texture("tree.jpeg", textures[3])
load_texture("home.jpeg", textures[4])
load_texture("door.jpeg", textures[5])
load_texture("window.jpeg", textures[6])
load_texture("black.png", textures[7])
load_texture("wall4.jpeg", textures[8])
load_texture("wall5.jpeg", textures[9])
load_texture("sun.jpeg", textures[10])
load_texture("yellow.jpeg", textures[11])

glUseProgram(shader)
glClearColor(0, 0.1, 0.1, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, 1280 / 720, 0.1, 100)
road_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
floor_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))
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
sun_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, -5, -10]))

view = pyrr.matrix44.create_look_at(pyrr.Vector3([0, 0, 8]), pyrr.Vector3([0, 0, 0]), pyrr.Vector3([0, 1, 0]))

model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)
glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    rot_y = pyrr.Matrix44.from_y_rotation(0.1 * glfw.get_time())
    model = pyrr.matrix44.multiply(rot_y, road_pos)

    glBindVertexArray(VAO[0])
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(road_verts))

    model = pyrr.matrix44.multiply(rot_y, floor_pos)
    glBindVertexArray(VAO[1])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(floor_verts))

    model = pyrr.matrix44.multiply(rot_y, solarpanel_pos)
    glBindVertexArray(VAO[2])
    glBindTexture(GL_TEXTURE_2D, textures[2])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(solarpanel_verts))

    model = pyrr.matrix44.multiply(rot_y, tree_pos)
    glBindVertexArray(VAO[3])
    glBindTexture(GL_TEXTURE_2D, textures[3])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(tree_verts))

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
    glBindTexture(GL_TEXTURE_2D, textures[11])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window_indices))

    model = pyrr.matrix44.multiply(rot_y, hotel_pos)
    glBindVertexArray(VAO[7])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel_indices))

    model = pyrr.matrix44.multiply(rot_y, window2_pos)
    glBindVertexArray(VAO[8])
    glBindTexture(GL_TEXTURE_2D, textures[7])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(window2_indices))

    model = pyrr.matrix44.multiply(rot_y, hotel2_pos)
    glBindVertexArray(VAO[9])
    glBindTexture(GL_TEXTURE_2D, textures[9])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel2_indices))

    glBindVertexArray(VAO[10])
    glBindTexture(GL_TEXTURE_2D, textures[8])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(hotel3_indices))

    glBindVertexArray(VAO[11])
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(leg_indices))

    glBindVertexArray(VAO[12])
    glBindTexture(GL_TEXTURE_2D, textures[10])
    glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)
    glDrawArrays(GL_TRIANGLES, 0, len(sun_indices))

    glfw.swap_buffers(window)

glfw.terminate()
