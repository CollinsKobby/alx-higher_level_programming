#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - print info about python lists
 * @p: address of pyobject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PySIZE(p); i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
