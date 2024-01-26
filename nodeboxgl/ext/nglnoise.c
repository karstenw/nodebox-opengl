// --- PERLIN NOISE --------------------------------------------------------------------
// Based on: Malcolm Kesson, http://www.fundza.com/c4serious/noise/perlin/perlin.html
// © 2002-4 Malcolm Kesson. All rights reserved.

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>
#include <math.h>


// protos
double fade(double);
double lerp(double, double, double);
double grad(int, double, double, double);
double _generate(double, double, double);
static PyObject *generate(PyObject *, PyObject *);
static PyObject *init(PyObject *, PyObject *);


// global
static int p[512];



double fade(double t) {
	return t * t * t * (t * (t * 6 - 15) + 10);
}


double lerp(double t, double a, double b) {
	return a + t * (b - a);
}


double grad(int hash, double x, double y, double z) {
	int     h = hash & 15;
	double u = h < 8 ? x : y;
	double v = h < 4 ? y : h==12 || h==14 ? x : z;

	return ((h&1) == 0 ? u : -u) + ((h&2) == 0 ? v : -v);
}


double _generate(double x, double y, double z) {
	// Find unit cuve that contains point.
	int X = (int)floor(x) & 255;
	int Y = (int)floor(y) & 255;
	int Z = (int)floor(z) & 255;

	// Find relative x, y, z of point in cube.
	x -= floor(x);
	y -= floor(y);
	z -= floor(z);

	// Compute fade curves for each of x, y, z.
	double u = fade(x);
	double v = fade(y);
	double w = fade(z);

	// Hash coordinates of the 8 cube corners.
	int A  = p[X  ] + Y;
	int AA = p[A  ] + Z;
	int AB = p[A+1] + Z;
	int B  = p[X+1] + Y;
	int BA = p[B  ] + Z;
	int BB = p[B+1] + Z;

	// Add blended results from 8 corners of cube.
	return lerp(w, 
		lerp(v, lerp(u, grad(p[AA  ], x  , y  , z  ), 
						grad(p[BA  ], x-1, y  , z  )),
				lerp(u, grad(p[AB  ], x  , y-1, z  ), 
						grad(p[BB  ], x-1, y-1, z  ))),
		lerp(v, lerp(u, grad(p[AA+1], x  , y  , z-1), 
						grad(p[BA+1], x-1, y  , z-1)),
				lerp(u, grad(p[AB+1], x  , y-1, z-1), 
						grad(p[BB+1], x-1, y-1, z-1))));
}

// -------------------------------------------------------------------------------------


static PyObject *
generate(PyObject *self, PyObject *args) {

	double x, y, z, d;   
	if (!PyArg_ParseTuple(args, "ddd", &x, &y, &z))
		return NULL;
	d = _generate(x, y, z);
	return Py_BuildValue("d", d);
}
char generate_docs[] = "generate(x, y, z)";


static PyObject *
init(PyObject *self, PyObject *args) {

	int i;
	PyObject *a;

	if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &a))
		return NULL;

	for(i=0; i<512; i++)
		p[i] = (int)PyLong_AsLong(PyList_GetItem(a, i));
	return Py_BuildValue("");
}
char init_docs[] = "init(a)";


PyMethodDef nglnoisemethods[] = {
	{	"generate",
		(PyCFunction)generate,
		METH_VARARGS,
		generate_docs},

	{	"init",
		(PyCFunction)init,
		METH_VARARGS,
		init_docs},
	
	{ NULL }
};

// yet unused
// static PyObject *NglNoiseError;

char nglnoisemod_docs[] = "Noise functions.";


PyModuleDef nglnoise_mod = {
	PyModuleDef_HEAD_INIT,
	"nglnoise",
	nglnoisemod_docs,
	-1,
	nglnoisemethods,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC
PyInit_nglnoise( void ) { 
	return PyModule_Create( &nglnoise_mod );
}

