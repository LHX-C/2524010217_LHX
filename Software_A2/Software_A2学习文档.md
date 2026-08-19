# Software_A2图形类体系设计
## 一、学习过程
1. 根据题目要求，需要完成图形类体系，基类 Shape 为抽象类，派生 Circle 圆形、Rectangle 矩形、Triangle 三角形，实现面积、周长计算并展示动态绑定。
2. 先搭建基类 Shape 框架，定义纯虚函数area()、perimeter()，使基类成为抽象类；同时添加虚析构函数，防止基类指针释放派生类对象出现内存问题。
3. 编写三个派生类，公有继承 Shape，声明私有成员保存图形参数，声明构造函数，重写area()与perimeter()虚函数。
4. 编写完成后编译代码，出现编译报错：构造函数只做声明，没有实现。补全构造函数，使用初始化列表完成成员变量初始化。
5. 运行程序发现三角形周长计算结果错误，排查后发现局部变量和类的成员变量重名，发生名字遮蔽，修改局部变量名称修复逻辑错误。
6. 在 main 函数中使用基类指针指向不同派生类对象，调用对应方法，验证动态绑定效果；使用 delete 释放堆上对象。
7. 测试各个图形面积周长输出，核对计算结果，完成程序调试。
-------------------------------------------------------------------------------------
## 二、关键知识点总结
1. 抽象类与纯虚函数
使用virtual void area() = 0;定义纯虚函数，包含纯虚函数的类是抽象类。抽象类不能实例化对象，派生类必须重写全部纯虚函数，否则派生类依旧是抽象类。
2. 虚析构函数
基类含有虚函数时，需要定义虚析构virtual ~Shape(){};，使用基类指针 new 派生类对象 delete 释放时，可以正确调用派生类析构函数，避免内存泄漏。
3. 初始化列表
构造函数可以使用初始化列表Circle(double r):r(r){}，在对象创建时直接给成员变量赋值。
4.继承与 override 重写
派生类使用public公有继承基类；override关键字显式标记重写虚函数，编译时检查函数签名是否匹配。
5. 动态绑定（多态）
满足三个条件：公有继承、重写虚函数、基类指针指向派生类对象。运行时根据指针实际对象类型调用对应类的函数。
-------------------------------------------------------------------------------------
## 三、踩坑记录
1. 构造函数只声明，没有实现
现象：编译报错，构造函数只有声明没有函数体。
原因：类内只写Circle(double r);声明，没有写构造函数实现。
解决：在类内部完成构造函数实现，使用初始化列表对成员赋值。
2. 局部变量与成员变量同名，名字遮蔽
现象：三角形周长计算结果异常。
原因：周长函数内定义double c = a + b + c;，局部变量 c 屏蔽类的私有成员 c，等式右边的 c 是刚定义的局部变量，不是三角形的边长。
解决：更换局部变量名字，不和成员变量重名。
3. 忘记虚析构函数
现象：程序可运行，但基类指针 delete 派生类对象，派生类析构不会执行，存在内存隐患。
解决：基类添加虚析构函数virtual ~Shape(){};。
-------------------------------------------------------------------------------------
## 四、代码
'''cpp
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
'''