# include <iostream>
using namespace std;
// Namespace: provide indetifiers for large project without collapse
struct Point{
    private:
        int x, y;   
    // Member function
    public:
    // Constructors, when input Point, input into here, do the code and then detructor
    // Point in this work like a def function -> we can type directly (int, int) without call
        Point (int a, int b){
        x = a;
        y = b;
        }
    // Inner function, since x, y is public, can access to it, local requires extra access
        void show (){
            cout << x << " " << y << endl;
        }
    // Detructor
        ~Point(){cout << "Destroyed Point Variable!!";}

    int sum() {
        return x + y;
    }
}; // like a namespace, but have it own structure
// typedef can be considered as an alias with struct
typedef struct GeeksforGeeks
{
    int x, y;
    // Alias is specified here
} GfG;
// Nested Structure
// we can both call from outside or inside
struct inner{
    int a, b;
};
struct outer{
    inner in;
    int x, y;
};
// union embedded im same memory location
union Student {
    int rollNo;
    float height;
    char firstletter;
};
// enumerate : Small sets of possible values
enum direction {
    EAST, NORTH = 2, WEST, SOUTH // -> return val(if no, when 1 is defined var, the remaining is also automically defined accoridng to its) when access: direction dir = NORTH - > 1
};
// enum class: provide better safety. It helps in resolving name conflicts by providing scope to the constant names.
// It also requires manual typecasting to interger values from names
enum class Day{
    Sunday = 1,
    Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
};
// OOP
class Employee {
    // Instance variables
    private:
        string name;
        float salary;
    public:
        // Constructure
        Employee(string name, float salary) {
            this ->name = name; // Pointer
            this ->salary = salary;
        }// getters method
        string getName() {return name;}
        float getSalary() {return salary;}
        // setters method
        void setName (string name){this ->name = name;}
        void setSalary (float salary) {this -> salary = salary;}
        // Instance method
        void displayDetails() {
            cout << "Employee: " << name << endl;
            cout << "Salary: " << salary << endl;
        }
};
// Polymorphism
class Parent {
    public:
        void func(){cout << "Parent.func()" <<endl;}
        // Polymorphism the other usage
        virtual void fun(int a){cout << "Parent.func(int)"<< a << endl;}
};
class Child: public Parent{
    public:
        void func(int a) {
            cout << "Child.func(int)" << a << endl;
        }
};
// indentifier 
typedef std::string text_t; // can use text_t as identifier
int main(){
    string name = "Hello";
    // for (int i = 0; i < name.size(); i++){
    //     cout << name[i];
    // }
    // cout << endl;
    // cout << "Using range-based for loop: ";
    // for (char ch: name){
    //    cout << ch << endl;        // for char in name
    // }
    // cout << "Traversing using iterator: ";
    // for (auto it = name.begin(); it != name.end(); it ++ ){
    //     cout << *it << endl;        // usinng pointer, it point to name.begin, traverse pointer till reach end -> till the end ends the loop
    // }
    // append element in Python in C++ it is push_back
    name.push_back('!');           // Attention push_back only work with char
    name.pop_back();
    name.insert(3, "C++"); 
    string sub1 = name.substr(6, 5); // substr(starting index, range)
    Point p = {0, 1};
    // Accessing members
   // value already saved in the initializers -> It workds like void, iiner funtion def?
    outer obj = {{1, 2}, 10, 20};
    // Declare a pointer to store the address of the allocated memory
    int *nptr;
    // Allocate and initialize memory
    nptr = new int(6);
    // Allocate block of memory (Array)
    nptr = new int[5]{1, 2, 3, 4, 5};
    // Print array
    for (int i = 0; i < 5; i ++)
        cout << nptr[i] << " ";
    string food[5];
    fill (food, food + 5, "pizza");
    cout << (4 % 2 == 0 ? "Even" : "Odd");
    return 0;
}   