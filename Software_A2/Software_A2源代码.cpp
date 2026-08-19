#include<iostream>
#include<cmath>
using namespace std;
const double P = 3.14;

class Shape {
public:
	virtual void area() = 0;//纯虚面积函数
	virtual void perimeter() = 0;//纯虚周长函数
	virtual ~Shape(){}//虚析构*，避免内存泄露
};

class Circle :public Shape {//派生类圆形
private:
	double r;
public:
	Circle(double r) :r(r) {};//构造函数定义
	void area()override {
		double s = P * r * r;
		cout << "area:"<<s<<endl;
	}
	void perimeter()override {
		double c = 2 * P * r;
		cout << "perimeter:"<<c<<endl;
	}
};

class Rectangle :public Shape {//派生类矩形
private:
	double a, b;
public:
	Rectangle(double a, double b) :a(a), b(b) {};
	void area()override {
		double s = a * b;
		cout << "area:"<<s<<endl;
	}
	void perimeter()override {
		double c = 2 * (a + b);
		cout << "perimeter:"<<c<<endl;
	}
};

class Triangle :public Shape {//派生类三角形
private:
	double a, b, d;
public:
	Triangle(double a, double b, double d) :a(a), b(b), d(d) {};
	void area()override {
		double p = (a + b + d) / 2;
		double s = sqrt(p * (p - a) * (p - b) * (p - d));
		cout << "area:"<<s<<endl;
	}
	void perimeter()override {
		double c = a + b + d;
		cout << "perimeter:"<<c<<endl;
	}
};

int main()
{
	Shape* s1 = new Circle(3);
	Shape* s2 = new Rectangle(3, 4);
	Shape* s3 = new Triangle(3, 4, 5);
	s1->area();
	s1->perimeter();
	s2->area();
	s2->perimeter();
	s3->area();
	s3->perimeter();
	delete s1;
	delete s2;
	delete s3;
	return 0;
}