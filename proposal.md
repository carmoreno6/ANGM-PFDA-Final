#CompositionGuideCreator: Creates Helpful Overalys in various formats to Help With Compositing

## Description
A tool that would create several types of compositional overlays used in artistic composition guides such as Rule of Thirds, Golden Ratio, Golden Triangle to aid visual artists, designers, and photographers in crafting aesthetically balanced compositions. Or even a starting base for most artworks.

##Features

- **Rule of Thirds**
  - Draws two vertical and two horizontal lines dividing the canvas into thirds.
- **Golden Ratio / Fibonacci Spiral**
  - Constructs rectangles and spirals based on Fibonacci proportions.
- **Golden Triangle**
  - Uses diagonal lines and triangles for classic composition structure.
- **Perfect Rectangle / Center Guides**
  - Adds centered crosshairs or balanced rectangles for symmetrical layouting.
- **Aspect Ratio Frames**
  - Shows common aspect ratios (e.g. 1:1, 4:3, 16:9) within the canvas.
- **Custom Grid Generator**
  - User specifies number of rows and columns for flexible layout planning.
- **Combined Overlay Mode**
  - Allows users to generate and export multiple guides in one overlay.
- **Overlay Color & Opacity Settings**
  - Users can define line color and transparency to suit their visual needs.
- **Image Underlay (Optional)**
  - Load an existing image and apply overlays for composition preview or export.
- **Multiple Export Formats**
  - Overlays can be exported as:
    - `.png` (transparent)
    - `.jpeg` (white background)
    - `.svg` (vector for infinite scalability)

## Challenges
- Researching and implementing  math for the golden spiral and other complex shapes.
- Handling resolution scaling, transparency, and compositing and technical aspects
- Supporting dynamic canvas sizes and responsive line positioning.
- Managing multiple export formats including SVG.
- Attempting to create a GUI of some sort for ease of use

## Outcomes

**Ideal Outcome:**
- A tool that can generate and export all overlay types on any canvas size in whichever format requested with full user customization.

**Minimal Viable Outcome:**
- A code that can generate a few basic overlays at fixed resolution and export them as transparent PNGs.

## Milestones

- 1. Add Golden Ratio and Golden Triangle overlays.
  2. Add PNG and JPEG export options with dynamic resolution.
  3. Add custom grid, aspect ratio frames, and SVG export
