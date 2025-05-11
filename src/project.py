from PIL import Image, ImageDraw
##first features
def create_canvas(width,height):
    return Image.new("RGBA", (width, height), (0, 0, 0, 0))

def draw_rule_of_thirds(draw, width, height, line_color=(255, 255, 255, 128)):
    #Vertical lines
    draw.line([(width / 3, 0), (width / 3, height)], fill=line_color, width=2)
    draw.line([(2 * width / 3, 0), ( 2 * width / 3 height)], fill=line_color, width=2)

#rule of Thirds
#center grids

##parameters
#Image Modes
#Canvas Size
#line options