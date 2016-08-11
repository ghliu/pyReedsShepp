#*********************************************************************
#
# Software License Agreement (BSD License)
#
#  Copyright (c) 2016, Guan-Horng Liu.
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
# Author:  Guan-Horng Liu
#********************************************************************/

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