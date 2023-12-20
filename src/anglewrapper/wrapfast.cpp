#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;

/**
 * @brief wraps the angle to +/- 180 degrees
 * 
 * @param angle 
 * @return double 
 */
double to_180(double angle) {
    if (angle > 180) {
        return angle - 360;
    } else if (angle < -180) {
        return angle + 360;
    } else {
        return angle;
    }
}

std::vector<double> to_180(std::vector<double> angles) {
    for (double& angle : angles) {
        angle = to_180(angle);
    }
    return angles;
}

/**
 * @brief wraps the angle to +/- 180 degrees
 * 
 * @param angle 
 * @return double 
 */
double to_360(double angle) {
    if (angle > 360) {
        return angle - 360;
    } else if (angle < 0) {
        return angle + 360;
    } else {
        return angle;
    }
}

std::vector<double> to_360(std::vector<double> angles) {
    for (double& angle : angles) {
        angle = to_360(angle);
    }
    return angles;
}

/**
 * @brief wraps the angle to +/- pi radians
 * 
 * @param angle
 * @return double 
 */

double to_pi(double angle) {
    if (angle > M_PI) {
        return angle - 2*M_PI;
    } else if (angle < -M_PI) {
        return angle + 2*M_PI;
    } else {
        return angle;
    }   
}

std::vector<double> to_pi(std::vector<double> angles) {
    for (double& angle : angles) {
        angle = to_pi(angle);
    }
    return angles;
}

/**
 * @brief wraps the angle to +/- 2*pi radians
 * 
 * @param angle
 * @return double 
 */
double to_2pi(double angle) {
    if (angle > 2*M_PI) {
        return angle - 2*M_PI;
    } else if (angle < 0) {
        return angle + 2*M_PI;
    } else {
        return angle;
    }   
}

std::vector<double> to_2pi(std::vector<double> angles) {
    for (double& angle : angles) {
        angle = to_2pi(angle);
    }
    return angles;
}


PYBIND11_MODULE(wrapfast, m) {
    m.doc() = "A fast module for wrapping angles to [-180, 180] and [-pi, pi], and [0, 360] and [0, 2pi]";

    m.def("to_180", py::overload_cast<double>(&to_180), "A function that wraps an angle to [-180, 180]");
    m.def("to_360", py::overload_cast<double>(&to_360), "A function that wraps an angle to [0, 360]");
    m.def("to_pi", py::overload_cast<double>(&to_pi), "A function that wraps an angle to [-pi, pi]");
    m.def("to_2pi", py::overload_cast<double>(&to_2pi), "A function that wraps an angle to [0, 2pi]");
    m.def("to_180", py::overload_cast<std::vector<double>>(&to_180), "A function that wraps an interable of angles to [-180, 180]");
    m.def("to_360", py::overload_cast<std::vector<double>>(&to_360), "A function that wraps an interable of angles to [0, 360]");
    m.def("to_pi", py::overload_cast<std::vector<double>>(&to_pi), "A function that wraps an interable of angles to [-pi, pi]");
    m.def("to_2pi", py::overload_cast<std::vector<double>>(&to_2pi), "A function that wraps an interable of angles to [0, 2pi]");
    /**
    m.def("to_180", [](py::array_t<double> input){
        py::buffer_info buf_info = input.request();
        double *ptr = static_cast<double *>(buf_info.ptr);
        std::vector<double> angles(ptr, ptr + buf_info.size);
        angles = to_2pi(angles);
        py::array_t<double> result(buf_info.size, angles.data());
        return result;
    }
    , "A function that wraps an interable of angles to [-180, 180]");
    
    m.def("to_360", [](py::array_t<double> input){
        py::buffer_info buf_info = input.request();
        double *ptr = static_cast<double *>(buf_info.ptr);
        std::vector<double> angles(ptr, ptr + buf_info.size);
        angles = to_360(angles);
        py::array_t<double> result(buf_info.size, angles.data());
        return result;
    }
    , "A function that wraps an interable of angles to [0, 360]");
    m.def("to_pi", [](py::array_t<double> input){
        py::buffer_info buf_info = input.request();
        double *ptr = static_cast<double *>(buf_info.ptr);
        std::vector<double> angles(ptr, ptr + buf_info.size);
        angles = to_pi(angles);
        py::array_t<double> result(buf_info.size, angles.data());
        return result;
    }
    , "A function that wraps an interable of angles to [-pi, pi]");
    m.def("to_2pi", [](py::array_t<double> input){
        py::buffer_info buf_info = input.request();
        double *ptr = static_cast<double *>(buf_info.ptr);
        std::vector<double> angles(ptr, ptr + buf_info.size);
        angles = to_2pi(angles);
        py::array_t<double> result(buf_info.size, angles.data());
        return result;
    }
    , "A function that wraps an interable of angles to [0, 2pi]");
    */
}