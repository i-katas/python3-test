#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject* _abs(PyObject *self, PyObject *args) {
    long n;
    if(!PyArg_ParseTuple(args, "l", &n)) {
        return NULL;
    }
    return PyLong_FromLong(abs(n));
}

static PyMethodDef CMathMethods[] {
    {"abs", _abs, METH_VARARGS, "absolute value of a number"},
    {NULL, NULL, 0, NULL}
};

static PyModuleDef CMathModule {
    PyModuleDef_HEAD_INIT,
    "cmath",
    "C math API",
    -1,
    CMathMethods
};

PyMODINIT_FUNC PyInit_cmath() {
    return PyModule_Create(&CMathModule);
}

//when embedding ptyhon, the PyInit_cmath() is not called automatically unless the entry point is called to add module to initialization table
int main(int argc, char *argv[]) {
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("cmath", PyInit_cmath);

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("cmath");
    PyMem_RawFree(program);
    return 0;
}
