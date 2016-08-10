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


cimport cython
from core cimport ReedsSheppStateSpace, sample_cb, type_cb

LEFT = 1
STRAIGHT = 2
RIGHT = 3

cdef class PyReedsSheppPath:
    cdef ReedsSheppStateSpace *thisptr
    cdef double _q0[3]
    cdef double _q1[3]

    def __init__(self, q0, q1, turning_radius):
        self.thisptr = new ReedsSheppStateSpace(turning_radius)
        for i in [0,1,2]:
            self._q0[i] = q0[i]
            self._q1[i] = q1[i]  

    def __dealloc__(self):
        del self.thisptr

    def distance(self):
        return self.thisptr.distance(self._q0, self._q1)

    def sample(self, step_size):
        qs = []

        def f(q):
            qs.append(q)
            return 0
            
        self.thisptr.sample(self._q0, self._q1, step_size, sample_cb, <void*>f)
        return qs
    
    def type(self):
        ts = []
        
        def f(t):
            if t is not 0 : ts.append(t)
            return 0

        self.thisptr.type(self._q0, self._q1, type_cb, <void*>f)
        return tuple(ts)


def path_length(q0, q1, rho):
    return PyReedsSheppPath(q0, q1, rho).distance()

def path_sample(q0, q1, rho, step_size):
    return PyReedsSheppPath(q0, q1, rho).sample(step_size)

def path_type(q0, q1, rho):
    return PyReedsSheppPath(q0, q1, rho).type()
