#include <iostream>

extern "C" {
    void greet() {
        std::cout << "Hello from C++ library!" << std::endl;
    }

    int add(int a, int b) {
        return a + b;
    }
}