#Copyright (c) 2017 William Emerison Six
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import ctypes.util
from ctypes import (Structure, POINTER, CFUNCTYPE, byref, c_char_p, c_int, c_short,
                    c_uint, c_double, c_float, c_ushort, c_byte, c_ubyte)
import glfw
import inspect
pwd = os.path.dirname(os.path.abspath(__file__))

# nuklear needs to uniquely identify widgets, and one
# way to do so is to inspect the function caller's frame info
# such as filename and line number.
#
# since callerFrameInfo is a function, we need the frame info
# from the caller which is two back.
def callerFrameInfo():
    previous_frame = inspect.currentframe().f_back.f_back
    return inspect.getframeinfo(previous_frame)

# Load it
_nuklear = ctypes.CDLL(os.path.join(pwd, '..', 'contrib', 'nuklear', 'nuklear.so'))



class Context(Structure): pass

class Color(Structure):
    _fields_ = [ ('r',  c_ubyte),
                 ('g',  c_ubyte),
                 ('b',  c_ubyte),
                 ('a',  c_ubyte)]

    def __init__(self,r,g,b,a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

class ColorF(Structure):
    _fields_ = [ ('r',  c_float),
                 ('g',  c_float),
                 ('b',  c_float),
                 ('a',  c_float)]

    def __init__(self,r,g,b,a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a


class Vec2(Structure):
    _fields_ = [ ('x',  c_float),
                 ('y',  c_float)]

    def __init__(self,x,y):
        self.x = x
        self.y = y


class Vec2i(Structure):
    _fields_ = [ ('x',  c_short),
                 ('y',  c_short)]

    def __init__(self,x,y):
        self.x = x
        self.y = y



class Rect(Structure):
    _fields_ = [ ('x',  c_float),
                 ('y',  c_float),
                 ('w',  c_float),
                 ('h',  c_float)]

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class Recti(Structure):
    _fields_ = [ ('x',  c_short),
                 ('y',  c_short),
                 ('w',  c_short),
                 ('h',  c_short)]

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


# TODO - figure out if there is a void pointer type
Handle = POINTER(c_int)

class Image(Structure):
    _fields_ = [ ('handle', Handle),
                 ('w',  c_short),
                 ('h',  c_short),
                 ('region',  c_int)]

    def __init__(self,handle,w,h,region):
        self.handle = handle
        self.w = w
        self.h = h
        self.region = region

class Cursor(Structure):
    _fields_ = [ ('img', Image),
                 ('size',  Vec2),
                 ('offset', Vec2)]

    def __init__(self,image,size,offset):
        self.image = image
        self.size = size
        self.offset = offset

class Scroll(Structure):
    _fields_ = [ ('x', c_int),
                 ('y',  c_int)]

    def __init__(self,x,y):
        self.x = x
        self.y = y

UP=0
RIGHT=1
DOWN=2
LEFT=3

BUTTON_DEFAULT=0
BUTTON_REPEATER=1

FIXED=0
MODIFIABLE=1

VERTICAL=0
HORIZONTAL=1

MINIMIZED=0
MAXIMIZED=1

HIDDEN=0
SHOWN=1

CHART_LINES=0
CHART_COLUMN=1
CHART_MAX=2

CHART_HOVERING=1
CHART_CLICKED=2

RGB = 0
RGBA = 1

POPUP_STATIC=0
POPUP_DYNAMIC=1

DYNAMIC=0
STATIC=1

TREE_NODE=0
TREE_TAB=1

#TODO
# typedef void*(*nk_plugin_alloc)(nk_handle, void *old, nk_size);
# typedef void (*nk_plugin_free)(nk_handle, void *old);
# typedef int(*nk_plugin_filter)(const struct nk_text_edit*, nk_rune unicode);
# typedef void(*nk_plugin_paste)(nk_handle, struct nk_text_edit*);
# typedef void(*nk_plugin_copy)(nk_handle, const char*, int len);

# struct nk_allocator {
#     nk_handle userdata;
#     nk_plugin_alloc alloc;
#     nk_plugin_free free;
# };

SYMBOL_NONE=0
SYMBOL_X=1
SYMBOL_UNDERSCORE=2
SYMBOL_CIRCLE_SOLID=3
SYMBOL_CIRCLE_OUTLINE=4
SYMBOL_RECT_SOLID=5
SYMBOL_RECT_OUTLINE=6
SYMBOL_TRIANGLE_UP=7
SYMBOL_TRIANGLE_DOWN=8
SYMBOL_TRIANGLE_LEFT=9
SYMBOL_TRIANGLE_RIGHT=10
SYMBOL_PLUS=11
SYMBOL_MINUS=12
SYMBOL_MAX=13


# Context
# int nk_init_default(struct nk_context*, const struct nk_user_font*);
# int nk_init_fixed(struct nk_context*, void *memory, nk_size size, const struct nk_user_font*);
# int nk_init(struct nk_context*, struct nk_allocator*, const struct nk_user_font*);
# int nk_init_custom(struct nk_context*, struct nk_buffer *cmds, struct nk_buffer *pool, const struct nk_user_font*);
clear = _nuklear.nk_clear
clear.arglist = [POINTER(Context)]
# void nk_free(struct nk_context*);
# void nk_set_user_data(struct nk_context*, nk_handle handle);

# Input

## Keys
KEY_NONE=0
KEY_SHIFT=1
KEY_CTRL=2
KEY_DEL=3
KEY_ENTER=4
KEY_TAB=5
KEY_BACKSPACE=6
KEY_COPY=7
KEY_CUT=8
KEY_PASTE=9
KEY_UP=10
KEY_DOWN=11
KEY_LEFT=12
KEY_RIGHT=13
KEY_TEXT_INSERT_MODE=14
KEY_TEXT_REPLACE_MODE=15
KEY_TEXT_RESET_MODE=16
KEY_TEXT_LINE_START=17
KEY_TEXT_LINE_END=18
KEY_TEXT_START=19
KEY_TEXT_END=20
KEY_TEXT_UNDO=21
KEY_TEXT_REDO=22
KEY_TEXT_SELECT_ALL=23
KEY_TEXT_WORD_LEFT=24
KEY_TEXT_WORD_RIGHT=25
KEY_SCROLL_START=26
KEY_SCROLL_END=27
KEY_SCROLL_DOWN=28
KEY_SCROLL_UP=29
KEY_MAX=30

## Buttons
BUTTON_LEFT=0
BUTTON_MIDDLE=1
BUTTON_RIGHT=2
BUTTON_DOUBLE=3
BUTTON_MAX=4

#TODO
input_begin = _nuklear.nk_input_begin
input_begin.arglist = [POINTER(Context)]

input_motion = _nuklear.nk_input_motion
input_motion.arglist = [POINTER(Context), c_int, c_int]

input_key = _nuklear.nk_input_key
input_key.arglist = [POINTER(Context), c_int, c_int]

input_button = _nuklear.nk_input_button
input_button.arglist = [POINTER(Context), c_int, c_int, c_int, c_int]

input_scroll = _nuklear.nk_input_scroll
input_scroll.arglist = [POINTER(Context), Vec2]

# TODO
# input_char = _nuklear.nk_input_char
# input_char.arglist = [POINTER(Context), c_char]


# TODO
# input_glyph = _nuklear.nk_input_glyph
# input_glyph.arglist = [POINTER(Context), Glyph]

# TODO
# input_unicode = _nuklear.nk_input_unicode
# input_unicode.arglist = [POINTER(Context, Rune)]

input_end = _nuklear.nk_input_end
input_end.arglist = [POINTER(Context)]

# Drawing
ANTI_ALIASING_OFF=0
ANTI_ALIASING_ON=1

CONVERT_SUCCESS = 0
CONVERT_INVALID_PARAM = 1
CONVERT_COMMAND_BUFFER_FULL = 1 << 0
CONVERT_VERTEX_BUFFER_FULL = 1 << 1
CONVERT_ELEMENT_BUFFER_FULL = 1 << 2


#TODO
# struct nk_draw_null_texture {
#     nk_handle texture; /* texture handle to a texture with a white pixel */
#     struct nk_vec2 uv; /* coordinates to a white pixel in the texture  */
# };
# struct nk_convert_config {
#     float global_alpha; /* global alpha value */
#     enum nk_anti_aliasing line_AA; /* line anti-aliasing flag can be turned off if you are tight on memory */
#     enum nk_anti_aliasing shape_AA; /* shape anti-aliasing flag can be turned off if you are tight on memory */
#     unsigned circle_segment_count; /* number of segments used for circles: default to 22 */
#     unsigned arc_segment_count; /* number of segments used for arcs: default to 22 */
#     unsigned curve_segment_count; /* number of segments used for curves: default to 22 */
#     struct nk_draw_null_texture null; /* handle to texture with a white pixel for shape drawing */
#     const struct nk_draw_vertex_layout_element *vertex_layout; /* describes the vertex output format and packing */
#     nk_size vertex_size; /* sizeof one vertex for vertex packing */
#     nk_size vertex_alignment; /* vertex alignment: Can be obtained by NK_ALIGNOF */
# };

# const struct nk_command* nk__begin(struct nk_context*);
# const struct nk_command* nk__next(struct nk_context*, const struct nk_command*);
# nk_flags nk_convert(struct nk_context*, struct nk_buffer *cmds, struct nk_buffer *vertices, struct nk_buffer *elements, const struct nk_convert_config*);
# const struct nk_draw_command* nk__draw_begin(const struct nk_context*, const struct nk_buffer*);
# const struct nk_draw_command* nk__draw_end(const struct nk_context*, const struct nk_buffer*);
# const struct nk_draw_command* nk__draw_next(const struct nk_draw_command*, const struct nk_buffer*, const struct nk_context*);


# Window

WINDOW_BORDER            = 1 << 0
WINDOW_MOVABLE           = 1 << 1
WINDOW_SCALABLE          = 1 << 2
WINDOW_CLOSABLE          = 1 << 3
WINDOW_MINIMIZABLE       = 1 << 4
WINDOW_NO_SCROLLBAR      = 1 << 5
WINDOW_TITLE             = 1 << 6
WINDOW_SCROLL_AUTO_HIDE  = 1 << 7
WINDOW_BACKGROUND        = 1 << 8
WINDOW_SCALE_LEFT        = 1 << 9
WINDOW_NO_INPUT          = 1 << 10

wrapped_begin = _nuklear.nk_begin
wrapped_begin.arglist = [POINTER(Context), c_char_p, Rect, c_uint]
wrapped_begin.restype = c_int

def begin(ctx, title, bounds, flags):
    return wrapped_begin(ctx, str.encode(title), bounds, flags)

# c_int nk_begin_titled(POINTER(Context), c_char_p name, c_char_p title, Rect bounds, c_int flags);
end            = _nuklear.nk_end
end.arglist    = [POINTER(Context)]
# struct nk_window *nk_window_find(POINTER(Context), c_char_p name);
window_get_bounds = _nuklear.nk_window_get_bounds
window_get_bounds.arglist = [POINTER(Context)]
window_get_bounds.restype = Rect

window_get_position = _nuklear.nk_window_get_position
window_get_position.arglist = [POINTER(Context)]
window_get_position.restype = Vec2

window_get_size = _nuklear.nk_window_get_size
window_get_size.arglist = [POINTER(Context)]
window_get_size.restype = Vec2

window_get_width = _nuklear.nk_window_get_width
window_get_width.arglist = [POINTER(Context)]
window_get_width.restype = c_float

window_get_height = _nuklear.nk_window_get_height
window_get_height.arglist = [POINTER(Context)]
window_get_height.restype = c_float

# struct nk_panel* nk_window_get_panel(POINTER(Context));

nk_window_get_content_region = _nuklear.nk_window_get_content_region
nk_window_get_content_region.arglist = [POINTER(Context)]
nk_window_get_content_region.restype = Rect

nk_window_get_content_region_min = _nuklear.nk_window_get_content_region_min
nk_window_get_content_region_min.arglist = [POINTER(Context)]
nk_window_get_content_region_min.restype = Vec2

nk_window_get_content_region_max = _nuklear.nk_window_get_content_region_max
nk_window_get_content_region_max.arglist = [POINTER(Context)]
nk_window_get_content_region_max.restype = Vec2

# Vec2 nk_window_get_content_region_size(POINTER(Context));
# struct nk_command_buffer* nk_window_get_canvas(POINTER(Context));

window_has_focus = _nuklear.nk_window_has_focus
window_has_focus.arglist = [POINTER(Context)]
window_has_focus.restype = c_int

window_is_collapsed = _nuklear.nk_window_is_collapsed
window_is_collapsed.arglist = [POINTER(Context), c_char_p]
window_is_collapsed.restype = c_int

window_is_closed = _nuklear.nk_window_is_closed
window_is_closed.arglist = [POINTER(Context), c_char_p]
window_is_closed.restype = c_int

window_is_hidden = _nuklear.nk_window_is_hidden
window_is_hidden.arglist = [POINTER(Context), c_char_p]
window_is_hidden.restype = c_int

window_is_active = _nuklear.nk_window_is_active
window_is_active.arglist = [POINTER(Context), c_char_p]
window_is_active.restype = c_int

window_is_hovered = _nuklear.nk_window_is_hovered
window_is_hovered.arglist = [POINTER(Context)]
window_is_hovered.restype = c_int

window_is_any_hovered = _nuklear.nk_window_is_any_hovered
window_is_any_hovered.arglist = [POINTER(Context)]
window_is_any_hovered.restype = c_int


item_is_any_active = _nuklear.nk_item_is_any_active
item_is_any_active.arglist = [POINTER(Context)]
item_is_any_active.restype = c_int

window_set_bounds = _nuklear.nk_window_set_bounds
window_set_bounds.arglist = [POINTER(Context), c_char_p, Rect]

window_set_position = _nuklear.nk_window_set_position
window_set_position.arglist = [POINTER(Context), c_char_p, Vec2]

window_set_size = _nuklear.nk_window_set_size
window_set_size.arglist = [POINTER(Context), c_char_p, Vec2]

window_set_focus = _nuklear.nk_window_set_focus
window_set_focus.arglist = [POINTER(Context), c_char_p]

window_close = _nuklear.nk_window_close
window_close.arglist = [POINTER(Context), c_char_p]

window_collapse = _nuklear.nk_window_collapse
window_collapse.arglist = [POINTER(Context), c_char_p, c_int]

window_collapse_if = _nuklear.nk_window_collapse_if
window_collapse_if.arglist = [POINTER(Context), c_char_p, c_int, c_int]

window_show = _nuklear.nk_window_show
window_show.arglist = [POINTER(Context), c_char_p, c_int]

window_show_if = _nuklear.nk_window_show_if
window_show_if.arglist = [POINTER(Context), c_char_p, c_int, c_int]

# Layout
layout_set_min_row_height = _nuklear.nk_layout_set_min_row_height
layout_set_min_row_height.arglist = [POINTER(Context), c_float]

layout_reset_min_row_height = _nuklear.nk_layout_reset_min_row_height
layout_reset_min_row_height.arglist = [POINTER(Context)]

layout_widget_bounds = _nuklear.nk_layout_widget_bounds
layout_widget_bounds.arglist = [POINTER(Context)]
layout_widget_bounds.restype = Rect

layout_ratio_from_pixel = _nuklear.nk_layout_ratio_from_pixel
layout_ratio_from_pixel.arglist = [POINTER(Context), c_float]
layout_ratio_from_pixel.restype = c_float

wrapped_layout_row_dynamic = _nuklear.nk_layout_row_dynamic
wrapped_layout_row_dynamic.arglist = [POINTER(Context), c_float, c_int]

def layout_row_dynamic(ctx,height,cols):
    wrapped_layout_row_dynamic(ctx,ctypes.c_float(height), cols)

wrapped_layout_row_static = _nuklear.nk_layout_row_static
wrapped_layout_row_static.arglist = [POINTER(Context), c_float, c_int, c_int]

def layout_row_static(ctx,height,item_width,cols):
    wrapped_layout_row_static(ctx,ctypes.c_float(height), item_width,cols)


layout_row_begin = _nuklear.nk_layout_row_begin
layout_row_begin.arglist = [POINTER(Context), c_int, c_float, c_int]

layout_row_push = _nuklear.nk_layout_row_push
layout_row_push.arglist = [POINTER(Context), c_float]

layout_row_end = _nuklear.nk_layout_row_end
layout_row_end.arglist = [POINTER(Context)]

#TODO
#layout_row = _nuklear.nk_layout_row
#layout_row.arglist = [POINTER(Context), c_int, c_float, c_int, const c_float *ratio]

layout_row_template_begin = _nuklear.nk_layout_row_template_begin
layout_row_template_begin.arglist = [POINTER(Context), c_float]

layout_row_template_push_dynamic = _nuklear.nk_layout_row_template_push_dynamic
layout_row_template_push_dynamic.arglist = [POINTER(Context)]

layout_row_template_push_variable = _nuklear.nk_layout_row_template_push_variable
layout_row_template_push_variable.arglist = [POINTER(Context), c_float ]

layout_row_template_push_static = _nuklear.nk_layout_row_template_push_static
layout_row_template_push_static.arglist = [POINTER(Context), c_float]

layout_row_template_end = _nuklear.nk_layout_row_template_end
layout_row_template_end.arglist = [POINTER(Context)]

layout_space_begin = _nuklear.nk_layout_space_begin
layout_space_begin.arglist = [POINTER(Context), c_int, c_float, c_int]

layout_space_push = _nuklear.nk_layout_space_push
layout_space_push.arglist = [POINTER(Context), Rect]

layout_space_end = _nuklear.nk_layout_space_end
layout_space_end.arglist = [POINTER(Context)]

layout_space_bounds = _nuklear.nk_layout_space_bounds
layout_space_bounds.arglist = [POINTER(Context)]
layout_space_bounds.restype = Rect

layout_space_to_screen = _nuklear.nk_layout_space_to_screen
layout_space_to_screen.arglist = [POINTER(Context), Vec2]
layout_space_to_screen.restype = Vec2

layout_space_to_local = _nuklear.nk_layout_space_to_local
layout_space_to_local.arglist = [POINTER(Context), Vec2]
layout_space_to_local.restype = Vec2

layout_space_rect_to_screen = _nuklear.nk_layout_space_rect_to_screen
layout_space_rect_to_screen.arglist = [POINTER(Context), Rect]
layout_space_rect_to_screen.restype = Rect

layout_space_rect_to_local = _nuklear.nk_layout_space_rect_to_local
layout_space_rect_to_local.arglist = [POINTER(Context), Rect]
layout_space_rect_to_local.restype = Rect



# Group
# int nk_group_begin(struct nk_context*, const char *title, nk_flags);
# int nk_group_scrolled_offset_begin(struct nk_context*, nk_uint *x_offset, nk_uint *y_offset, const char*, nk_flags);
# int nk_group_scrolled_begin(struct nk_context*, struct nk_scroll*, const char *title, nk_flags);
# void nk_group_scrolled_end(struct nk_context*);
# void nk_group_end(struct nk_context*);


# List View

# struct nk_list_view {
# /* public: */
#     int begin, end, count;
# /* private: */
#     int total_height;
#     struct nk_context *ctx;
#     nk_uint *scroll_pointer;
#     nk_uint scroll_value;
# };
# int nk_list_view_begin(struct nk_context*, struct nk_list_view *out, const char *id, nk_flags, int row_height, int row_count);
# void nk_list_view_end(struct nk_list_view*);

# Tree
tree_push_hashed = _nuklear.nk_tree_push_hashed
tree_push_hashed.arglist = [POINTER(Context), c_int, c_char_p, c_int, c_char_p,c_int,c_int]
tree_push_hashed.restype = c_int

def tree_push(ctx, theType, title, state):
    (filename, line_number,
     function_name, lines, index) = callerFrameInfo()
    return tree_push_hashed(ctx, theType, str.encode(title), state, filename, len(filename),line_number)


# int nk_tree_image_push_hashed(struct nk_context*, enum nk_tree_type, struct nk_image, const char *title, enum nk_collapse_states initial_state, const char *hash, int len,int seed);

tree_pop = _nuklear.nk_tree_pop
tree_pop.arglist = [POINTER(Context)]

# int nk_tree_state_push(struct nk_context*, enum nk_tree_type, const char *title, enum nk_collapse_states *state);
# int nk_tree_state_image_push(struct nk_context*, enum nk_tree_type, struct nk_image, const char *title, enum nk_collapse_states *state);
# void nk_tree_state_pop(struct nk_context*);

# Widget

WIDGET_INVALID=0
WIDGET_VALID=1
WIDGET_ROM=2


WIDGET_STATE_MODIFIED    = 1 << 0
WIDGET_STATE_INACTIVE    = 1 << 1
WIDGET_STATE_ENTERED     = 1 << 2
WIDGET_STATE_HOVER       = 1 << 3
WIDGET_STATE_ACTIVED     = 1 << 4
WIDGET_STATE_LEFT        = 1 << 5
WIDGET_STATE_HOVERED     = WIDGET_STATE_HOVER|WIDGET_STATE_MODIFIED
WIDGET_STATE_ACTIVE      = WIDGET_STATE_ACTIVED|WIDGET_STATE_MODIFIED


# enum nk_widget_layout_states nk_widget(struct nk_rect*, const struct nk_context*);
# enum nk_widget_layout_states nk_widget_fitting(struct nk_rect*, struct nk_context*, struct nk_vec2);
# struct nk_rect nk_widget_bounds(struct nk_context*);
# struct nk_vec2 nk_widget_position(struct nk_context*);
# struct nk_vec2 nk_widget_size(struct nk_context*);
widget_width = _nuklear.nk_widget_width
widget_width.arglist = [POINTER(Context)]
widget_width.restype = c_float

widget_height = _nuklear.nk_widget_height
widget_height.arglist = [POINTER(Context)]
widget_height.restype = c_float
# int nk_widget_is_hovered(struct nk_context*);
# int nk_widget_is_mouse_clicked(struct nk_context*, enum nk_buttons);
# int nk_widget_has_mouse_click_down(struct nk_context*, enum nk_buttons, int down);
# void nk_spacing(struct nk_context*, int cols);


# Text

TEXT_ALIGN_LEFT        = 1
TEXT_ALIGN_CENTERED    = 2
TEXT_ALIGN_RIGHT       = 4
TEXT_ALIGN_TOP         = 8
TEXT_ALIGN_MIDDLE      = 10
TEXT_ALIGN_BOTTOM      = 20

TEXT_LEFT        = TEXT_ALIGN_MIDDLE|TEXT_ALIGN_LEFT
TEXT_CENTERED    = TEXT_ALIGN_MIDDLE|TEXT_ALIGN_CENTERED
TEXT_RIGHT       = TEXT_ALIGN_MIDDLE|TEXT_ALIGN_RIGHT


wrapped_text = _nuklear.nk_text
wrapped_text.arglist = [POINTER(Context), c_char_p, c_int, c_int]

def text(ctx, text, length, alignment):
    wrapped_text(ctx,str.encode(text),length, alignment)

# void nk_text_colored(struct nk_context*, const char*, int, nk_flags, struct nk_color);
# void nk_text_wrap(struct nk_context*, const char*, int);
# void nk_text_wrap_colored(struct nk_context*, const char*, int, struct nk_color);

wrapped_label = _nuklear.nk_label
wrapped_label.arglist = [POINTER(Context), c_char_p, c_uint]

def label(ctx, text, alignment):
    wrapped_label(ctx, str.encode(text), alignment)

wrapped_label_colored = _nuklear.nk_label_colored
wrapped_label_colored.arglist = [POINTER(Context), c_char_p, c_int, Color]

def label_colored(ctx, text, align, color):
    wrapped_label_colored(ctx,str.encode(text),align,color)

wrapped_label_wrap = _nuklear.nk_label_wrap
wrapped_label_wrap.arglist = [POINTER(Context), c_char_p]

def label_wrap(ctx, text):
    wrapped_label_wrap(ctx,str.encode(text))

# void nk_label_colored_wrap(struct nk_context*, const char*, struct nk_color);
# void nk_image(struct nk_context*, struct nk_image);
# void nk_labelf(struct nk_context*, nk_flags, const char*, ...);
# void nk_labelf_colored(struct nk_context*, nk_flags align, struct nk_color, const char*,...);
# void nk_labelf_wrap(struct nk_context*, const char*,...);
# void nk_labelf_colored_wrap(struct nk_context*, struct nk_color, const char*,...);
# void nk_value_bool(struct nk_context*, const char *prefix, int);
# void nk_value_int(struct nk_context*, const char *prefix, int);
# void nk_value_uint(struct nk_context*, const char *prefix, unsigned int);
# void nk_value_float(struct nk_context*, const char *prefix, float);
# void nk_value_color_byte(struct nk_context*, const char *prefix, struct nk_color);
# void nk_value_color_float(struct nk_context*, const char *prefix, struct nk_color);
# void nk_value_color_hex(struct nk_context*, const char *prefix, struct nk_color);


# Button

# int nk_button_text(struct nk_context*, const char *title, int len);
wrapped_button_label = _nuklear.nk_button_label
wrapped_button_label.arglist = [POINTER(Context), c_char_p]
wrapped_button_label.restype     = c_int

def button_label(ctx, title):
    return wrapped_button_label(ctx, str.encode(title))

# int nk_button_color(struct nk_context*, struct nk_color);
# int nk_button_symbol(struct nk_context*, enum nk_symbol_type);
# int nk_button_image(struct nk_context*, struct nk_image img);
# int nk_button_symbol_label(struct nk_context*, enum nk_symbol_type, const char*, nk_flags text_alignment);
# int nk_button_symbol_text(struct nk_context*, enum nk_symbol_type, const char*, int, nk_flags alignment);
# int nk_button_image_label(struct nk_context*, struct nk_image img, const char*, nk_flags text_alignment);
# int nk_button_image_text(struct nk_context*, struct nk_image img, const char*, int, nk_flags alignment);
# int nk_button_text_styled(struct nk_context*, const struct nk_style_button*, const char *title, int len);
# int nk_button_label_styled(struct nk_context*, const struct nk_style_button*, const char *title);
# int nk_button_symbol_styled(struct nk_context*, const struct nk_style_button*, enum nk_symbol_type);
# int nk_button_image_styled(struct nk_context*, const struct nk_style_button*, struct nk_image img);
# int nk_button_symbol_text_styled(struct nk_context*,const struct nk_style_button*, enum nk_symbol_type, const char*, int, nk_flags alignment);
# int nk_button_symbol_label_styled(struct nk_context *ctx, const struct nk_style_button *style, enum nk_symbol_type symbol, const char *title, nk_flags align);
# int nk_button_image_label_styled(struct nk_context*,const struct nk_style_button*, struct nk_image img, const char*, nk_flags text_alignment);
# int nk_button_image_text_styled(struct nk_context*,const struct nk_style_button*, struct nk_image img, const char*, int, nk_flags alignment);
# void nk_button_set_behavior(struct nk_context*, enum nk_button_behavior);
# int nk_button_push_behavior(struct nk_context*, enum nk_button_behavior);
# int nk_button_pop_behavior(struct nk_context*);


# Checkbox
# int nk_check_label(struct nk_context*, const char*, int active);
# int nk_check_text(struct nk_context*, const char*, int,int active);
# unsigned nk_check_flags_label(struct nk_context*, const char*, unsigned int flags, unsigned int value);
# unsigned nk_check_flags_text(struct nk_context*, const char*, int, unsigned int flags, unsigned int value);

wrapped_checkbox_label = _nuklear.nk_checkbox_label
wrapped_checkbox_label.arglist = [POINTER(Context), c_char_p, POINTER(c_int)]
wrapped_checkbox_label.restype = c_int

def checkbox_label(ctx, text, active):
    a = ctypes.c_int(active)
    wasModified = wrapped_checkbox_label(ctx,str.encode(text),ctypes.byref(a))
    return (a.value, wasModified)


# int nk_checkbox_text(struct nk_context*, const char*, int, int *active);
# int nk_checkbox_flags_label(struct nk_context*, const char*, unsigned int *flags, unsigned int value);
# int nk_checkbox_flags_text(struct nk_context*, const char*, int, unsigned int *flags, unsigned int value);


# Radio Button

# int nk_radio_label(struct nk_context*, const char*, int *active);
# int nk_radio_text(struct nk_context*, const char*, int, int *active);

wrapped_option_label = _nuklear.nk_option_label
wrapped_option_label.arglist = [POINTER(Context), c_char_p, c_int]
wrapped_option_label.restype = c_int

def option_label(ctx, label, active):
    return wrapped_option_label(ctx, str.encode(label), active)

# int nk_option_text(struct nk_context*, const char*, int, int active);
# int nk_selectable_label(struct nk_context*, const char*, nk_flags align, int *value);


# Selectable
# int nk_selectable_label(struct nk_context*, const char*, nk_flags align, int *value);
# int nk_selectable_text(struct nk_context*, const char*, int, nk_flags align, int *value);
# int nk_selectable_image_label(struct nk_context*,struct nk_image,  const char*, nk_flags align, int *value);
# int nk_selectable_image_text(struct nk_context*,struct nk_image, const char*, int, nk_flags align, int *value);
# int nk_select_label(struct nk_context*, const char*, nk_flags align, int value);
# int nk_select_text(struct nk_context*, const char*, int, nk_flags align, int value);
# int nk_select_image_label(struct nk_context*, struct nk_image,const char*, nk_flags align, int value);
# int nk_select_image_text(struct nk_context*, struct nk_image,const char*, int, nk_flags align, int value);


# Slider
# float nk_slide_float(struct nk_context*, float min, float val, float max, float step);
# int nk_slide_int(struct nk_context*, int min, int val, int max, int step);
# int nk_slider_float(struct nk_context*, float min, float *val, float max, float step);

wrapped_slider_int = _nuklear.nk_slider_int
wrapped_slider_int.arglist = [POINTER(Context), c_int, POINTER(c_int), c_int, c_int]
wrapped_slider_int.restype = c_int

def slider_int(ctx, minV, value, maxV, step):
    v = ctypes.c_int(value)
    wasModified = wrapped_slider_int(ctx, minV, ctypes.byref(v), maxV, step)
    return (v.value, wasModified)


wrapped_progress = _nuklear.nk_progress
wrapped_progress.arglist = [POINTER(Context), POINTER(c_int), c_int, c_int]
wrapped_progress.restype = c_int

def progress(ctx, cur, max, is_modifyable):
    v = ctypes.c_int(cur)
    wasModified = wrapped_progress(ctx, ctypes.byref(v), max, is_modifyable)
    return (v.value, wasModified)

# ProgressBar
# int nk_progress(struct nk_context*, nk_size *cur, nk_size max, int modifyable);
# nk_size nk_prog(struct nk_context*, nk_size cur, nk_size max, int modifyable);

# ColorPicker#
color_picker = _nuklear.nk_color_picker
color_picker.arglist = [POINTER(Context), Color, c_int]
color_picker.restype = Color
# int nk_color_pick(struct nk_context*, struct nk_color*, enum nk_color_format);


# Properties

wrapped_property_int = _nuklear.nk_property_int
wrapped_property_int.arglist = [POINTER(Context), c_char_p, c_int, c_int, c_int, c_int, c_float]

def property_int(ctx, name, minV, val, maxV, step, inc_per_pixel):
    v = ctypes.c_int(val)
    wrapped_property_int(ctx,str.encode(name),minV, ctypes.byref(v),maxV, step, inc_per_pixel)
    return v.value

# void nk_property_float(struct nk_context*, const char *name, float min, float *val, float max, float step, float inc_per_pixel);
# void nk_property_double(struct nk_context*, const char *name, double min, double *val, double max, double step, float inc_per_pixel);

wrapped_propertyi = _nuklear.nk_propertyi
wrapped_propertyi.arglist = [POINTER(Context), c_char_p, c_int, c_int, c_int, c_int, c_float]
wrapped_propertyi.restype = c_int

def propertyi(ctx, name, minVal, val, maxVal, step, inc_per_pixel):
    return wrapped_propertyi(ctx,
                             str.encode(name),
                             minVal,
                             val,
                             maxVal,
                             step,
                             ctypes.c_float(inc_per_pixel))


# float nk_propertyf(struct nk_context*, const char *name, float min, float val, float max, float step, float inc_per_pixel);
# double nk_propertyd(struct nk_context*, const char *name, double min, double val, double max, double step, float inc_per_pixel);


# TextEdit

EDIT_DEFAULT                 = 0,
EDIT_READ_ONLY               = 1 << 0
EDIT_AUTO_SELECT             = 1 << 1
EDIT_SIG_ENTER               = 1 << 2
EDIT_ALLOW_TAB               = 1 << 3
EDIT_NO_CURSOR               = 1 << 4
EDIT_SELECTABLE              = 1 << 5
EDIT_CLIPBOARD               = 1 << 6
EDIT_CTRL_ENTER_NEWLINE      = 1 << 7
EDIT_NO_HORIZONTAL_SCROLL    = 1 << 8
EDIT_ALWAYS_INSERT_MODE      = 1 << 9
EDIT_MULTILINE               = 1 << 10
EDIT_GOTO_END_ON_ACTIVATE    = 1 << 11


EDIT_SIMPLE  = EDIT_ALWAYS_INSERT_MODE
EDIT_FIELD   = EDIT_SIMPLE|EDIT_SELECTABLE|EDIT_CLIPBOARD
EDIT_BOX     = EDIT_ALWAYS_INSERT_MODE| EDIT_SELECTABLE| EDIT_MULTILINE|EDIT_ALLOW_TAB|EDIT_CLIPBOARD
EDIT_EDITOR  = EDIT_SELECTABLE|EDIT_MULTILINE|EDIT_ALLOW_TAB| EDIT_CLIPBOARD


EDIT_ACTIVE      = 1 << 0
EDIT_INACTIVE    = 1 << 1
EDIT_ACTIVATED   = 1 << 2
EDIT_DEACTIVATED = 1 << 3
EDIT_COMMITED    = 1 << 4


# nk_flags nk_edit_string(struct nk_context*, nk_flags, char *buffer, int *len, int max, nk_plugin_filter);
# nk_flags nk_edit_string_zero_terminated(struct nk_context*, nk_flags, char *buffer, int max, nk_plugin_filter);
# nk_flags nk_edit_buffer(struct nk_context*, nk_flags, struct nk_text_edit*, nk_plugin_filter);
# void nk_edit_focus(struct nk_context*, nk_flags flags);
# void nk_edit_unfocus(struct nk_context*);

# Chart
# int nk_chart_begin(struct nk_context*, enum nk_chart_type, int num, float min, float max);
# int nk_chart_begin_colored(struct nk_context*, enum nk_chart_type, struct nk_color, struct nk_color active, int num, float min, float max);
# void nk_chart_add_slot(struct nk_context *ctx, const enum nk_chart_type, int count, float min_value, float max_value);
# void nk_chart_add_slot_colored(struct nk_context *ctx, const enum nk_chart_type, struct nk_color, struct nk_color active, int count, float min_value, float max_value);
# nk_flags nk_chart_push(struct nk_context*, float);
# nk_flags nk_chart_push_slot(struct nk_context*, float, int);
# void nk_chart_end(struct nk_context*);
# void nk_plot(struct nk_context*, enum nk_chart_type, const float *values, int count, int offset);
# void nk_plot_function(struct nk_context*, enum nk_chart_type, void *userdata, float(*value_getter)(void* user, int index), int count, int offset);


# Popup

wrapped_popup_begin = _nuklear.nk_popup_begin
wrapped_popup_begin.arglist= [POINTER(Context), c_int, c_char_p, c_int,Rect]
wrapped_popup_begin.restype = c_int

def popup_begin(ctx, theType, title, flags, rect):
    return wrapped_popup_begin(ctx, theType, str.encode(title), flags, rect)

# void nk_popup_close(struct nk_context*);

popup_end = _nuklear.nk_popup_end
popup_end.arglist= [POINTER(Context)]


# void nk_popup_end(struct nk_context*);


# ComboBox
# int nk_combo(struct nk_context*, const char **items, int count, int selected, int item_height, struct nk_vec2 size);
# int nk_combo_separator(struct nk_context*, const char *items_separated_by_separator, int separator, int selected, int count, int item_height, struct nk_vec2 size);
# int nk_combo_string(struct nk_context*, const char *items_separated_by_zeros, int selected, int count, int item_height, struct nk_vec2 size);
# int nk_combo_callback(struct nk_context*, void(*item_getter)(void*, int, const char**), void *userdata, int selected, int count, int item_height, struct nk_vec2 size);
# void nk_combobox(struct nk_context*, const char **items, int count, int *selected, int item_height, struct nk_vec2 size);
# void nk_combobox_string(struct nk_context*, const char *items_separated_by_zeros, int *selected, int count, int item_height, struct nk_vec2 size);
# void nk_combobox_separator(struct nk_context*, const char *items_separated_by_separator, int separator,int *selected, int count, int item_height, struct nk_vec2 size);
# void nk_combobox_callback(struct nk_context*, void(*item_getter)(void*, int, const char**), void*, int *selected, int count, int item_height, struct nk_vec2 size);


# Abstract Combobox
# int nk_combo_begin_text(struct nk_context*, const char *selected, int, struct nk_vec2 size);
# int nk_combo_begin_label(struct nk_context*, const char *selected, struct nk_vec2 size);
combo_begin_color = _nuklear.nk_combo_begin_color
combo_begin_color.arglist = [POINTER(Context), Color, Vec2]
combo_begin_color.restype = c_int
# int nk_combo_begin_symbol(struct nk_context*,  enum nk_symbol_type,  struct nk_vec2 size);
# int nk_combo_begin_symbol_label(struct nk_context*, const char *selected, enum nk_symbol_type, struct nk_vec2 size);
# int nk_combo_begin_symbol_text(struct nk_context*, const char *selected, int, enum nk_symbol_type, struct nk_vec2 size);
# int nk_combo_begin_image(struct nk_context*, struct nk_image img,  struct nk_vec2 size);
# int nk_combo_begin_image_label(struct nk_context*, const char *selected, struct nk_image, struct nk_vec2 size);
# int nk_combo_begin_image_text(struct nk_context*,  const char *selected, int, struct nk_image, struct nk_vec2 size);
# int nk_combo_item_label(struct nk_context*, const char*, nk_flags alignment);
# int nk_combo_item_text(struct nk_context*, const char*,int, nk_flags alignment);
# int nk_combo_item_image_label(struct nk_context*, struct nk_image, const char*, nk_flags alignment);
# int nk_combo_item_image_text(struct nk_context*, struct nk_image, const char*, int,nk_flags alignment);
# int nk_combo_item_symbol_label(struct nk_context*, enum nk_symbol_type, const char*, nk_flags alignment);
# int nk_combo_item_symbol_text(struct nk_context*, enum nk_symbol_type, const char*, int, nk_flags alignment);
# void nk_combo_close(struct nk_context*);
combo_end = _nuklear.nk_combo_end
combo_end.arglist = [POINTER(Context)]

# Contextual
# int nk_contextual_begin(struct nk_context*, nk_flags, struct nk_vec2, struct nk_rect trigger_bounds);
# int nk_contextual_item_text(struct nk_context*, const char*, int,nk_flags align);
# int nk_contextual_item_label(struct nk_context*, const char*, nk_flags align);
# int nk_contextual_item_image_label(struct nk_context*, struct nk_image, const char*, nk_flags alignment);
# int nk_contextual_item_image_text(struct nk_context*, struct nk_image, const char*, int len, nk_flags alignment);
# int nk_contextual_item_symbol_label(struct nk_context*, enum nk_symbol_type, const char*, nk_flags alignment);
# int nk_contextual_item_symbol_text(struct nk_context*, enum nk_symbol_type, const char*, int, nk_flags alignment);
# void nk_contextual_close(struct nk_context*);
# void nk_contextual_end(struct nk_context*);


# Tooltip
# void nk_tooltip(struct nk_context*, const char*);
# void nk_tooltipf(struct nk_context*, const char*, ...);
# int nk_tooltip_begin(struct nk_context*, float width);
# void nk_tooltip_end(struct nk_context*);


# Menu
menubar_begin = _nuklear.nk_menubar_begin
menubar_begin.arglist = [POINTER(Context)]

menubar_end = _nuklear.nk_menubar_end
menubar_end.arglist = [POINTER(Context)]

# int nk_menu_begin_text(struct nk_context*, const char* title, int title_len, nk_flags align, struct nk_vec2 size);

wrapped_menu_begin_label = _nuklear.nk_menu_begin_label
wrapped_menu_begin_label.arglist = [POINTER(Context), c_char_p, c_int, Vec2]
wrapped_menu_begin_label.restype = c_int

def menu_begin_label(ctx,text,align,size):
    return wrapped_menu_begin_label(ctx,str.encode(text),align,size)


# int nk_menu_begin_image(struct nk_context*, const char*, struct nk_image, struct nk_vec2 size);
# int nk_menu_begin_image_text(struct nk_context*, const char*, int,nk_flags align,struct nk_image, struct nk_vec2 size);
# int nk_menu_begin_image_label(struct nk_context*, const char*, nk_flags align,struct nk_image, struct nk_vec2 size);
# int nk_menu_begin_symbol(struct nk_context*, const char*, enum nk_symbol_type, struct nk_vec2 size);
# int nk_menu_begin_symbol_text(struct nk_context*, const char*, int,nk_flags align,enum nk_symbol_type, struct nk_vec2 size);
# int nk_menu_begin_symbol_label(struct nk_context*, const char*, nk_flags align,enum nk_symbol_type, struct nk_vec2 size);
# int nk_menu_item_text(struct nk_context*, const char*, int,nk_flags align);

wrapped_menu_item_label = _nuklear.nk_menu_item_label
wrapped_menu_item_label.arglist = [POINTER(Context), c_char_p, c_int]
wrapped_menu_item_label.restype = c_int

def menu_item_label(ctx, label, align):
    return wrapped_menu_item_label(ctx,str.encode(label), align)

# int nk_menu_item_image_label(struct nk_context*, struct nk_image, const char*, nk_flags alignment);
# int nk_menu_item_image_text(struct nk_context*, struct nk_image, const char*, int len, nk_flags alignment);
# int nk_menu_item_symbol_text(struct nk_context*, enum nk_symbol_type, const char*, int, nk_flags alignment);
# int nk_menu_item_symbol_label(struct nk_context*, enum nk_symbol_type, const char*, nk_flags alignment);
# void nk_menu_close(struct nk_context*);

menu_end = _nuklear.nk_menu_end
menu_end.arglist = [POINTER(Context)]


# Style

COLOR_TEXT=0
COLOR_WINDOW=1
COLOR_HEADER=2
COLOR_BORDER=3
COLOR_BUTTON=4
COLOR_BUTTON_HOVER=5
COLOR_BUTTON_ACTIVE=6
COLOR_TOGGLE=7
COLOR_TOGGLE_HOVER=8
COLOR_TOGGLE_CURSOR=9
COLOR_SELECT=10
COLOR_SELECT_ACTIVE=11
COLOR_SLIDER=12
COLOR_SLIDER_CURSOR=13
COLOR_SLIDER_CURSOR_HOVER=14
COLOR_SLIDER_CURSOR_ACTIVE=15
COLOR_PROPERTY=16
COLOR_EDIT=17
COLOR_EDIT_CURSOR=18
COLOR_COMBO=19
COLOR_CHART=20
COLOR_CHART_COLOR=21
COLOR_CHART_COLOR_HIGHLIGHT=22
COLOR_SCROLLBAR=23
COLOR_SCROLLBAR_CURSOR=24
COLOR_SCROLLBAR_CURSOR_HOVER=25
COLOR_SCROLLBAR_CURSOR_ACTIVE=26
COLOR_TAB_HEADER=27
COLOR_COUNT=28


CURSOR_ARROW=0
CURSOR_TEXT=1
CURSOR_MOVE=2
CURSOR_RESIZE_VERTICAL=3
CURSOR_RESIZE_HORIZONTAL=4
CURSOR_RESIZE_TOP_LEFT_DOWN_RIGHT=5
CURSOR_RESIZE_TOP_RIGHT_DOWN_LEFT=6
CURSOR_COUN=7


# void nk_style_default(struct nk_context*);
# void nk_style_from_table(struct nk_context*, const struct nk_color*);
# void nk_style_load_cursor(struct nk_context*, enum nk_style_cursor, const struct nk_cursor*);
# void nk_style_load_all_cursors(struct nk_context*, struct nk_cursor*);
# const char* nk_style_get_color_by_name(enum nk_style_colors);
# void nk_style_set_font(struct nk_context*, const struct nk_user_font*);
# int nk_style_set_cursor(struct nk_context*, enum nk_style_cursor);
# void nk_style_show_cursor(struct nk_context*);
# void nk_style_hide_cursor(struct nk_context*);
# int nk_style_push_font(struct nk_context*, const struct nk_user_font*);
# int nk_style_push_float(struct nk_context*, float*, float);
# int nk_style_push_vec2(struct nk_context*, struct nk_vec2*, struct nk_vec2);
# int nk_style_push_style_item(struct nk_context*, struct nk_style_item*, struct nk_style_item);
# int nk_style_push_flags(struct nk_context*, nk_flags*, nk_flags);
# int nk_style_push_color(struct nk_context*, struct nk_color*, struct nk_color);
# int nk_style_pop_font(struct nk_context*);
# int nk_style_pop_float(struct nk_context*);
# int nk_style_pop_vec2(struct nk_context*);
# int nk_style_pop_style_item(struct nk_context*);
# int nk_style_pop_flags(struct nk_context*);
# int nk_style_pop_color(struct nk_context*);
# struct nk_color nk_rgb(int r, int g, int b);


# Color
# struct nk_color nk_rgb(int r, int g, int b);
# struct nk_color nk_rgb_iv(const int *rgb);
# struct nk_color nk_rgb_bv(const nk_byte* rgb);
# struct nk_color nk_rgb_f(float r, float g, float b);
# struct nk_color nk_rgb_fv(const float *rgb);
# struct nk_color nk_rgb_hex(const char *rgb);
# struct nk_color nk_rgba(int r, int g, int b, int a);
# struct nk_color nk_rgba_u32(nk_uint);
# struct nk_color nk_rgba_iv(const int *rgba);
# struct nk_color nk_rgba_bv(const nk_byte *rgba);
# struct nk_color nk_rgba_f(float r, float g, float b, float a);
# struct nk_color nk_rgba_fv(const float *rgba);
# struct nk_color nk_rgba_hex(const char *rgb);
# struct nk_color nk_hsv(int h, int s, int v);
# struct nk_color nk_hsv_iv(const int *hsv);
# struct nk_color nk_hsv_bv(const nk_byte *hsv);
# struct nk_color nk_hsv_f(float h, float s, float v);
# struct nk_color nk_hsv_fv(const float *hsv);
# struct nk_color nk_hsva(int h, int s, int v, int a);
# struct nk_color nk_hsva_iv(const int *hsva);
# struct nk_color nk_hsva_bv(const nk_byte *hsva);
# struct nk_color nk_hsva_f(float h, float s, float v, float a);
# struct nk_color nk_hsva_fv(const float *hsva);
# void nk_color_f(float *r, float *g, float *b, float *a, struct nk_color);
# void nk_color_fv(float *rgba_out, struct nk_color);
# void nk_color_d(double *r, double *g, double *b, double *a, struct nk_color);
# void nk_color_dv(double *rgba_out, struct nk_color);
# nk_uint nk_color_u32(struct nk_color);
# void nk_color_hex_rgba(char *output, struct nk_color);
# void nk_color_hex_rgb(char *output, struct nk_color);
# void nk_color_hsv_i(int *out_h, int *out_s, int *out_v, struct nk_color);
# void nk_color_hsv_b(nk_byte *out_h, nk_byte *out_s, nk_byte *out_v, struct nk_color);
# void nk_color_hsv_iv(int *hsv_out, struct nk_color);
# void nk_color_hsv_bv(nk_byte *hsv_out, struct nk_color);
# void nk_color_hsv_f(float *out_h, float *out_s, float *out_v, struct nk_color);
# void nk_color_hsv_fv(float *hsv_out, struct nk_color);
# void nk_color_hsva_i(int *h, int *s, int *v, int *a, struct nk_color);
# void nk_color_hsva_b(nk_byte *h, nk_byte *s, nk_byte *v, nk_byte *a, struct nk_color);
# void nk_color_hsva_iv(int *hsva_out, struct nk_color);
# void nk_color_hsva_bv(nk_byte *hsva_out, struct nk_color);
# void nk_color_hsva_f(float *out_h, float *out_s, float *out_v, float *out_a, struct nk_color);
# void nk_color_hsva_fv(float *hsva_out, struct nk_color);


# Image# nk_handle nk_handle_ptr(void*);
# nk_handle nk_handle_id(int);
# struct nk_image nk_image_handle(nk_handle);
# struct nk_image nk_image_ptr(void*);
# struct nk_image nk_image_id(int);
# int nk_image_is_subimage(const struct nk_image* img);
# struct nk_image nk_subimage_ptr(void*, unsigned short w, unsigned short h, struct nk_rect sub_region);
# struct nk_image nk_subimage_id(int, unsigned short w, unsigned short h, struct nk_rect sub_region);
# struct nk_image nk_subimage_handle(nk_handle, unsigned short w, unsigned short h, struct nk_rect sub_region);


# Math# nk_hash nk_murmur_hash(const void *key, int len, nk_hash seed);
# void nk_triangle_from_direction(struct nk_vec2 *result, struct nk_rect r, float pad_x, float pad_y, enum nk_heading);
# struct nk_vec2 nk_vec2(float x, float y);
# struct nk_vec2 nk_vec2i(int x, int y);
# struct nk_vec2 nk_vec2v(const float *xy);
# struct nk_vec2 nk_vec2iv(const int *xy);
# struct nk_rect nk_get_null_rect(void);
# struct nk_rect nk_rect(float x, float y, float w, float h);
# struct nk_rect nk_recti(int x, int y, int w, int h);
# struct nk_rect nk_recta(struct nk_vec2 pos, struct nk_vec2 size);
# struct nk_rect nk_rectv(const float *xywh);
# struct nk_rect nk_rectiv(const int *xywh);
# struct nk_vec2 nk_rect_pos(struct nk_rect);
# struct nk_vec2 nk_rect_size(struct nk_rect);
# int nk_strlen(const char *str);

# String# int nk_strlen(const char *str);
# int nk_stricmp(const char *s1, const char *s2);
# int nk_stricmpn(const char *s1, const char *s2, int n);
# int nk_strtoi(const char *str, const char **endptr);
# float nk_strtof(const char *str, const char **endptr);
# double nk_strtod(const char *str, const char **endptr);
# int nk_strfilter(const char *text, const char *regexp);
# int nk_strmatch_fuzzy_string(char const *str, char const *pattern, int *out_score);
# int nk_strmatch_fuzzy_text(const char *txt, int txt_len, const char *pattern, int *out_score);

# UTF 8
# int nk_utf_decode(const char*, nk_rune*, int);
# int nk_utf_encode(nk_rune, char*, int);
# int nk_utf_len(const char*, int byte_len);
# const char* nk_utf_at(const char *buffer, int length, int index, nk_rune *unicode, int *len);


# Font

# struct nk_user_font_glyph;
# typedef float(*nk_text_width_f)(nk_handle, float h, const char*, int len);
# typedef void(*nk_query_font_glyph_f)(nk_handle handle, float font_height,
#                                     struct nk_user_font_glyph *glyph,
#                                     nk_rune codepoint, nk_rune next_codepoint);

# #if defined(NK_INCLUDE_VERTEX_BUFFER_OUTPUT) || defined(NK_INCLUDE_SOFTWARE_FONT)
# struct nk_user_font_glyph {
#     struct nk_vec2 uv[2];
#     /* texture coordinates */
#     struct nk_vec2 offset;
#     /* offset between top left and glyph */
#     float width, height;
#     /* size of the glyph  */
#     float xadvance;
#     /* offset to the next glyph */
# };
# #endif

# struct nk_user_font {
#     nk_handle userdata;
#     /* user provided font handle */
#     float height;
#     /* max height of the font */
#     nk_text_width_f width;
#     /* font string width in pixel callback */
# #ifdef NK_INCLUDE_VERTEX_BUFFER_OUTPUT
#     nk_query_font_glyph_f query;
#     /* font glyph callback to query drawing info */
#     nk_handle texture;
#     /* texture handle to the used font atlas or texture */
# #endif
# };

COORD_UV=0
COORD_PIXEL=1


# struct nk_font;
# struct nk_baked_font {
#     float height;
#     /* height of the font  */
#     float ascent, descent;
#     /* font glyphs ascent and descent  */
#     nk_rune glyph_offset;
#     /* glyph array offset inside the font glyph baking output array  */
#     nk_rune glyph_count;
#     /* number of glyphs of this font inside the glyph baking array output */
#     const nk_rune *ranges;
#     /* font codepoint ranges as pairs of (from/to) and 0 as last element */
# };

# struct nk_font_config {
#     struct nk_font_config *next;
#     /* NOTE: only used internally */
#     void *ttf_blob;
#     /* pointer to loaded TTF file memory block.
#      * NOTE: not needed for nk_font_atlas_add_from_memory and nk_font_atlas_add_from_file. */
#     nk_size ttf_size;
#     /* size of the loaded TTF file memory block
#      * NOTE: not needed for nk_font_atlas_add_from_memory and nk_font_atlas_add_from_file. */

#     unsigned char ttf_data_owned_by_atlas;
#     /* used inside font atlas: default to: 0*/
#     unsigned char merge_mode;
#     /* merges this font into the last font */
#     unsigned char pixel_snap;
#     /* align every character to pixel boundary (if true set oversample (1,1)) */
#     unsigned char oversample_v, oversample_h;
#     /* rasterize at hight quality for sub-pixel position */
#     unsigned char padding[3];

#     float size;
#     /* baked pixel height of the font */
#     enum nk_font_coord_type coord_type;
#     /* texture coordinate format with either pixel or UV coordinates */
#     struct nk_vec2 spacing;
#     /* extra pixel spacing between glyphs  */
#     const nk_rune *range;
#     /* list of unicode ranges (2 values per range, zero terminated) */
#     struct nk_baked_font *font;
#     /* font to setup in the baking process: NOTE: not needed for font atlas */
#     nk_rune fallback_glyph;
#     /* fallback glyph to use if a given rune is not found */
#     struct nk_font_config *n;
#     struct nk_font_config *p;
# };

# struct nk_font_glyph {
#     nk_rune codepoint;
#     float xadvance;
#     float x0, y0, x1, y1, w, h;
#     float u0, v0, u1, v1;
# };

# struct nk_font {
#     struct nk_font *next;
#     struct nk_user_font handle;
#     struct nk_baked_font info;
#     float scale;
#     struct nk_font_glyph *glyphs;
#     const struct nk_font_glyph *fallback;
#     nk_rune fallback_codepoint;
#     nk_handle texture;
#     struct nk_font_config *config;
# };

FONT_ATLAS_ALPHA8=0
FONT_ATLAS_RGBA32=1

# struct nk_font_atlas {
#     void *pixel;
#     int tex_width;
#     int tex_height;

#     struct nk_allocator permanent;
#     struct nk_allocator temporary;

#     struct nk_recti custom;
#     struct nk_cursor cursors[NK_CURSOR_COUNT];

#     int glyph_count;
#     struct nk_font_glyph *glyphs;
#     struct nk_font *default_font;
#     struct nk_font *fonts;
#     struct nk_font_config *config;
#     int font_num;
# };

# const nk_rune *nk_font_default_glyph_ranges(void);
# const nk_rune *nk_font_chinese_glyph_ranges(void);
# const nk_rune *nk_font_cyrillic_glyph_ranges(void);
# const nk_rune *nk_font_korean_glyph_ranges(void);
# void nk_font_atlas_init_default(struct nk_font_atlas*);
# void nk_font_atlas_init(struct nk_font_atlas*, struct nk_allocator*);
# void nk_font_atlas_init_custom(struct nk_font_atlas*, struct nk_allocator *persistent, struct nk_allocator *transient);
# void nk_font_atlas_begin(struct nk_font_atlas*);
# struct nk_font_config nk_font_config(float pixel_height);
# struct nk_font *nk_font_atlas_add(struct nk_font_atlas*, const struct nk_font_config*);
# struct nk_font* nk_font_atlas_add_default(struct nk_font_atlas*, float height, const struct nk_font_config*);
# struct nk_font* nk_font_atlas_add_from_memory(struct nk_font_atlas *atlas, void *memory, nk_size size, float height, const struct nk_font_config *config);
# struct nk_font* nk_font_atlas_add_from_file(struct nk_font_atlas *atlas, const char *file_path, float height, const struct nk_font_config*);
# struct nk_font *nk_font_atlas_add_compressed(struct nk_font_atlas*, void *memory, nk_size size, float height, const struct nk_font_config*);
# struct nk_font* nk_font_atlas_add_compressed_base85(struct nk_font_atlas*, const char *data, float height, const struct nk_font_config *config);
# const void* nk_font_atlas_bake(struct nk_font_atlas*, int *width, int *height, enum nk_font_atlas_format);
# void nk_font_atlas_end(struct nk_font_atlas*, nk_handle tex, struct nk_draw_null_texture*);
# const struct nk_font_glyph* nk_font_find_glyph(struct nk_font*, nk_rune unicode);
# void nk_font_atlas_cleanup(struct nk_font_atlas *atlas);
# void nk_font_atlas_clear(struct nk_font_atlas*);


# Memory Buffer

# struct nk_memory_status {
#     void *memory;
#     unsigned int type;
#     nk_size size;
#     nk_size allocated;
#     nk_size needed;
#     nk_size calls;
# };

BUFFER_FIXED=0
BUFFER_DYNAMIC=1

BUFFER_FRONT=0
BUFFER_BACK=1
BUFFER_MAX=2

# struct nk_buffer_marker {
#     int active;
#     nk_size offset;
# };

# struct nk_memory {void *ptr;nk_size size;};
# struct nk_buffer {
#     struct nk_buffer_marker marker[NK_BUFFER_MAX];
#     /* buffer marker to free a buffer to a certain offset */
#     struct nk_allocator pool;
#     /* allocator callback for dynamic buffers */
#     enum nk_allocation_type type;
#     /* memory management type */
#     struct nk_memory memory;
#     /* memory and size of the current memory block */
#     float grow_factor;
#     /* growing factor for dynamic memory management */
#     nk_size allocated;
#     /* total amount of memory allocated */
#     nk_size needed;
#     /* totally consumed memory given that enough memory is present */
#     nk_size calls;
#     /* number of allocation calls */
#     nk_size size;
#     /* current size of the buffer */
# };
# void nk_buffer_init_default(struct nk_buffer*);
# void nk_buffer_init(struct nk_buffer*, const struct nk_allocator*, nk_size size);
# void nk_buffer_init_fixed(struct nk_buffer*, void *memory, nk_size size);
# void nk_buffer_info(struct nk_memory_status*, struct nk_buffer*);
# void nk_buffer_push(struct nk_buffer*, enum nk_buffer_allocation_type type, const void *memory, nk_size size, nk_size align);
# void nk_buffer_mark(struct nk_buffer*, enum nk_buffer_allocation_type type);
# void nk_buffer_reset(struct nk_buffer*, enum nk_buffer_allocation_type type);
# void nk_buffer_clear(struct nk_buffer*);
# void nk_buffer_free(struct nk_buffer*);
# void *nk_buffer_memory(struct nk_buffer*);
# const void *nk_buffer_memory_const(const struct nk_buffer*);
# nk_size nk_buffer_total(struct nk_buffer*);


# String
# struct nk_str {
#     struct nk_buffer buffer;
#     int len; /* in codepoints/runes/glyphs */
# };
# void nk_str_init_default(struct nk_str*);
# void nk_str_init(struct nk_str*, const struct nk_allocator*, nk_size size);
# void nk_str_init_fixed(struct nk_str*, void *memory, nk_size size);
# void nk_str_clear(struct nk_str*);
# void nk_str_free(struct nk_str*);
# int nk_str_append_text_char(struct nk_str*, const char*, int);
# int nk_str_append_str_char(struct nk_str*, const char*);
# int nk_str_append_text_utf8(struct nk_str*, const char*, int);
# int nk_str_append_str_utf8(struct nk_str*, const char*);
# int nk_str_append_text_runes(struct nk_str*, const nk_rune*, int);
# int nk_str_append_str_runes(struct nk_str*, const nk_rune*);
# int nk_str_insert_at_char(struct nk_str*, int pos, const char*, int);
# int nk_str_insert_at_rune(struct nk_str*, int pos, const char*, int);
# int nk_str_insert_text_char(struct nk_str*, int pos, const char*, int);
# int nk_str_insert_str_char(struct nk_str*, int pos, const char*);
# int nk_str_insert_text_utf8(struct nk_str*, int pos, const char*, int);
# int nk_str_insert_str_utf8(struct nk_str*, int pos, const char*);
# int nk_str_insert_text_runes(struct nk_str*, int pos, const nk_rune*, int);
# int nk_str_insert_str_runes(struct nk_str*, int pos, const nk_rune*);
# void nk_str_remove_chars(struct nk_str*, int len);
# void nk_str_remove_runes(struct nk_str *str, int len);
# void nk_str_delete_chars(struct nk_str*, int pos, int len);
# void nk_str_delete_runes(struct nk_str*, int pos, int len);
# char *nk_str_at_char(struct nk_str*, int pos);
# char *nk_str_at_rune(struct nk_str*, int pos, nk_rune *unicode, int *len);
# nk_rune nk_str_rune_at(const struct nk_str*, int pos);
# const char *nk_str_at_char_const(const struct nk_str*, int pos);
# const char *nk_str_at_const(const struct nk_str*, int pos, nk_rune *unicode, int *len);
# char *nk_str_get(struct nk_str*);
# const char *nk_str_get_const(const struct nk_str*);
# int nk_str_len(struct nk_str*);
# int nk_str_len_char(struct nk_str*);

# Text Editor

#ifndef NK_TEXTEDIT_UNDOSTATECOUNT
#define NK_TEXTEDIT_UNDOSTATECOUNT     99
#endif

#ifndef NK_TEXTEDIT_UNDOCHARCOUNT
#define NK_TEXTEDIT_UNDOCHARCOUNT      999
#endif

# struct nk_text_edit;
# struct nk_clipboard {
#     nk_handle userdata;
#     nk_plugin_paste paste;
#     nk_plugin_copy copy;
# };

# struct nk_text_undo_record {
#    int where;
#    short insert_length;
#    short delete_length;
#    short char_storage;
# };

# struct nk_text_undo_state {
#    struct nk_text_undo_record undo_rec[NK_TEXTEDIT_UNDOSTATECOUNT];
#    nk_rune undo_char[NK_TEXTEDIT_UNDOCHARCOUNT];
#    short undo_point;
#    short redo_point;
#    short undo_char_point;
#    short redo_char_point;
# };

TEXT_EDIT_SINGLE_LINE=0
TEXT_EDIT_MULTI_LINE=1

TEXT_EDIT_MODE_VIEW=0
TEXT_EDIT_MODE_INSERT=1
TEXT_EDIT_MODE_REPLACE=2

# struct nk_text_edit {
#     struct nk_clipboard clip;
#     struct nk_str string;
#     nk_plugin_filter filter;
#     struct nk_vec2 scrollbar;

#     int cursor;
#     int select_start;
#     int select_end;
#     unsigned char mode;
#     unsigned char cursor_at_end_of_line;
#     unsigned char initialized;
#     unsigned char has_preferred_x;
#     unsigned char single_line;
#     unsigned char active;
#     unsigned char padding1;
#     float preferred_x;
#     struct nk_text_undo_state undo;
# };

# int nk_filter_default(const struct nk_text_edit*, nk_rune unicode);
# int nk_filter_ascii(const struct nk_text_edit*, nk_rune unicode);
# int nk_filter_float(const struct nk_text_edit*, nk_rune unicode);
# int nk_filter_decimal(const struct nk_text_edit*, nk_rune unicode);
# int nk_filter_hex(const struct nk_text_edit*, nk_rune unicode);
# int nk_filter_oct(const struct nk_text_edit*, nk_rune unicode);
# int nk_filter_binary(const struct nk_text_edit*, nk_rune unicode);
# void nk_textedit_init_default(struct nk_text_edit*);
# void nk_textedit_init(struct nk_text_edit*, struct nk_allocator*, nk_size size);
# void nk_textedit_init_fixed(struct nk_text_edit*, void *memory, nk_size size);
# void nk_textedit_free(struct nk_text_edit*);
# void nk_textedit_text(struct nk_text_edit*, const char*, int total_len);
# void nk_textedit_delete(struct nk_text_edit*, int where, int len);
# void nk_textedit_delete_selection(struct nk_text_edit*);
# void nk_textedit_select_all(struct nk_text_edit*);
# int nk_textedit_cut(struct nk_text_edit*);
# int nk_textedit_paste(struct nk_text_edit*, char const*, int len);
# void nk_textedit_undo(struct nk_text_edit*);
# void nk_textedit_redo(struct nk_text_edit*);

# Drawing
COMMAND_NOP=0
COMMAND_SCISSOR=1
COMMAND_LINE=2
COMMAND_CURVE=3
COMMAND_RECT=4
COMMAND_RECT_FILLED=5
COMMAND_RECT_MULTI_COLOR=6
COMMAND_CIRCLE=7
COMMAND_CIRCLE_FILLED=8
COMMAND_ARC=9
COMMAND_ARC_FILLED=10
COMMAND_TRIANGLE=11
COMMAND_TRIANGLE_FILLED=12
COMMAND_POLYGON=13
COMMAND_POLYGON_FILLED=14
COMMAND_POLYLINE=15
COMMAND_TEXT=16
COMMAND_IMAGE=17
COMMAND_CUSTOM=18

# /* command base and header of every command inside the buffer */
# struct nk_command {
#     enum nk_command_type type;
#     nk_size next;
# #ifdef NK_INCLUDE_COMMAND_USERDATA
#     nk_handle userdata;
# #endif
# };

# struct nk_command_scissor {
#     struct nk_command header;
#     short x, y;
#     unsigned short w, h;
# };

# struct nk_command_line {
#     struct nk_command header;
#     unsigned short line_thickness;
#     struct nk_vec2i begin;
#     struct nk_vec2i end;
#     struct nk_color color;
# };

# struct nk_command_curve {
#     struct nk_command header;
#     unsigned short line_thickness;
#     struct nk_vec2i begin;
#     struct nk_vec2i end;
#     struct nk_vec2i ctrl[2];
#     struct nk_color color;
# };

# struct nk_command_rect {
#     struct nk_command header;
#     unsigned short rounding;
#     unsigned short line_thickness;
#     short x, y;
#     unsigned short w, h;
#     struct nk_color color;
# };

# struct nk_command_rect_filled {
#     struct nk_command header;
#     unsigned short rounding;
#     short x, y;
#     unsigned short w, h;
#     struct nk_color color;
# };

# struct nk_command_rect_multi_color {
#     struct nk_command header;
#     short x, y;
#     unsigned short w, h;
#     struct nk_color left;
#     struct nk_color top;
#     struct nk_color bottom;
#     struct nk_color right;
# };

# struct nk_command_triangle {
#     struct nk_command header;
#     unsigned short line_thickness;
#     struct nk_vec2i a;
#     struct nk_vec2i b;
#     struct nk_vec2i c;
#     struct nk_color color;
# };

# struct nk_command_triangle_filled {
#     struct nk_command header;
#     struct nk_vec2i a;
#     struct nk_vec2i b;
#     struct nk_vec2i c;
#     struct nk_color color;
# };

# struct nk_command_circle {
#     struct nk_command header;
#     short x, y;
#     unsigned short line_thickness;
#     unsigned short w, h;
#     struct nk_color color;
# };

# struct nk_command_circle_filled {
#     struct nk_command header;
#     short x, y;
#     unsigned short w, h;
#     struct nk_color color;
# };

# struct nk_command_arc {
#     struct nk_command header;
#     short cx, cy;
#     unsigned short r;
#     unsigned short line_thickness;
#     float a[2];
#     struct nk_color color;
# };

# struct nk_command_arc_filled {
#     struct nk_command header;
#     short cx, cy;
#     unsigned short r;
#     float a[2];
#     struct nk_color color;
# };

# struct nk_command_polygon {
#     struct nk_command header;
#     struct nk_color color;
#     unsigned short line_thickness;
#     unsigned short point_count;
#     struct nk_vec2i points[1];
# };

# struct nk_command_polygon_filled {
#     struct nk_command header;
#     struct nk_color color;
#     unsigned short point_count;
#     struct nk_vec2i points[1];
# };

# struct nk_command_polyline {
#     struct nk_command header;
#     struct nk_color color;
#     unsigned short line_thickness;
#     unsigned short point_count;
#     struct nk_vec2i points[1];
# };

# struct nk_command_image {
#     struct nk_command header;
#     short x, y;
#     unsigned short w, h;
#     struct nk_image img;
#     struct nk_color col;
# };

# typedef void (*nk_command_custom_callback)(void *canvas, short x,short y,
#     unsigned short w, unsigned short h, nk_handle callback_data);
# struct nk_command_custom {
#     struct nk_command header;
#     short x, y;
#     unsigned short w, h;
#     nk_handle callback_data;
#     nk_command_custom_callback callback;
# };

# struct nk_command_text {
#     struct nk_command header;
#     const struct nk_user_font *font;
#     struct nk_color background;
#     struct nk_color foreground;
#     short x, y;
#     unsigned short w, h;
#     float height;
#     int length;
#     char string[1];
# };

CLIPPING_OFF = 0
CLIPPING_ON = 1

# struct nk_command_buffer {
#     struct nk_buffer *base;
#     struct nk_rect clip;
#     int use_clipping;
#     nk_handle userdata;
#     nk_size begin, end, last;
# };


# void nk_stroke_line(struct nk_command_buffer *b, float x0, float y0, float x1, float y1, float line_thickness, struct nk_color);
# void nk_stroke_curve(struct nk_command_buffer*, float, float, float, float, float, float, float, float, float line_thickness, struct nk_color);
# void nk_stroke_rect(struct nk_command_buffer*, struct nk_rect, float rounding, float line_thickness, struct nk_color);
# void nk_stroke_circle(struct nk_command_buffer*, struct nk_rect, float line_thickness, struct nk_color);
# void nk_stroke_arc(struct nk_command_buffer*, float cx, float cy, float radius, float a_min, float a_max, float line_thickness, struct nk_color);
# void nk_stroke_triangle(struct nk_command_buffer*, float, float, float, float, float, float, float line_thichness, struct nk_color);
# void nk_stroke_polyline(struct nk_command_buffer*, float *points, int point_count, float line_thickness, struct nk_color col);
# void nk_stroke_polygon(struct nk_command_buffer*, float*, int point_count, float line_thickness, struct nk_color);
# void nk_fill_rect(struct nk_command_buffer*, struct nk_rect, float rounding, struct nk_color);
# void nk_fill_rect_multi_color(struct nk_command_buffer*, struct nk_rect, struct nk_color left, struct nk_color top, struct nk_color right, struct nk_color bottom);
# void nk_fill_circle(struct nk_command_buffer*, struct nk_rect, struct nk_color);
# void nk_fill_arc(struct nk_command_buffer*, float cx, float cy, float radius, float a_min, float a_max, struct nk_color);
# void nk_fill_triangle(struct nk_command_buffer*, float x0, float y0, float x1, float y1, float x2, float y2, struct nk_color);
# void nk_fill_polygon(struct nk_command_buffer*, float*, int point_count, struct nk_color);
# void nk_draw_image(struct nk_command_buffer*, struct nk_rect, const struct nk_image*, struct nk_color);
# void nk_draw_text(struct nk_command_buffer*, struct nk_rect, const char *text, int len, const struct nk_user_font*, struct nk_color, struct nk_color);
# void nk_push_scissor(struct nk_command_buffer*, struct nk_rect);
# void nk_push_custom(struct nk_command_buffer*, struct nk_rect, nk_command_custom_callback, nk_handle usr);


# Input
# struct nk_mouse_button {
#     int down;
#     unsigned int clicked;
#     struct nk_vec2 clicked_pos;
# };
# struct nk_mouse {
#     struct nk_mouse_button buttons[NK_BUTTON_MAX];
#     struct nk_vec2 pos;
#     struct nk_vec2 prev;
#     struct nk_vec2 delta;
#     struct nk_vec2 scroll_delta;
#     unsigned char grab;
#     unsigned char grabbed;
#     unsigned char ungrab;
# };

# struct nk_key {
#     int down;
#     unsigned int clicked;
# };
# struct nk_keyboard {
#     struct nk_key keys[NK_KEY_MAX];
#     char text[NK_INPUT_MAX];
#     int text_len;
# };

# struct nk_input {
#     struct nk_keyboard keyboard;
#     struct nk_mouse mouse;
# };
# int nk_input_has_mouse_click(const struct nk_input*, enum nk_buttons);
# int nk_input_has_mouse_click_in_rect(const struct nk_input*, enum nk_buttons, struct nk_rect);
# int nk_input_has_mouse_click_down_in_rect(const struct nk_input*, enum nk_buttons, struct nk_rect, int down);
# int nk_input_is_mouse_click_in_rect(const struct nk_input*, enum nk_buttons, struct nk_rect);
# int nk_input_is_mouse_click_down_in_rect(const struct nk_input *i, enum nk_buttons id, struct nk_rect b, int down);
# int nk_input_any_mouse_click_in_rect(const struct nk_input*, struct nk_rect);
# int nk_input_is_mouse_prev_hovering_rect(const struct nk_input*, struct nk_rect);
# int nk_input_is_mouse_hovering_rect(const struct nk_input*, struct nk_rect);
# int nk_input_mouse_clicked(const struct nk_input*, enum nk_buttons, struct nk_rect);
# int nk_input_is_mouse_down(const struct nk_input*, enum nk_buttons);
# int nk_input_is_mouse_pressed(const struct nk_input*, enum nk_buttons);
# int nk_input_is_mouse_released(const struct nk_input*, enum nk_buttons);
# int nk_input_is_key_pressed(const struct nk_input*, enum nk_keys);
# int nk_input_is_key_released(const struct nk_input*, enum nk_keys);
# int nk_input_is_key_down(const struct nk_input*, enum nk_keys);


# Draw List

# typedef nk_ushort nk_draw_index;
STROKE_OPEN=0
STROKE_CLOSED=1


VERTEX_POSITION=0
VERTEX_COLOR=1
VERTEX_TEXCOORD=2
VERTEX_ATTRIBUTE_COUNT=3


# enum nk_draw_vertex_layout_format {
#     NK_FORMAT_SCHAR,
#     NK_FORMAT_SSHORT,
#     NK_FORMAT_SINT,
#     NK_FORMAT_UCHAR,
#     NK_FORMAT_USHORT,
#     NK_FORMAT_UINT,
#     NK_FORMAT_FLOAT,
#     NK_FORMAT_DOUBLE,

# NK_FORMAT_COLOR_BEGIN,
#     NK_FORMAT_R8G8B8 = NK_FORMAT_COLOR_BEGIN,
#     NK_FORMAT_R16G15B16,
#     NK_FORMAT_R32G32B32,

#     NK_FORMAT_R8G8B8A8,
#     NK_FORMAT_B8G8R8A8,
#     NK_FORMAT_R16G15B16A16,
#     NK_FORMAT_R32G32B32A32,
#     NK_FORMAT_R32G32B32A32_FLOAT,
#     NK_FORMAT_R32G32B32A32_DOUBLE,

#     NK_FORMAT_RGB32,
#     NK_FORMAT_RGBA32,
# NK_FORMAT_COLOR_END = NK_FORMAT_RGBA32,
#     NK_FORMAT_COUNT
# };

# #define NK_VERTEX_LAYOUT_END NK_VERTEX_ATTRIBUTE_COUNT,NK_FORMAT_COUNT,0
# struct nk_draw_vertex_layout_element {
#     enum nk_draw_vertex_layout_attribute attribute;
#     enum nk_draw_vertex_layout_format format;
#     nk_size offset;
# };

# struct nk_draw_command {
#     unsigned int elem_count;
#     /* number of elements in the current draw batch */
#     struct nk_rect clip_rect;
#     /* current screen clipping rectangle */
#     nk_handle texture;
#     /* current texture to set */
# #ifdef NK_INCLUDE_COMMAND_USERDATA
#     nk_handle userdata;
# #endif
# };

# struct nk_draw_list {
#     struct nk_rect clip_rect;
#     struct nk_vec2 circle_vtx[12];
#     struct nk_convert_config config;

#     struct nk_buffer *buffer;
#     struct nk_buffer *vertices;
#     struct nk_buffer *elements;

#     unsigned int element_count;
#     unsigned int vertex_count;
#     unsigned int cmd_count;
#     nk_size cmd_offset;

#     unsigned int path_count;
#     unsigned int path_offset;

#     enum nk_anti_aliasing line_AA;
#     enum nk_anti_aliasing shape_AA;

# #ifdef NK_INCLUDE_COMMAND_USERDATA
#     nk_handle userdata;
# #endif
# };

# void nk_draw_list_init(struct nk_draw_list*);
# void nk_draw_list_setup(struct nk_draw_list*, const struct nk_convert_config*, struct nk_buffer *cmds, struct nk_buffer *vertices, struct nk_buffer *elements, enum nk_anti_aliasing line_aa,enum nk_anti_aliasing shape_aa);
# void nk_draw_list_clear(struct nk_draw_list*);
# const struct nk_draw_command* nk__draw_list_begin(const struct nk_draw_list*, const struct nk_buffer*);
# const struct nk_draw_command* nk__draw_list_next(const struct nk_draw_command*, const struct nk_buffer*, const struct nk_draw_list*);
# const struct nk_draw_command* nk__draw_list_end(const struct nk_draw_list*, const struct nk_buffer*);
# void nk_draw_list_clear(struct nk_draw_list *list);
# void nk_draw_list_path_clear(struct nk_draw_list*);
# void nk_draw_list_path_line_to(struct nk_draw_list*, struct nk_vec2 pos);
# void nk_draw_list_path_arc_to_fast(struct nk_draw_list*, struct nk_vec2 center, float radius, int a_min, int a_max);
# void nk_draw_list_path_arc_to(struct nk_draw_list*, struct nk_vec2 center, float radius, float a_min, float a_max, unsigned int segments);
# void nk_draw_list_path_rect_to(struct nk_draw_list*, struct nk_vec2 a, struct nk_vec2 b, float rounding);
# void nk_draw_list_path_curve_to(struct nk_draw_list*, struct nk_vec2 p2, struct nk_vec2 p3, struct nk_vec2 p4, unsigned int num_segments);
# void nk_draw_list_path_fill(struct nk_draw_list*, struct nk_color);
# void nk_draw_list_path_stroke(struct nk_draw_list*, struct nk_color, enum nk_draw_list_stroke closed, float thickness);
# void nk_draw_list_stroke_line(struct nk_draw_list*, struct nk_vec2 a, struct nk_vec2 b, struct nk_color, float thickness);
# void nk_draw_list_stroke_rect(struct nk_draw_list*, struct nk_rect rect, struct nk_color, float rounding, float thickness);
# void nk_draw_list_stroke_triangle(struct nk_draw_list*, struct nk_vec2 a, struct nk_vec2 b, struct nk_vec2 c, struct nk_color, float thickness);
# void nk_draw_list_stroke_circle(struct nk_draw_list*, struct nk_vec2 center, float radius, struct nk_color, unsigned int segs, float thickness);
# void nk_draw_list_stroke_curve(struct nk_draw_list*, struct nk_vec2 p0, struct nk_vec2 cp0, struct nk_vec2 cp1, struct nk_vec2 p1, struct nk_color, unsigned int segments, float thickness);
# void nk_draw_list_stroke_poly_line(struct nk_draw_list*, const struct nk_vec2 *pnts, const unsigned int cnt, struct nk_color, enum nk_draw_list_stroke, float thickness, enum nk_anti_aliasing);
# void nk_draw_list_fill_rect(struct nk_draw_list*, struct nk_rect rect, struct nk_color, float rounding);
# void nk_draw_list_fill_rect_multi_color(struct nk_draw_list*, struct nk_rect rect, struct nk_color left, struct nk_color top, struct nk_color right, struct nk_color bottom);
# void nk_draw_list_fill_triangle(struct nk_draw_list*, struct nk_vec2 a, struct nk_vec2 b, struct nk_vec2 c, struct nk_color);
# void nk_draw_list_fill_circle(struct nk_draw_list*, struct nk_vec2 center, float radius, struct nk_color col, unsigned int segs);
# void nk_draw_list_fill_poly_convex(struct nk_draw_list*, const struct nk_vec2 *points, const unsigned int count, struct nk_color, enum nk_anti_aliasing);
# void nk_draw_list_add_image(struct nk_draw_list*, struct nk_image texture, struct nk_rect rect, struct nk_color);
# void nk_draw_list_add_text(struct nk_draw_list*, const struct nk_user_font*, struct nk_rect, const char *text, int len, float font_height, struct nk_color);
# void nk_draw_list_push_userdata(struct nk_draw_list*, nk_handle userdata);


# GUI

STYLE_ITEM_COLOR=0
STYLE_ITEM_IMAGE=1

# union nk_style_item_data {
#     struct nk_image image;
#     struct nk_color color;
# };

# struct nk_style_item {
#     enum nk_style_item_type type;
#     union nk_style_item_data data;
# };

# struct nk_style_text {
#     struct nk_color color;
#     struct nk_vec2 padding;
# };

# struct nk_style_button {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* text */
#     struct nk_color text_background;
#     struct nk_color text_normal;
#     struct nk_color text_hover;
#     struct nk_color text_active;
#     nk_flags text_alignment;

#     /* properties */
#     float border;
#     float rounding;
#     struct nk_vec2 padding;
#     struct nk_vec2 image_padding;
#     struct nk_vec2 touch_padding;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle userdata);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle userdata);
# };

# struct nk_style_toggle {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* cursor */
#     struct nk_style_item cursor_normal;
#     struct nk_style_item cursor_hover;

#     /* text */
#     struct nk_color text_normal;
#     struct nk_color text_hover;
#     struct nk_color text_active;
#     struct nk_color text_background;
#     nk_flags text_alignment;

#     /* properties */
#     struct nk_vec2 padding;
#     struct nk_vec2 touch_padding;
#     float spacing;
#     float border;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle);
# };

# struct nk_style_selectable {
#     /* background (inactive) */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item pressed;

#     /* background (active) */
#     struct nk_style_item normal_active;
#     struct nk_style_item hover_active;
#     struct nk_style_item pressed_active;

#     /* text color (inactive) */
#     struct nk_color text_normal;
#     struct nk_color text_hover;
#     struct nk_color text_pressed;

#     /* text color (active) */
#     struct nk_color text_normal_active;
#     struct nk_color text_hover_active;
#     struct nk_color text_pressed_active;
#     struct nk_color text_background;
#     nk_flags text_alignment;

#     /* properties */
#     float rounding;
#     struct nk_vec2 padding;
#     struct nk_vec2 touch_padding;
#     struct nk_vec2 image_padding;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle);
# };

# struct nk_style_slider {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* background bar */
#     struct nk_color bar_normal;
#     struct nk_color bar_hover;
#     struct nk_color bar_active;
#     struct nk_color bar_filled;

#     /* cursor */
#     struct nk_style_item cursor_normal;
#     struct nk_style_item cursor_hover;
#     struct nk_style_item cursor_active;

#     /* properties */
#     float border;
#     float rounding;
#     float bar_height;
#     struct nk_vec2 padding;
#     struct nk_vec2 spacing;
#     struct nk_vec2 cursor_size;

#     /* optional buttons */
#     int show_buttons;
#     struct nk_style_button inc_button;
#     struct nk_style_button dec_button;
#     enum nk_symbol_type inc_symbol;
#     enum nk_symbol_type dec_symbol;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle);
# };

# struct nk_style_progress {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* cursor */
#     struct nk_style_item cursor_normal;
#     struct nk_style_item cursor_hover;
#     struct nk_style_item cursor_active;
#     struct nk_color cursor_border_color;

#     /* properties */
#     float rounding;
#     float border;
#     float cursor_border;
#     float cursor_rounding;
#     struct nk_vec2 padding;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle);
# };

# struct nk_style_scrollbar {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* cursor */
#     struct nk_style_item cursor_normal;
#     struct nk_style_item cursor_hover;
#     struct nk_style_item cursor_active;
#     struct nk_color cursor_border_color;

#     /* properties */
#     float border;
#     float rounding;
#     float border_cursor;
#     float rounding_cursor;
#     struct nk_vec2 padding;

#     /* optional buttons */
#     int show_buttons;
#     struct nk_style_button inc_button;
#     struct nk_style_button dec_button;
#     enum nk_symbol_type inc_symbol;
#     enum nk_symbol_type dec_symbol;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle);
# };

# struct nk_style_edit {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;
#     struct nk_style_scrollbar scrollbar;

#     /* cursor  */
#     struct nk_color cursor_normal;
#     struct nk_color cursor_hover;
#     struct nk_color cursor_text_normal;
#     struct nk_color cursor_text_hover;

#     /* text (unselected) */
#     struct nk_color text_normal;
#     struct nk_color text_hover;
#     struct nk_color text_active;

#     /* text (selected) */
#     struct nk_color selected_normal;
#     struct nk_color selected_hover;
#     struct nk_color selected_text_normal;
#     struct nk_color selected_text_hover;

#     /* properties */
#     float border;
#     float rounding;
#     float cursor_size;
#     struct nk_vec2 scrollbar_size;
#     struct nk_vec2 padding;
#     float row_padding;
# };

# struct nk_style_property {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* text */
#     struct nk_color label_normal;
#     struct nk_color label_hover;
#     struct nk_color label_active;

#     /* symbols */
#     enum nk_symbol_type sym_left;
#     enum nk_symbol_type sym_right;

#     /* properties */
#     float border;
#     float rounding;
#     struct nk_vec2 padding;

#     struct nk_style_edit edit;
#     struct nk_style_button inc_button;
#     struct nk_style_button dec_button;

#     /* optional user callbacks */
#     nk_handle userdata;
#     void(*draw_begin)(struct nk_command_buffer*, nk_handle);
#     void(*draw_end)(struct nk_command_buffer*, nk_handle);
# };

# struct nk_style_chart {
#     /* colors */
#     struct nk_style_item background;
#     struct nk_color border_color;
#     struct nk_color selected_color;
#     struct nk_color color;

#     /* properties */
#     float border;
#     float rounding;
#     struct nk_vec2 padding;
# };

# struct nk_style_combo {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;
#     struct nk_color border_color;

#     /* label */
#     struct nk_color label_normal;
#     struct nk_color label_hover;
#     struct nk_color label_active;

#     /* symbol */
#     struct nk_color symbol_normal;
#     struct nk_color symbol_hover;
#     struct nk_color symbol_active;

#     /* button */
#     struct nk_style_button button;
#     enum nk_symbol_type sym_normal;
#     enum nk_symbol_type sym_hover;
#     enum nk_symbol_type sym_active;

#     /* properties */
#     float border;
#     float rounding;
#     struct nk_vec2 content_padding;
#     struct nk_vec2 button_padding;
#     struct nk_vec2 spacing;
# };

# struct nk_style_tab {
#     /* background */
#     struct nk_style_item background;
#     struct nk_color border_color;
#     struct nk_color text;

#     /* button */
#     struct nk_style_button tab_maximize_button;
#     struct nk_style_button tab_minimize_button;
#     struct nk_style_button node_maximize_button;
#     struct nk_style_button node_minimize_button;
#     enum nk_symbol_type sym_minimize;
#     enum nk_symbol_type sym_maximize;

#     /* properties */
#     float border;
#     float rounding;
#     float indent;
#     struct nk_vec2 padding;
#     struct nk_vec2 spacing;
# };

HEADER_LEFT=0
HEADER_RIGHT=1

# struct nk_style_window_header {
#     /* background */
#     struct nk_style_item normal;
#     struct nk_style_item hover;
#     struct nk_style_item active;

#     /* button */
#     struct nk_style_button close_button;
#     struct nk_style_button minimize_button;
#     enum nk_symbol_type close_symbol;
#     enum nk_symbol_type minimize_symbol;
#     enum nk_symbol_type maximize_symbol;

#     /* title */
#     struct nk_color label_normal;
#     struct nk_color label_hover;
#     struct nk_color label_active;

#     /* properties */
#     enum nk_style_header_align align;
#     struct nk_vec2 padding;
#     struct nk_vec2 label_padding;
#     struct nk_vec2 spacing;
# };

# struct nk_style_window {
#     struct nk_style_window_header header;
#     struct nk_style_item fixed_background;
#     struct nk_color background;

#     struct nk_color border_color;
#     struct nk_color popup_border_color;
#     struct nk_color combo_border_color;
#     struct nk_color contextual_border_color;
#     struct nk_color menu_border_color;
#     struct nk_color group_border_color;
#     struct nk_color tooltip_border_color;
#     struct nk_style_item scaler;

#     float border;
#     float combo_border;
#     float contextual_border;
#     float menu_border;
#     float group_border;
#     float tooltip_border;
#     float popup_border;
#     float min_row_height_padding;

#     float rounding;
#     struct nk_vec2 spacing;
#     struct nk_vec2 scrollbar_size;
#     struct nk_vec2 min_size;

#     struct nk_vec2 padding;
#     struct nk_vec2 group_padding;
#     struct nk_vec2 popup_padding;
#     struct nk_vec2 combo_padding;
#     struct nk_vec2 contextual_padding;
#     struct nk_vec2 menu_padding;
#     struct nk_vec2 tooltip_padding;
# };

# struct nk_style {
#     const struct nk_user_font *font;
#     const struct nk_cursor *cursors[NK_CURSOR_COUNT];
#     const struct nk_cursor *cursor_active;
#     struct nk_cursor *cursor_last;
#     int cursor_visible;

#     struct nk_style_text text;
#     struct nk_style_button button;
#     struct nk_style_button contextual_button;
#     struct nk_style_button menu_button;
#     struct nk_style_toggle option;
#     struct nk_style_toggle checkbox;
#     struct nk_style_selectable selectable;
#     struct nk_style_slider slider;
#     struct nk_style_progress progress;
#     struct nk_style_property property;
#     struct nk_style_edit edit;
#     struct nk_style_chart chart;
#     struct nk_style_scrollbar scrollh;
#     struct nk_style_scrollbar scrollv;
#     struct nk_style_tab tab;
#     struct nk_style_combo combo;
#     struct nk_style_window window;
# };

# struct nk_style_item nk_style_item_image(struct nk_image img);
# struct nk_style_item nk_style_item_color(struct nk_color);
# struct nk_style_item nk_style_item_hide(void);


# Panel
#ifndef NK_MAX_LAYOUT_ROW_TEMPLATE_COLUMNS
#define NK_MAX_LAYOUT_ROW_TEMPLATE_COLUMNS 16
#endif
#ifndef NK_CHART_MAX_SLOT
#define NK_CHART_MAX_SLOT 4
#endif

PANEL_WINDOW     = 1 << 0
PANEL_GROUP      = 1 << 1
PANEL_POPUP      = 1 << 2
PANEL_CONTEXTUAL = 1 << 4
PANEL_COMBO      = 1 << 5
PANEL_MENU       = 1 << 6
PANEL_TOOLTIP    = 1 << 7

PANEL_SET_NONBLOCK = PANEL_CONTEXTUAL|PANEL_COMBO|PANEL_MENU|PANEL_TOOLTIP
PANEL_SET_POPUP = PANEL_SET_NONBLOCK|PANEL_POPUP
PANEL_SET_SUB = PANEL_SET_POPUP|PANEL_GROUP

# struct nk_chart_slot {
#     enum nk_chart_type type;
#     struct nk_color color;
#     struct nk_color highlight;
#     float min, max, range;
#     int count;
#     struct nk_vec2 last;
#     int index;
# };

# struct nk_chart {
#     int slot;
#     float x, y, w, h;
#     struct nk_chart_slot slots[NK_CHART_MAX_SLOT];
# };

NK_LAYOUT_DYNAMIC_FIXED = 0
NK_LAYOUT_DYNAMIC_ROW=1
NK_LAYOUT_DYNAMIC_FREE=2
NK_LAYOUT_DYNAMIC=3
NK_LAYOUT_STATIC_FIXED=4
NK_LAYOUT_STATIC_ROW=5
NK_LAYOUT_STATIC_FREE=6
NK_LAYOUT_STATIC=7
NK_LAYOUT_TEMPLATE=8
NK_LAYOUT_COUNT=9

# struct nk_row_layout {
#     enum nk_panel_row_layout_type type;
#     int index;
#     float height;
#     float min_height;
#     int columns;
#     const float *ratio;
#     float item_width;
#     float item_height;
#     float item_offset;
#     float filled;
#     struct nk_rect item;
#     int tree_depth;
#     float templates[NK_MAX_LAYOUT_ROW_TEMPLATE_COLUMNS];
# };

# struct nk_popup_buffer {
#     nk_size begin;
#     nk_size parent;
#     nk_size last;
#     nk_size end;
#     int active;
# };

# struct nk_menu_state {
#     float x, y, w, h;
#     struct nk_scroll offset;
# };

# struct nk_panel {
#     enum nk_panel_type type;
#     nk_flags flags;
#     struct nk_rect bounds;
#     nk_uint *offset_x;
#     nk_uint *offset_y;
#     float at_x, at_y, max_x;
#     float footer_height;
#     float header_height;
#     float border;
#     unsigned int has_scrolling;
#     struct nk_rect clip;
#     struct nk_menu_state menu;
#     struct nk_row_layout row;
#     struct nk_chart chart;
#     struct nk_command_buffer *buffer;
#     struct nk_panel *parent;
# };


#==============================================================
#                          WINDOW
# =============================================================
#ifndef NK_WINDOW_MAX_NAME
#define NK_WINDOW_MAX_NAME 64
#endif

# struct nk_table;

WINDOW_PRIVATE       = 1 << 11
WINDOW_DYNAMIC       = WINDOW_PRIVATE
WINDOW_ROM           = 1 << 12
WINDOW_NOT_INTERACTIVE = WINDOW_ROM|WINDOW_NO_INPUT
WINDOW_HIDDEN        = 1 << 13
WINDOW_CLOSED        = 1 << 14
WINDOW_MINIMIZED     = 1 << 15
WINDOW_REMOVE_ROM    = 1 << 16

# struct nk_popup_state {
#     struct nk_window *win;
#     enum nk_panel_type type;
#     struct nk_popup_buffer buf;
#     nk_hash name;
#     int active;
#     unsigned combo_count;
#     unsigned con_count, con_old;
#     unsigned active_con;
#     struct nk_rect header;
# };

# struct nk_edit_state {
#     nk_hash name;
#     unsigned int seq;
#     unsigned int old;
#     int active, prev;
#     int cursor;
#     int sel_start;
#     int sel_end;
#     struct nk_scroll scrollbar;
#     unsigned char mode;
#     unsigned char single_line;
# };

# struct nk_property_state {
#     int active, prev;
#     char buffer[NK_MAX_NUMBER_BUFFER];
#     int length;
#     int cursor;
#     int select_start;
#     int select_end;
#     nk_hash name;
#     unsigned int seq;
#     unsigned int old;
#     int state;
# };

# struct nk_window {
#     unsigned int seq;
#     nk_hash name;
#     char name_string[NK_WINDOW_MAX_NAME];
#     nk_flags flags;

#     struct nk_rect bounds;
#     struct nk_scroll scrollbar;
#     struct nk_command_buffer buffer;
#     struct nk_panel *layout;
#     float scrollbar_hiding_timer;

#     /* persistent widget state */
#     struct nk_property_state property;
#     struct nk_popup_state popup;
#     struct nk_edit_state edit;
#     unsigned int scrolled;

#     struct nk_table *tables;
#     unsigned int table_count;

#     /* window list hooks */
#     struct nk_window *next;
#     struct nk_window *prev;
#     struct nk_window *parent;
# };


# /*==============================================================
#  *                          STACK
#  * =============================================================*/
# /* The style modifier stack can be used to temporarily change a
#  * property inside `nk_style`. For example if you want a special
#  * red button you can temporarily push the old button color onto a stack
#  * draw the button with a red color and then you just pop the old color
#  * back from the stack:
#  *
#  *      nk_style_push_style_item(ctx, &ctx->style.button.normal, nk_style_item_color(nk_rgb(255,0,0)));
#  *      nk_style_push_style_item(ctx, &ctx->style.button.hover, nk_style_item_color(nk_rgb(255,0,0)));
#  *      nk_style_push_style_item(ctx, &ctx->style.button.active, nk_style_item_color(nk_rgb(255,0,0)));
#  *      nk_style_push_vec2(ctx, &cx->style.button.padding, nk_vec2(2,2));
#  *
#  *      nk_button(...);
#  *
#  *      nk_style_pop_style_item(ctx);
#  *      nk_style_pop_style_item(ctx);
#  *      nk_style_pop_style_item(ctx);
#  *      nk_style_pop_vec2(ctx);
#  *
#  * Nuklear has a stack for style_items, float properties, vector properties,
#  * flags, colors, fonts and for button_behavior. Each has it's own fixed size stack
#  * which can be changed at compile time.
#  */
# #ifndef NK_BUTTON_BEHAVIOR_STACK_SIZE
# #define NK_BUTTON_BEHAVIOR_STACK_SIZE 8
# #endif

# #ifndef NK_FONT_STACK_SIZE
# #define NK_FONT_STACK_SIZE 8
# #endif

# #ifndef NK_STYLE_ITEM_STACK_SIZE
# #define NK_STYLE_ITEM_STACK_SIZE 16
# #endif

# #ifndef NK_FLOAT_STACK_SIZE
# #define NK_FLOAT_STACK_SIZE 32
# #endif

# #ifndef NK_VECTOR_STACK_SIZE
# #define NK_VECTOR_STACK_SIZE 16
# #endif

# #ifndef NK_FLAGS_STACK_SIZE
# #define NK_FLAGS_STACK_SIZE 32
# #endif

# #ifndef NK_COLOR_STACK_SIZE
# #define NK_COLOR_STACK_SIZE 32
# #endif

# #define NK_CONFIGURATION_STACK_TYPE(prefix, name, type)\
#     struct nk_config_stack_##name##_element {\
#         prefix##_##type *address;\
#         prefix##_##type old_value;\
#     }
# #define NK_CONFIG_STACK(type,size)\
#     struct nk_config_stack_##type {\
#         int head;\
#         struct nk_config_stack_##type##_element elements[size];\
#     }

# #define nk_float float
# NK_CONFIGURATION_STACK_TYPE(struct nk, style_item, style_item);
# NK_CONFIGURATION_STACK_TYPE(nk ,float, float);
# NK_CONFIGURATION_STACK_TYPE(struct nk, vec2, vec2);
# NK_CONFIGURATION_STACK_TYPE(nk ,flags, flags);
# NK_CONFIGURATION_STACK_TYPE(struct nk, color, color);
# NK_CONFIGURATION_STACK_TYPE(const struct nk, user_font, user_font*);
# NK_CONFIGURATION_STACK_TYPE(enum nk, button_behavior, button_behavior);

# NK_CONFIG_STACK(style_item, NK_STYLE_ITEM_STACK_SIZE);
# NK_CONFIG_STACK(float, NK_FLOAT_STACK_SIZE);
# NK_CONFIG_STACK(vec2, NK_VECTOR_STACK_SIZE);
# NK_CONFIG_STACK(flags, NK_FLAGS_STACK_SIZE);
# NK_CONFIG_STACK(color, NK_COLOR_STACK_SIZE);
# NK_CONFIG_STACK(user_font, NK_FONT_STACK_SIZE);
# NK_CONFIG_STACK(button_behavior, NK_BUTTON_BEHAVIOR_STACK_SIZE);

# struct nk_configuration_stacks {
#     struct nk_config_stack_style_item style_items;
#     struct nk_config_stack_float floats;
#     struct nk_config_stack_vec2 vectors;
#     struct nk_config_stack_flags flags;
#     struct nk_config_stack_color colors;
#     struct nk_config_stack_user_font fonts;
#     struct nk_config_stack_button_behavior button_behaviors;
# };

# /*==============================================================
#  *                          CONTEXT
#  * =============================================================*/
# #define NK_VALUE_PAGE_CAPACITY \
#     (((NK_MAX(sizeof(struct nk_window),sizeof(struct nk_panel)) / sizeof(nk_uint))) / 2)

# struct nk_table {
#     unsigned int seq;
#     unsigned int size;
#     nk_hash keys[NK_VALUE_PAGE_CAPACITY];
#     nk_uint values[NK_VALUE_PAGE_CAPACITY];
#     struct nk_table *next, *prev;
# };

# union nk_page_data {
#     struct nk_table tbl;
#     struct nk_panel pan;
#     struct nk_window win;
# };

# struct nk_page_element {
#     union nk_page_data data;
#     struct nk_page_element *next;
#     struct nk_page_element *prev;
# };

# struct nk_page {
#     unsigned int size;
#     struct nk_page *next;
#     struct nk_page_element win[1];
# };

# struct nk_pool {
#     struct nk_allocator alloc;
#     enum nk_allocation_type type;
#     unsigned int page_count;
#     struct nk_page *pages;
#     struct nk_page_element *freelist;
#     unsigned capacity;
#     nk_size size;
#     nk_size cap;
# };

# struct nk_context {
# /* public: can be accessed freely */
#     struct nk_input input;
#     struct nk_style style;
#     struct nk_buffer memory;
#     struct nk_clipboard clip;
#     nk_flags last_widget_state;
#     enum nk_button_behavior button_behavior;
#     struct nk_configuration_stacks stacks;
#     float delta_time_seconds;

# /* private:
#     should only be accessed if you
#     know what you are doing */
# #ifdef NK_INCLUDE_VERTEX_BUFFER_OUTPUT
#     struct nk_draw_list draw_list;
# #endif
# #ifdef NK_INCLUDE_COMMAND_USERDATA
#     nk_handle userdata;
# #endif
#     /* text editor objects are quite big because of an internal
#      * undo/redo stack. Therefore it does not make sense to have one for
#      * each window for temporary use cases, so I only provide *one* instance
#      * for all windows. This works because the content is cleared anyway */
#     struct nk_text_edit text_edit;
#     /* draw buffer used for overlay drawing operation like cursor */
#     struct nk_command_buffer overlay;

#     /* windows */
#     int build;
#     int use_pool;
#     struct nk_pool pool;
#     struct nk_window *begin;
#     struct nk_window *end;
#     struct nk_window *active;
#     struct nk_window *current;
#     struct nk_page_element *freelist;
#     unsigned int count;
#     unsigned int seq;
# };



GLFW3_DEFAULT=0
GLFW3_INSTALL_CALLBACKS=1


glfw3_init             = _nuklear.nk_glfw3_init
glfw3_init.restype     = POINTER(Context)
glfw3_init.arglist     = [POINTER(glfw.GLFWwindow), c_int]

class FontAtlas(Structure): pass

glfw3_font_stash_begin = _nuklear.nk_glfw3_font_stash_begin
glfw3_font_stash_begin.arglist = [POINTER(POINTER(FontAtlas))]

glfw3_font_stash_end = _nuklear.nk_glfw3_font_stash_end

glfw3_new_frame = _nuklear.nk_glfw3_new_frame



glfw3_render = _nuklear.nk_glfw3_render
glfw3_render.arglist = [c_int, c_int, c_int]