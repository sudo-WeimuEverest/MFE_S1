#include<iostream>
#include<cmath>
#include<cstring>
#include<fstream>
#define r 0.0305
#define S0 3.014
#define M_E 2.71828182845904523536
#define N 12
#define T 5/365.0
using namespace std;
struct V{
 double F0;
 double price[100][100];
};
int main(){
    V v;
    v.F0 = S0*pow(M_E, r*T);
    //文件第1行是c的价格，第2行p的价格，第三行E
    ifstream infile("v1.txt");
    int pos = 0;
    for (int i = 0; i < N * 3; i++){
        int j = i%N;
        if (j == 0&&i!=0){
            pos++;
        }  
    infile >> v.price[pos][j];
    }
    infile.close();
 //sum记录两个微积分的和
    double sum = 0;
    for (int i = 0; i < N-1; i++){
        if (v.price[2][i] < v.F0&&v.price[2][i+1]<v.F0){
            double deltaE = v.price[2][i + 1] - v.price[2][i];
            double E_2 = pow((v.price[2][i + 1] + v.price[2][i]) / 2, 2);
            double p = (v.price[1][i] + v.price[1][i + 1]) / 2;
            sum = sum + (p / E_2) * deltaE;
        }
        else if (v.price[2][i] < v.F0&&v.price[2][i + 1] >= v.F0){
            double deltaE = v.F0 - v.price[2][i];
            double E_2 = pow((v.F0 + v.price[2][i]) / 2, 2);
            double p = (v.price[1][i] + v.price[1][i + 1]) / 2;
            p = (p + v.price[1][i]) / 2;
            sum = sum + (p / E_2) * deltaE;
            deltaE = v.price[2][i+1] - v.F0;
            E_2 = pow((v.F0 + v.price[2][i+1]) / 2, 2);
            double c = (v.price[0][i] + v.price[0][i + 1]) / 2;
            c = (c + v.price[0][i + 1]) / 2;
            sum = sum + (c / E_2) * deltaE;
        }
        else{
            double deltaE = v.price[2][i + 1] - v.price[2][i];
            double E_2 = pow((v.price[2][i + 1] + v.price[2][i]) / 2, 2);
            double c = (v.price[0][i] + v.price[0][i + 1]) / 2;
            sum = sum + (c / E_2) * deltaE;
        }
    }
    sum = 2 * sum * pow(M_E, r*T) / T;
    double a = pow(sum, 0.5);
    cout << a << endl;
}