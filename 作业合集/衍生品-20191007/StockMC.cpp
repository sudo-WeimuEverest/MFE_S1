#include <iostream>
#include <cmath>
#include <random>
#include <fstream>
using namespace std;

//运用Box-Muller方法生成正态分布的随机数
double GetOneGaussianByBoxMuller()
{
	double result;

	double x;
	double y;

	double sizeSquared;
	do
	{
		x = 2.0 * rand() / static_cast<double>(RAND_MAX) - 1;
		y = 2.0 * rand() / static_cast<double>(RAND_MAX) - 1;
		sizeSquared = x * x + y * y;
	} while
		(sizeSquared >= 1.0);
	result = x * sqrt(-2 * log(sizeSquared) / sizeSquared);

	return result;
}

//Monte Carlo模拟生成股价路径
double StockMC(
    double Spot,
    double Expiry,
    double Mu,
    double Sigma,
    unsigned long NumberOfPaths){
    
    double dt = 1/Expiry; //定义时间间隔
    double drift = Mu * dt; //初始化漂移项； 
    double shock;
    
    char filename[1314];//初始化列表
    for(unsigned long number = 1; number <= NumberOfPaths; number++){
        double price = Spot; //每条路径初始价格统一
        srand(number); //每次生成随机数使用不同的种子

        sprintf(filename,"C:\\Users\\Lenovo\\Desktop\\price\\%ld.txt",number); //实现数字与字符的转换
        ofstream fout(filename); //数据分路径储存在txt文件中
        for (unsigned long i = 0; i <= Expiry; i++){
            fout << price << endl;
            
            double thisGaussian = GetOneGaussianByBoxMuller(); //使用BoxMuller算法生成N（0，1）的随机数
            shock = Mu * dt +  Sigma * Sigma * dt *  thisGaussian; //定义随机扰动项
            price = price + price * (shock + drift); //生成价格序列
        }
        fout.close();
    } 
    return 0;
}


int main(){
    double Spot;
    double Expiry;
    double Mu;
    double Sigma;
    unsigned long NumberOfPaths;
    
	cout << "\nEnter spot\n";
	cin >> Spot;

    cout << "\nEnter expiry\n";
	cin >> Expiry;
	
    cout << "\nEnter Mu\n";
	cin >> Mu;

    cout << "\nEnter Sigma\n";
	cin >> Sigma;

	cout << "\nNumber of paths\n";
	cin >> NumberOfPaths;
    
    StockMC(
        Spot,
        Expiry,
        Mu,
        Sigma,
        NumberOfPaths);
} 