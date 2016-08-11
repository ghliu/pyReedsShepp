import reeds_shepp
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


step_size = 0.5
rho = 5.8 # turning radius

qs = [
    [( 0.0, 0.0,     0.0), ( 0.0, 0.0,   np.pi)],
    [( 0.0, 0.0, np.pi/4), ( 3.0, 4.0,     0.0)],
    [( 4.0, 4.0, np.pi/4), ( 0.0, 4.0,     0.0)],
    [( 4.0, 0.0,     0.0), (-3.0, 4.0,   np.pi)],
    [(-4.0, 0.0,     0.0), ( 3.0, 4.0, np.pi/3)],
    [( 4.0, 4.0,     0.0), ( 3.0, 4.0, np.pi/2)]
]

def get_point(center, radius, orin):
	x = center[0] + radius * np.cos(orin)
	y = center[1] + radius * np.sin(orin)
	return (x,y)

def plot_car(q):
    a = get_point(q[:-1], step_size, q[2])
    b = get_point(q[:-1], step_size/2, q[2]+150./180.*np.pi)
    c = get_point(q[:-1], step_size/2, q[2]-150./180.*np.pi)
    tri = np.array([a,b,c,a])
    plt.plot(tri[:,0], tri[:,1], 'g-')

def plot_path(q0, q1):
    qs = reeds_shepp.path_sample(q0, q1, rho, step_size)
    xs = [q[0] for q in qs]
    ys = [q[1] for q in qs]
    plt.plot(xs, ys, 'b-')
    plt.plot(xs, ys, 'r.')
    plot_car(q0)
    plot_car(q1)
    plt.axis('equal')


def plot_table(cols):
    rows = ((len(qs)) / cols)
    for i,(q0, q1) in enumerate(qs):
        plt.subplot(rows, cols, i+1)
        plot_path(q0, q1)
        dist = reeds_shepp.path_length(q0, q1, rho)
        plt.title('length: {:.2f}'.format(dist))
    plt.savefig('fig/demo.png')
    plt.show()

if __name__ == "__main__":
    plot_table(3)