#include "control-system.h"
#include <iostream>
#include <vector>

std::vector<double> output(const double& dStop,const double& dTs,const double& dU)
{
    //y(k) = 1.4*y(k-1) - 0.5*y(k-2)+0.8*u(k-2)
    // initial condition
    double y1{0};
    double y2{0};
    double u1{0};
    double u2{0};
    // return value
    std::vector<double> y{0};
    // update status
    for (int i{0} ; i < 100; i++)
    {
        y.push_back(1.4*y1 - 0.5*y2 + 0.8*u2);
        // update history
        y2 = y1;
        y1 = y.back();
        u2 = u1;
        u1 = dU;
    }
    return y;
}
   
int main()
{

    std::vector<double> y = output(2,0.1,1);
    for (auto i:y)
        std::cout << i << std::endl;
    //foo();

    return 0;
} 