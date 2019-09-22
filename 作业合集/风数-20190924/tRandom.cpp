//生成t(n)分布的随机数
#include <iostream>
#include <random>
#include <cmath>
#include <fstream>
#include<time.h>
using namespace std;
double pi = 3.1415926897932384;

//生成Chi_Square(n)分布的随机数
double Chisquare(int n) {
	double z = 0;
	for (int i = 1; i <= n; i++) {
		double u1 = rand() % RAND_MAX / (double)RAND_MAX; 
		double u2 = rand() % RAND_MAX / (double)RAND_MAX;
		double y = sqrt(-2 * log(u1)) * (cos(2 * pi * u2));//y为标准正态分布的随机数
		z += y * y; //运算得到chi_Square（n）分布随机数
	}
	return z;
}

int main() {
	int n;
	cout << "The degree of t distribution is ：" << endl;
	cin >> n;
	ofstream fout("C:\\Users\\Lenovo\\Desktop\\tRandom.txt");

	for (int i = 1; i <= 10000; ++i) {
		double u1, u2, x;
		srand(i); // 每次设置不同的随机数seed

		//使用Box-Muller变换生成正态分布随机数
		u1 = rand() % RAND_MAX / (double)RAND_MAX; //生成（0，1）的随机数
		u2 = rand() % RAND_MAX / (double)RAND_MAX;
		x = sqrt(-2 * log(u1)) * sin(2 * pi * u2); //x为标准正态分布的随机数

		double z = Chisquare(n);
		double t = x / sqrt(z / n);

		//如果结果是inf或者nan就再进行一遍
		if (isinf(t) || isnan(t)) {
			i--;
			continue;
		}
		fout << t << endl;//将生成的随机数储存到文件内，以备检验
	}
	fout.close();
}