# A1.有理数类设计学习文档
## 一、学习过程
1.编写基础 Rational 有理数类，定义分子、分母私有成员，通过辗转相除求最大公约数，实现初始化分数
2.使用函数重载实现四则运算
3.使用友元函数实现私有成员的访问，从而顺利输出结果

## 二、关键知识点总结
1.函数重载
同一个作用域内，多个函数函数名相同、参数列表不同。运算符重载属于函数重载，能够让运算符支持自定义类对象运算。
2.友元函数
友元函数不属于类成员，在类内通过friend声明。可以直接访问类的私有成员；输出运算符operator<<只能采用全局友元函数形式重载

## 三、代码
'''cpp
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
'''