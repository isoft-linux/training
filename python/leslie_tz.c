/* 
 * Copyright (C) 2016 Leslie Zhai <xiang.zhai@i-soft.com.cn>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <Python.h>
#include <time.h>

#define INT(v) PyInt_FromLong(v)

static PyObject *gmtoff(PyObject *self, PyObject *args);

static PyMethodDef leslie_tz_methods[] = 
{
    {"gmtoff", gmtoff, 0, "Leslie timezone get gmtoff"}, 
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initleslie_tz() 
{
    PyObject *m = NULL;

    m = Py_InitModule("leslie_tz", leslie_tz_methods);
    if (!m)
        return;
}

static PyObject *gmtoff(PyObject *self, PyObject *args) 
{
    time_t cur_time = time(NULL);
    struct tm *local_tm = localtime(&cur_time);

    return INT(local_tm->tm_gmtoff / 3600);
}
