import os
import pygame
import tkinter as tk
from tkinter import filedialog

pygame.init()

# Config
WIDTH, HEIGHT = 1920, 1080
BUTTON_HEIGHT = 50
BG_COLOR = (30, 30, 30)
BUTTON_COLOR = (60, 60, 60)
BUTTON_HIGHLIGHT = (90, 90, 90)
TEXT_COLOR = (255, 255, 255)
LINE_COLOR = (255, 255, 255)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT + BUTTON_HEIGHT))
pygame.display.set_caption("Grid IT UI")
font = pygame.font.SysFont(None, 36)

# Flags
show_rule_of_thirds = True
show_center_grid = True

# Classes
class Button:
    def __init__(self, rect, text, callback):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        
    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
                color = BUTTON_HIGHLIGHT
        else:
            color = BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect)
        text_surf = font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()
            
# drawing function
def draw_rule_of_thirds(surface):
    third_x = WIDTH // 3
    two_third_x = 2 * WIDTH // 3
    third_y = HEIGHT // 3
    two_third_y = 2 * HEIGHT // 3
    pygame.draw.line(surface, LINE_COLOR, (third_x, 0), (third_x, HEIGHT), 2)
    pygame.draw.line(surface, LINE_COLOR, (two_third_x, 0), (two_third_x, HEIGHT), 2)
    pygame.draw.line(surface, LINE_COLOR, (0, third_y), (WIDTH, third_y), 2)
    pygame.draw.line(surface, LINE_COLOR, (0, two_third_y), (WIDTH, two_third_y), 2)
    
def draw_center_grid(surface):
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    pygame.draw.line(surface, LINE_COLOR, (center_x, 0), (center_x, HEIGHT), 2)
    pygame.draw.line(surface, LINE_COLOR, (0, center_y), (WIDTH, center_y), 2)
    
def export_overlay():
    #Hide Window
    root = tk.Tk()
    root.withdraw()
    
    #Save Location
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
        title = "Save Overlay As"
    )    
    
    root.destroy()
    
    #IF Canceled
    if not file_path:
        print("Export canceled")
        return
    
    #EXT
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".jpg" or ext == ".jpeg":
        format = "JPEG"
    else:
        format = "PNG"
    
    #Export
    pygame.image.save(screen.subsurface((0, 0, WIDTH, HEIGHT)), file_path)
    print(f"Overlay exported as {format} to: {file_path}")

# Toggles 
def toggle_rule_of_thirds():
    global show_rule_of_thirds
    show_rule_of_thirds = not show_rule_of_thirds
    
def toggle_center_grid():
    global show_center_grid
    show_center_grid = not show_center_grid
    
# Buttons
buttons = [
    Button((10, HEIGHT, 200, BUTTON_HEIGHT), "Rule of Thirds", toggle_rule_of_thirds),
    Button((220, HEIGHT, 200, BUTTON_HEIGHT), "Center Grid", toggle_center_grid),
    Button((430, HEIGHT, 150, BUTTON_HEIGHT), "Export", export_overlay)
]

#Main Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BG_COLOR, (0, 0, WIDTH, HEIGHT))
    
    # Draw overlays
    if show_rule_of_thirds:
        draw_rule_of_thirds(screen)
    if show_center_grid:
        draw_center_grid(screen)
    
    # Draw UI
    pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT, WIDTH, BUTTON_HEIGHT))

    # Draw Buttons
    for btn in buttons:
        btn.draw(screen)
    
    #Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for btn in buttons:
            btn.handle_event(event)
        
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()