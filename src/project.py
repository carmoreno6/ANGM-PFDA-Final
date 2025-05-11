from PIL import Image, ImageDraw
import os

##first features
def create_canvas(width,height):
    return Image.new("RGBA", (width, height), (0, 0, 0, 0))

def draw_rule_of_thirds(draw, width, height, line_color=(255, 255, 255, 128)):
    #Vertical lines L-R
    draw.line([(width / 3, 0), (width / 3, height)], fill=line_color, width=2)
    draw.line([(2 * width / 3, 0), (2 * width / 3, height)], fill=line_color, width=2)
    #Horizontal line L-R
    draw.line([(0, height / 3), (width, height /3)], fill=line_color, width=2)
    draw.line([(0, 2 * width / 3), (width, 2 * height / 3)], fill=line_color, width=2)
    
def draw_center_grid(draw, width, height, line_color=(255, 255, 255, 128)):
    #Center Cross
    draw.line([(width /2, 0), (width / 2, height)], fill=line_color, width=2)
    draw.line([(0, height / 2), (width, height /2)], fill=line_color, width=2)
    
def save_overlay(image, filename):
    #makes sure save occurs without issue
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename,"PNG")
    
def save_overlay(image, filename):
    image.save(filename, "PNG")
    
def main():
    width, height = 1920, 1080
    overlay = create_canvas(width, height)
    draw = ImageDraw.Draw(overlay)

    #draw guides
    draw_rule_of_thirds(draw, width, height)
    draw_center_grid(draw, width, height)
    
    #save
    save_overlay(overlay, "overlays/overlay_rule_of_thirds_and_center.png")
    
if __name__ == "__main__":
    main()