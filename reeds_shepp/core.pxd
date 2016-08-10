cimport cython

ctypedef int (*ReedsSheppPathSamplingCallback)(double q[3], void* user_data)
ctypedef int (*ReedsSheppPathTypeCallback) (int t, void* user_data)

cdef extern from "reeds_shepp.h":
    cdef cppclass ReedsSheppStateSpace:
        ReedsSheppStateSpace(double turningRadius)
        double distance(double q0[3], double q1[3])
        void sample(double q0[3], double q1[3], double step_size, ReedsSheppPathSamplingCallback cb, void* user_data)
        void type(double q0[3], double q1[3], ReedsSheppPathTypeCallback cb, void* user_data)

cdef inline int sample_cb(double q[3], void* f):
    qn = (q[0], q[1], q[2])
    return (<object>f)(qn)

cdef inline int type_cb(int t, void* f):
    return (<object>f)(t)