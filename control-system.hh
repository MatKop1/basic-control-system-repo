#ifndef ConSys
#define ConSys
#include <vector>
namespace control
{
// TOPIC: Discreate Control System
std::vector<double> output(const double& dStop,const double& dTs,const double& dU); // function to calculate response to input signal
}
namespace numeric
{
// TOPIC: Numerical Methods
//dx/dt = y
double func1(double X1);
//dy/dt = u*(1-x^2)*y-x^2
double func2(double &t, double X1, double X2, double U1);
double solveRK4(double t,double dt,double TF,double XX[], double UU[]);
}

#endif