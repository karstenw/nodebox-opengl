#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>
#include <math.h>


// protos
float _fast_inverse_sqrt(float);
void _angle(double, double, double, double, double *);
void _distance(double, double, double, double, double *);
void _coordinates(double, double, double, double, double *, double *);
void _rotate(double, double, double, double, double, double *, double *);
void _smoothstep(double, double, double, double *);
void _superformula(double, double, double, double, double, double *, double *);
void _mmult(double, double, double, double, double, double, double, double, double,
			double, double, double, double, double, double, double, double, double,
			double *, double *, double *, double *, double *, double *, double *, double *, double *);


// --- FAST INVERSE SQRT --------------------------------------------------------
// Chris Lomont, http://www.math.purdue.edu/~clomont/Math/Papers/2003/InvSqrt.pdf
float _fast_inverse_sqrt(float x) {
    float xhalf = 0.5f*x;
    int i = *(int*)&x;
    i = 0x5f3759df - (i>>1);
    x = *(float*)&i;
    x = x*(1.5f-xhalf*x*x);
    return x;
}

// --- ANGLE --------------------------------------------------------------------
void _angle(double x0, double y0, double x1, double y1, double *a) {
    *a = atan2(y1-y0, x1-x0) / M_PI * 180;
}

// --- DISTANCE -----------------------------------------------------------------
void _distance(double x0, double y0, double x1, double y1, double *d) {
    *d = sqrt((x1-x0)*(x1-x0) + (y1-y0)*(y1-y0));
}

// --- COORDINATES --------------------------------------------------------------
void _coordinates(double x0, double y0, double d, double a, double *x1, double *y1) {
    *x1 = x0 + cos(a/180*M_PI) * d;
    *y1 = y0 + sin(a/180*M_PI) * d;
}

// --- ROTATE -------------------------------------------------------------------
void _rotate(double x, double y, double x0, double y0, double a, double *x1, double *y1) {
    x = x-x0;
    y = y-y0;
    double u = cos(a/180*M_PI);
    double v = sin(a/180*M_PI);
    *x1 = x*u-y*v+x0;
    *y1 = y*u+x*v+y0;
}

// --- SMOOTHSTEP ---------------------------------------------------------------
void _smoothstep(double a, double b, double x, double *t) {
    if (x < a) {
        *t = 0.0;
    } else if (x >= b) {
        *t = 1.0;
    } else {
        x = (x-a) / (b-a);
        *t = x*x * (3-2*x);
    }
}

// --- SUPERFORMULA -------------------------------------------------------------

void _superformula(double m, double n1, double n2, double n3, double phi, double *x, double *y) {
    double a=1.0, b=1.0, r;
    if (n1 != 0) { 
        r = pow(pow(fabs(cos(m*phi/4.0)/a), n2) + 
            pow(fabs(sin(m*phi/4.0)/b), n3), 1.0/n1);
    }
    if (n1 == 0 || fabs(r) == 0) {
        *x = 0;
        *y = 0;
    } else {
        r = 1.0 / r;
        *x = r*cos(phi);
        *y = r*sin(phi);
    }
}

// --- MATRIX MULTIPLY ----------------------------------------------------------

void _mmult(double  a0, double  a1, double  a2, double  a3, double  a4, double  a5, double  a6, double  a7, double  a8,
            double  b0, double  b1, double  b2, double  b3, double  b4, double  b5, double  b6, double  b7, double  b8,
            double *c0, double *c1, double *c2, double *c3, double *c4, double *c5, double *c6, double *c7, double *c8) {
    *c0 = a0*b0 + a1*b3;
    *c1 = a0*b1 + a1*b4;
    *c2 = 0;
    *c3 = a3*b0 + a4*b3;
    *c4 = a3*b1 + a4*b4;
    *c5 = 0;
    *c6 = a6*b0 + a7*b3 + b6;
    *c7 = a6*b1 + a7*b4 + b7;
    *c8 = 1;
}

// ------------------------------------------------------------------------------

static PyObject *
fast_inverse_sqrt(PyObject *self, PyObject *args) {
    double x;   
    if (!PyArg_ParseTuple(args, "d", &x))
        return NULL;
    x = _fast_inverse_sqrt(x);
    return Py_BuildValue("d", x);
}

static PyObject *
angle(PyObject *self, PyObject *args) {
    double x0, y0, x1, y1, a;   
    if (!PyArg_ParseTuple(args, "dddd", &x0, &y0, &x1, &y1))
        return NULL;
    _angle(x0, y0, x1, y1, &a);
    return Py_BuildValue("d", a);
}

static PyObject *
distance(PyObject *self, PyObject *args) {
    double x0, y0, x1, y1, d;   
    if (!PyArg_ParseTuple(args, "dddd", &x0, &y0, &x1, &y1))
        return NULL;
    _distance(x0, y0, x1, y1, &d);
    return Py_BuildValue("d", d);
}

static PyObject *
coordinates(PyObject *self, PyObject *args) {
    double x0, y0, d, a, x1, y1;   
    if (!PyArg_ParseTuple(args, "dddd", &x0, &y0, &d, &a))
        return NULL;
    _coordinates(x0, y0, d, a, &x1, &y1);
    return Py_BuildValue("dd", x1, y1);
}

static PyObject *
rotate(PyObject *self, PyObject *args) {
    double x, y, x0, y0, a, x1, y1;   
    if (!PyArg_ParseTuple(args, "ddddd", &x, &y, &x0, &y0, &a))
        return NULL;
    _rotate(x, y, x0, y0, a, &x1, &y1);
    return Py_BuildValue("dd", x1, y1);
}

static PyObject *
smoothstep(PyObject *self, PyObject *args) {
    double a, b, x, t;
    if (!PyArg_ParseTuple(args, "ddd", &a, &b, &x))
        return NULL;
    _smoothstep(a, b, x, &t);
    return Py_BuildValue("d", t);
}

static PyObject *
superformula(PyObject *self, PyObject *args) {
    double m, n1, n2, n3, phi, x, y;
    if (!PyArg_ParseTuple(args, "ddddd", &m, &n1, &n2, &n3, &phi))
        return NULL;
    _superformula(m, n1, n2, n3, phi, &x, &y);
    return Py_BuildValue("dd", x, y);
}

static PyObject *
mmult(PyObject *self, PyObject *args) {
    double a0, a1, a2, a3, a4, a5, a6, a7, a8;
    double b0, b1, b2, b3, b4, b5, b6, b7, b8;
    double c0, c1, c2, c3, c4, c5, c6, c7, c8;
    if (!PyArg_ParseTuple(args, "dddddddddddddddddd", 
        &a0, &a1, &a2, &a3, &a4, &a5, &a6, &a7, &a8,
        &b0, &b1, &b2, &b3, &b4, &b5, &b6, &b7, &b8))
        return NULL;
    _mmult( a0,  a1,  a2,  a3,  a4,  a5,  a6,  a7,  a8,
            b0,  b1,  b2,  b3,  b4,  b5,  b6,  b7,  b8,
           &c0, &c1, &c2, &c3, &c4, &c5, &c6, &c7, &c8);
    return Py_BuildValue("ddddddddd", c0, c1, c2, c3, c4, c5, c6, c7, c8);
}

// ------------------------------------------------------------------------------

PyMethodDef nglgeometry_methods[]={
    { "fast_inverse_sqrt", (PyCFunction)fast_inverse_sqrt, METH_VARARGS, "Fast inverse square root." },
    { "angle", (PyCFunction)angle, METH_VARARGS, "angle(x1,y1,x2,y2)." },
    { "distance", (PyCFunction)distance, METH_VARARGS, "distance(x1,y1,x2,y2)." },
    { "coordinates", (PyCFunction)coordinates, METH_VARARGS, "coordinates(x0, y0, d, a, x1, y1)." }, 
    { "rotate", (PyCFunction)rotate, METH_VARARGS, "rotate( x, y, x0, y0, a, x1, y1)." },
    { "smoothstep", (PyCFunction)smoothstep, METH_VARARGS, "smoothstep(a, b, x, t)." },
    { "superformula", (PyCFunction)superformula, METH_VARARGS, "superformula(m, n1, n2, n3, phi)." },
    { "mmult", (PyCFunction)mmult, METH_VARARGS, "mmult(a0, a1, a2, a3, a4, a5, a6, a7, a8, b0, b1, b2, b3, b4, b5, b6, b7, b8)." }, 
    { NULL }
};

static PyObject *NglGeometryError;

char nglgeometrymod_docs[] = "fast_inverse_sqrt, angle, distance, coordinates, rotate, smoothstep, superformula & mmult.";

PyModuleDef nglgeometry_mod = {
	PyModuleDef_HEAD_INIT,
	"nglgeometry",
	nglgeometrymod_docs,
	-1,
	nglgeometry_methods,
	NULL,
	NULL,
	NULL,
	NULL
};




PyMODINIT_FUNC
PyInit_nglgeometry(void) {
	PyObject *m;
	
	m = PyModule_Create( &nglgeometry_mod );
	if (m == NULL)
		return NULL;
	
	NglGeometryError = PyErr_NewException("nglgeometry.error", NULL, NULL);
	Py_XINCREF(NglGeometryError);
	if (PyModule_AddObject(m, "error", NglGeometryError) < 0) {
		Py_XDECREF(NglGeometryError);
		Py_CLEAR(NglGeometryError);
		Py_DECREF(m);
		return NULL;
	}
    return m;
}

