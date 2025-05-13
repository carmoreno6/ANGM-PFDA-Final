# ANGM-PFDA-Final
ANGM 2305.0W2 Final Assignment
# Grid IT UI - Compositional Overlay Tool


## Description
Grid IT UI is an interactive Python tool for artists, photographers, and designers to visualize compositional guides, such as the Rule of Thirds and Center Grid, over digital canvases.

The overlays can be toggled live in the interface and exported as transparent PNGs

## Features
- **Rule of Thirds Overlay**  
  Toggleable grid dividing the canvas into 9 equal areas.
  
- **Center Grid Overlay**  
  Toggleable cross grid highlighting the vertical and horizontal center.
  
- **Export Overlay**  
  Allows users to export the current overlay view as a PNG image file.

- **Interactive UI with Buttons**  
  Real-time toggling and exporting via on-screen buttons using Pygame.

## Challenges
- Integrating UI interactions in Pygame.
- Managing overlays with transparency.
- Ensuring export of the live UI canvas without including UI buttons.
- Adding file dialogs for flexible export locations (optional).


## Usage Instructions
1. Run the Python script:
    ```bash
    python project.py
    ```
2. Use the on-screen buttons to toggle overlays and export.
3. Exported overlays will be saved inside the `overlays_ui_buttons` folder.
