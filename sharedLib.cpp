#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>

extern "C" {
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

    double func1(double X1)
    {
        return X1;
    }

    double func2(double &t, double X1, double X2, double U1)
    {
        double F2{U1*(1-std::pow(X2,2))*X1-X2};
        return F2;
    }

    double solveRK4(double t,double dt,double TF,double XX[], double UU[])
    {
        // const int N{2};
        // const int M{1};
        // double X[N+1];
        // double U[M+1];

        //RK4 constants
        double a1{0.166};
        double a23{0.333};
        double a4{0.166};
        
        //function approximators
        double K1{},K2{},K3{},K4{};
        double L1{},L2{},L3{},L4{};

        //initial conditions for example
        // dt{0.01};
        // TF{150};
        // t = 0.0;
        XX[1]=0.01;
        XX[2]=0;
        
        std::ofstream fout("sim.csv");
        if(!fout)
            std::cout <<"\nError!\n";
        else
        {
            //fout.open("sim.csv");
            fout << std::scientific;
            fout.precision(8);
            fout << "%Time(s)" << ";" <<"X-Position (X[2])" << ";" << "Y-Position (X[1])" << ";" << "Input U" << "\n";
            while(t < TF)
            {
                // input 
                UU[1] = std::sin(std::pow(t,0.2));

                //placeholders
                double t_2 = t+0.5*dt;
                double t_3 = t+dt;

                //at each time step, forward iterations
                K1 = dt*func1(XX[1]);
                L1 = dt*func2(t,XX[1],XX[2],UU[1]);

                K2 = dt*func1(XX[1]+0.5*L1);
                L2 = dt*func2(t_2,XX[1]+0.5*L1,XX[2]+0.5*K1,UU[1]);

                K3 = dt*func1(XX[1]+0.5*L2);
                L3 = dt*func2(t_2,XX[1]+0.5*L2,XX[2]+0.5*K2,UU[1]);
                
                K4 = dt*func1(XX[1]+0.5*L3);
                L4 = dt*func2(t_3,XX[1]+0.5*L3,XX[2]+0.5*K3,UU[1]);
                //update X-Position
                XX[2] = XX[2]+a1*(K1+K4)+a23*(K2+K3);
                //update Y-Position
                XX[1] = XX[1]+a1*(L1+L4)+a23*(L2+L3);
                //output
                fout << t << ";" << XX[2] << ";" << XX[1] << ";" << UU[1] << "\n";
                t+=dt;
            }
            fout.close();
            //at the end of the simulation
            std::cout <<"X[1] = " << XX[1] << std::endl;
            std::cout <<"X[2] = " << XX[2] << std::endl;
            std::cout <<"t = " << t << std::endl;
            std::system("pause");
        }
        double dRet{0.0};
        return dRet;
    }
}