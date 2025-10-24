import argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

def main():
    parser = argparse.ArgumentParser(description="Generate SVG for Kirigami parachute with intermittent concentric circles.")
    parser.add_argument('--outer_diam', type=float, required=True, help="Outer diameter of the circle.")
    parser.add_argument('--inner_diam', type=float, required=True, help="Inner diameter of the circle.")
    parser.add_argument('--num_intermediate', type=int, default=10, help="Number of intermediate concentric circles.")
    parser.add_argument('--num_segments', type=int, default=20, help="Number of arc segments per circle.")
    parser.add_argument('--arc_fraction', type=float, default=0.8, help="Fraction of the segment that is an arc (vs gap).")
    parser.add_argument('--stagger', action='store_true', default=True, help="Stagger the arcs between adjacent rings.")
    parser.add_argument('--line_width', type=float, default=0.1, help="Line width for the cuts.")
    parser.add_argument('--output', type=str, default='kirigami_parachute.svg', help="Output SVG file name.")

    args = parser.parse_args()

    outer_r = args.outer_diam / 2
    inner_r = args.inner_diam / 2
    radii = np.linspace(inner_r, outer_r, args.num_intermediate + 2)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Draw inner and outer full circles
    ax.add_patch(Circle((0, 0), inner_r, fill=False, linewidth=args.line_width))
    ax.add_patch(Circle((0, 0), outer_r, fill=False, linewidth=args.line_width))

    # Draw intermediate intermittent arcs
    for i, r in enumerate(radii[1:-1]):
        total_angle = 360
        segment_angle = total_angle / args.num_segments
        arc_angle = segment_angle * args.arc_fraction
        start_angle_offset = 0 if not args.stagger else (i % 2) * (segment_angle / 2)
        for j in range(args.num_segments):
            start_angle = start_angle_offset + j * segment_angle
            ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=start_angle, theta2=start_angle + arc_angle, linewidth=args.line_width))

    # Set plot limits
    margin = outer_r * 1.1
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    plt.axis('off')
    plt.savefig(args.output, format='svg')
    plt.close()

if __name__ == "__main__":
    main()