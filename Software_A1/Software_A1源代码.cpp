#include <iostream>
using namespace std;
class Rational
{
private:
	int numerator;//分子
	int denominator;//分母
	int gcd(int a, int b)//求最大公约数，辗转相除
	{
		a = abs(a);
		b = abs(b);
		while (b != 0)
		{
			int temp = a%b;
			a = b;
			b = temp;
		}
		return a;
	}
	void standard()//约分函数
	{
		if (denominator == 0)
		{
			cout << "false";
			exit(1);
		}
		int GCD = gcd(numerator, denominator);
		numerator /= GCD;
		denominator /= GCD;
		if (denominator < 0)//符号给分子
		{
			numerator = -numerator;
			denominator = -denominator;
		}
	}
public://函数重载*
	Rational():numerator(0),denominator(1){}//默认0/1
	Rational(int num) :numerator(num), denominator(1) //num/1
	{
		standard();
	}
	Rational(int num,int den) :numerator(num), denominator(den) //num/den
	{
		standard();
	}
	Rational operator+(Rational& r)//加法
	{
		int NUM = numerator * r.denominator + r.numerator * denominator;
		int DEN = denominator * r.denominator;
		return Rational(NUM, DEN);
	}
	Rational operator-(Rational& r)//减法
	{
		int NUM = numerator * r.denominator - r.numerator * denominator;
		int DEN = denominator * r.denominator;
		return Rational(NUM, DEN);
	}
	Rational operator*(Rational& r)//乘法
	{
		int NUM = numerator * r.numerator;
		int DEN = denominator * r.denominator;
		return Rational(NUM, DEN);
	}
	Rational operator/(Rational& r)//除法
	{
		int NUM = numerator * r.denominator;
		int DEN = denominator * r.numerator;
		return Rational(NUM, DEN);
	}
	void show()//输出函数
	{
		if (denominator == 1)
		{
			cout << numerator;
		}
		else
		{
			cout << numerator << "/" << denominator;
		}
	}
	friend ostream& operator<<(ostream& os, const Rational& r)//友元函数*
	{
		if (r.denominator == 1)
		{
			os << r.numerator;
		}
		else
		{
			os << r.numerator << "/" << r.denominator;
		}
		return os;
	}

};
int main()
{
	Rational r1;
	Rational r2(4);
	Rational r3(6,-9);
	Rational r4(1, -3);
	cout << r1 << endl;
	cout << r2 << endl;
	cout << r3 << endl;
	cout << r3 + r4 << endl;
	cout << r3 - r4 << endl;
	cout << r3 * r4 << endl;
	cout << r3 / r4 << endl;
}