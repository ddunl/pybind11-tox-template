#include <pybind11/pybind11.h>
#include "cpp/add.cpp"
#include "cpp/sub.cpp"

PYBIND11_MODULE(cpplib, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers");
    m.def("sub", &sub, "A function which subtracts two numbers");
}
