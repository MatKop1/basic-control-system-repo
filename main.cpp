#include "control-system.hh"
#include <iostream>
#include <vector>
#include <fstream>
int main()
{
    // generate response
    // std::vector<double> y = control::output(2,0.1,1);
    // for (auto i:y)
    //     std::cout << i << std::endl;

    // solving nonlinear equations
    // initialization
    double t{0.0};       //time t0
    double dt{0.01};     //step time 
    double TF{150};      //simulation time
    double XX[3]{0.01,0}; // states X = [y x]' -> X[1] = y, X[2] = x 
    double UU[2]{0};      // input 
    numeric::solveRK4(t,dt,TF,XX,UU);   
    return 0;
} 