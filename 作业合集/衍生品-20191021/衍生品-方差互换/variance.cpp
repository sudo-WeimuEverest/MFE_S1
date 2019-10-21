#include<iostream>
#include<cmath>
#include<fstream>
#include<sstream>
#include<vector>
#include<string>
#include<cassert>
using namespace std;

#define R 0.02651 // 使用对应的一年期国债利率2.651
#define S 3.059 //数据导出时对应的上证50ETF价格
#define T 36.0/365.0  //11月合约的到期日
#define e 2.718281828459045 //自然底数
#define N 11 //价格数据的条数

void txt_to_vectordouble(vector<vector<double>>& res, string pathname)
{
	ifstream infile;
	infile.open(pathname.data());   //将文件流对象与文件连接起来 
	assert(infile.is_open());   //若失败,则输出错误消息,并终止程序运行 
	vector<double> num;
	string s;
	while (getline(infile, s)) {
		istringstream is(s); //将读出的一行转成数据流进行操作
		double d;
		while (!is.eof()) {
			is >> d;
			num.push_back(d);
		}
		res.push_back(num);
		num.clear();
		s.clear();
	}
	infile.close();  
}

int main (){
    double F = S*pow(e,R*T); //简易思路求得远期价格
    //输入看涨期权、看跌期权以及行权价
    /*vector<string> call, put, K;
    string line;
    int linenum = 0;
    ifstream infile("V-Nov.txt");
    while(getline(infile,line)){
        switch (linenum){
            case 0: call.push_back(line);break;
            case 1: put.push_back(line);break;
            case 2: K.push_back(line);break;
        }
        linenum++;
    }
    infile.close();
    cout << K[1] <<endl;
    vector<vector<double>> data;
    txt_to_vectordouble(data,"V-Nov.txt");
    for (auto a : data) {
		for (auto b : a) {
			cout << b << " ";
		}
		cout << endl;
	}*/

    

    

    vector<double> call{0.311,0.2606,0.2142,0.1689,0.1278,0.0929,0.042,0.015,0.0054,0.0022,0.0013};
    vector<double> put{0.002,0.0032,0.0056,0.0105,0.0193,0.0334,0.0819,0.1557,0.2457,0.3419,0.4409};
    vector<double> K{2.75,2.8,2.85,2.9,2.95,3,3.1,3.2,3.3,3.4,3.5};
    //找到K0,即小于F且最接近的执行价格
    int min = abs(call[0]-F);
    int r =0;
    for(int i =0; i< N; ++i){
        if ( abs(i - F) < min){
            min = abs(call[i]-F);
            r = i;
        }
    }
    double K0 = K[r];
    //求表达式中和式的值
    double sum = 0;
    for(int i =0;i < N;++i){
        double P = 0; //对应表达式中的P（Ki）
        double Delta =0;
        if (K[i]< K0){
            P = call[i];
        }
        else if (K[i]> K0){
            P = put[i];
        }
        else{
            P = (put[i]+call[i])/2;
        }
        if (i=0){
            Delta = K[1] - K[0];
        }
        else if (i=N-1){
            Delta = K[N-1] - K[N-2];
        }
        else{
            Delta = 0.5*(K[i+1]-K[i-1]);
        }
        sum += (Delta/K[i]*K[i])*pow(e,R*T)*P;
    }
    double variance = (2 /double(T))*sum;
    cout << variance <<endl;
}