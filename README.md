![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](kirigami.jpeg)

# Kirigami Parachute SVG Generator (Version 1)

A Python script to generate **laser-cut SVG patterns** for **Kirigami-style parachutes** using intermittent concentric arc cuts.

---

## Features

- Generates **intermittent concentric circles** between inner and outer diameter
- Adjustable number of rings, segments, and arc-to-gap ratio
- Optional **staggered arc alignment** for structural strength
- Outputs clean **SVG** for laser cutting
- Designed for **Kirigami deployable structures**

---

## Requirements

```bash
pip install matplotlib numpy

python kirigami_parachute_v1.py \
  --outer_diam 120 \
  --inner_diam 15 \
  --num_intermediate 12 \
  --num_segments 24 \
  --arc_fraction 0.75 \
  --stagger \
  --line_width 0.08 \
  --output parachute_v1.svg
```
## Parameters

| Parameter           | Type   | Description                                          | Default               | Required |
|---------------------|--------|------------------------------------------------------|-----------------------|----------|
| `--outer_diam`      | float  | Outer diameter (mm)                                  | —                     | Yes      |
| `--inner_diam`      | float  | Inner diameter (mm)                                  | —                     | Yes      |
| `--num_intermediate`| int    | Number of rings between inner & outer                | 10                    | No       |
| `--num_segments`    | int    | Number of arc/gap segments per ring                  | 20                    | No       |
| `--arc_fraction`    | float  | Fraction of each segment that is **cut** (0.0–1.0)   | 0.8                   | No       |
| `--stagger`         | flag   | Stagger arcs between adjacent rings                  | False                 | No       |
| `--line_width`      | float  | Line width for laser kerf (mm)                       | 0.1                   | No       |
| `--output`          | str    | Output SVG filename

## Usage Exsample
python kirigami.py --outer_diam 100 --inner_diam 10 --num_intermediate 15 --num_segments 30 --arc_fraction 0.7 --output my_parachute.svg

---

# Kirigami Parachute SVG Generator – Version 2 (Multi-Pattern)

Advanced CLI tool with **multiple cut patterns**, **spacing modes**, **spiral twist**, and more.

## New in v2

- 3 patterns: `concentric_arcs`, `spiral_arcs`, `radial_lines`
- Spacing: `linear`, `power`, `log`
- Central hole, boundary circles, wavy cuts (experimental)


## Usage Examples

### 1. Concentric Arcs (Default)
python kirigami-other.py --outer_diam 100 --inner_diam 10 --stagger --output conc.svg


### 2. Spiral Pattern
python kirigami-other.py --outer_diam 120 --pattern spiral_arcs --spiral_twist 18 --num_segments 30 --output spiral.svg


### 3. Radial Lines
python kirigami-other.py --outer_diam 100 --pattern radial_lines --num_intermediate 15 --output radial.svg


## Full CLI Options

| Flag                  | Type   | Description                                   | Default               |
|-----------------------|--------|-----------------------------------------------|-----------------------|
| `--outer_diam`        | float  | Outer diameter                                | **Required**          |
| `--inner_diam`        | float  | Inner diameter                                | 0.0                   |
| `--num_intermediate`  | int    | Number of rings/steps                         | 10                    |
| `--num_segments`      | int    | Segments per ring or radials                  | 20                    |
| `--arc_fraction`      | float  | Cut fraction per segment                      | 0.8                   |
| `--pattern`           | str    | `concentric_arcs`, `spiral_arcs`, `radial_lines`| `concentric_arcs`     |
| `--spacing`           | str    | `linear`, `power`, `log`                      | `linear`              |
| `--radial_exponent`   | float  | For power spacing                             | 1.0                   |
| `--spiral_twist`      | float  | Degrees per ring (spiral)                     | 10.0                  |
| `--stagger`           | flag   | Stagger concentric arcs                       | —                     |
| `--draw_bounds`       | flag   | Draw full inner/outer circles                 | —                     |
| `--central_hole`      | float  | Diameter of center hole                       | 0.0                   |
| `--line_width`        | float  | Laser cut width (mm)                          | 0.1                   |
| `--output`            | str    | Output SVG file                               | `kirigami_parachute.svg` |


