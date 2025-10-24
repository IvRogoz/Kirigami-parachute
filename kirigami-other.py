import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Wedge

def draw_concentric_arcs(ax, args, radii):
    # Draw inner and outer full circles if specified
    if args.draw_bounds:
        ax.add_patch(Circle((0, 0), args.inner_r, fill=False, linewidth=args.line_width))
        ax.add_patch(Circle((0, 0), args.outer_r, fill=False, linewidth=args.line_width))

    # Draw intermediate intermittent arcs
    for i, r in enumerate(radii):
        total_angle = 360
        segment_angle = total_angle / args.num_segments
        arc_angle = segment_angle * args.arc_fraction
        start_angle_offset = 0 if not args.stagger else (i % 2) * (segment_angle / 2)
        for j in range(args.num_segments):
            start_angle = start_angle_offset + j * segment_angle
            if args.wavy:
                # For wavy, use a series of small arcs or approximate sine
                # But for simplicity, we can use Arc with some modification, but skip for now
                pass
            ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=start_angle, theta2=start_angle + arc_angle, linewidth=args.line_width))

def draw_spiral_arcs(ax, args, radii):
    # Spiral pattern: cumulative offset
    cumulative_offset = args.spiral_twist
    for i, r in enumerate(radii):
        total_angle = 360
        segment_angle = total_angle / args.num_segments
        arc_angle = segment_angle * args.arc_fraction
        start_angle_offset = i * cumulative_offset
        for j in range(args.num_segments):
            start_angle = start_angle_offset + j * segment_angle
            ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=start_angle, theta2=start_angle + arc_angle, linewidth=args.line_width))

def draw_radial_lines(ax, args):
    # Draw radial intermittent lines
    num_radii = args.num_segments  # Reuse num_segments for number of radials
    inner_r = args.inner_r
    outer_r = args.outer_r
    for j in range(num_radii):
        angle = j * (360 / num_radii)
        rad = np.deg2rad(angle)
        # Intermittent: draw lines with gaps
        r_steps = np.linspace(inner_r, outer_r, args.num_intermediate + 2)
        for k in range(len(r_steps) - 1):
            r1 = r_steps[k]
            r2 = r_steps[k+1] * args.arc_fraction  # Fraction for length
            x1, y1 = r1 * np.cos(rad), r1 * np.sin(rad)
            x2, y2 = r2 * np.cos(rad), r2 * np.sin(rad)
            ax.plot([x1, x2], [y1, y2], linewidth=args.line_width, color='black')

def get_radii(args):
    if args.spacing == 'linear':
        return np.linspace(args.inner_r, args.outer_r, args.num_intermediate + 2)[1:-1]
    elif args.spacing == 'power':
        lin = np.linspace(0, 1, args.num_intermediate + 2)**args.radial_exponent
        return args.inner_r + (args.outer_r - args.inner_r) * lin[1:-1]
    elif args.spacing == 'log':
        if args.inner_r == 0:
            args.inner_r = 0.01  # Avoid log(0)
        log_inner = np.log(args.inner_r)
        log_outer = np.log(args.outer_r)
        logs = np.linspace(log_inner, log_outer, args.num_intermediate + 2)
        return np.exp(logs)[1:-1]

def main():
    parser = argparse.ArgumentParser(description="Generate SVG for Kirigami parachute variants with intermittent cuts. Use -h for help.")
    parser.add_argument('--outer_diam', type=float, required=True, help="Outer diameter of the circle.")
    parser.add_argument('--inner_diam', type=float, default=0.0, help="Inner diameter of the circle (default: 0.0).")
    parser.add_argument('--num_intermediate', type=int, default=10, help="Number of intermediate rings or steps (default: 10).")
    parser.add_argument('--num_segments', type=int, default=20, help="Number of segments per ring or radial lines (default: 20).")
    parser.add_argument('--arc_fraction', type=float, default=0.8, help="Fraction of the segment that is cut (vs gap) (default: 0.8).")
    parser.add_argument('--stagger', action='store_true', help="Stagger the arcs between adjacent rings (default: False).")
    parser.add_argument('--line_width', type=float, default=0.1, help="Line width for the cuts (default: 0.1).")
    parser.add_argument('--output', type=str, default='kirigami_parachute.svg', help="Output SVG file name (default: kirigami_parachute.svg).")
    parser.add_argument('--pattern', type=str, default='concentric_arcs', choices=['concentric_arcs', 'spiral_arcs', 'radial_lines'],
                        help="Pattern type: concentric_arcs, spiral_arcs, radial_lines (default: concentric_arcs).")
    parser.add_argument('--spacing', type=str, default='linear', choices=['linear', 'power', 'log'],
                        help="Radial spacing type: linear, power, log (default: linear).")
    parser.add_argument('--radial_exponent', type=float, default=1.0, help="Exponent for power spacing (default: 1.0).")
    parser.add_argument('--spiral_twist', type=float, default=10.0, help="Twist angle in degrees for spiral pattern (default: 10.0).")
    parser.add_argument('--draw_bounds', action='store_true', help="Draw full inner and outer boundary circles (default: False).")
    parser.add_argument('--central_hole', type=float, default=0.0, help="Diameter of central hole for attachment (default: 0.0).")
    parser.add_argument('--wavy', action='store_true', help="Make arcs wavy (experimental, default: False).")

    args = parser.parse_args()
    args.inner_r = args.inner_diam / 2
    args.outer_r = args.outer_diam / 2

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    radii = get_radii(args)

    if args.pattern == 'concentric_arcs':
        draw_concentric_arcs(ax, args, radii)
    elif args.pattern == 'spiral_arcs':
        draw_spiral_arcs(ax, args, radii)
    elif args.pattern == 'radial_lines':
        draw_radial_lines(ax, args)

    # Add central hole if specified
    if args.central_hole > 0:
        ax.add_patch(Circle((0, 0), args.central_hole / 2, fill=False, linewidth=args.line_width))

    # Set plot limits
    margin = args.outer_r * 1.1
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    plt.axis('off')
    plt.savefig(args.output, format='svg')
    plt.close()

if __name__ == "__main__":
    main()