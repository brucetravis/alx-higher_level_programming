#include <Python.h>
#include <float.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: Pointer to a PyObject representing a bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    size_t size = PyBytes_GET_SIZE(p);
    size_t i;
    char *data = PyBytes_AS_STRING(p);

    printf("[.] bytes object info\n");
    printf("  size: %zu\n", size);
    printf("  trying string: %s\n", data);
    printf("  first %zu bytes: ", size > 10 ? 10 : size);
    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx%c", data[i], i == size - 1 ? '\n' : ' ');
}

/**
 * print_python_list - Print information about Python list objects
 * @p: Pointer to a PyObject representing a list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    size_t size = PyList_Size(p);
    size_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zu\n", size);
    printf("[*] Allocated = %zu\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %zu: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

/**
 * print_python_float - Print information about Python float objects
 * @p: Pointer to a PyObject representing a float object
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *float_obj = (PyFloatObject *)p;
    double value = float_obj->ob_fval;

    printf("[.] float object info\n");
    printf("  value: %lf\n", value);
}

int main(void)
{
    return 0;
}
