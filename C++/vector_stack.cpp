# include <iostream>
# include <vector>
# include <algorithm>
# include <stack>
using namespace std;
// Template function to return maximum of two values
// template <typename A, typename B> entity_definition
template <typename T> T myMax(T x, T y){
    return (x > y) ? x : y;
}
// Defining class template
template <typename T> class Geek{
    public: 
    T x;
    T y;
    // Constructure 
    Geek (T val1, T val2) : x(val1), y(val2){} // initialize x with val1, y with val2
    void getValues(){cout << x << " " << y}; // Create x and set it to val1
};
// Define multiple typename
template <typename T1, typename T2, typename T3> class Geeks{
    public:
        T1 x; T2 y; T3 z;
    Geeks(T1 val1, T2 val2, T3 val3) : x(val1), y(val2), z(val3){}
    void getValues(){cout << x <<" " << y << " " << z;}
};
// FUNTION TEMPLATE ARGUMENTS DEDUCTION
// Declare right out side the template
template <typename t> t multiply(t first, t second){return first * second;}
// We can pass more than one datatype as arguments to templates
int main(){
    // Declare an empty vector
    vector<int> v1;
    // Declares vectir with given size and fills it with a value
    vector <int> v2(3, 5); // -> 5 5 5
    for (int x : v2) {
        cout << x << " ";
    }
    vector <int> v3 = {1, 2, 3}; // -> 1 2 3
    for (int x : v3) {
        cout << x << " ";
    }
    vector <char> v = {'a', 'f', 'd'};
    v.push_back('z');
    v.insert(v.begin() + 1, 'c'); // point the pointer to begin + 1
    vector<vector<int>> matrix = {{1, 2, 3},{2, 3, 4},{3, 4, 5}};
    myMax<int>(3, 7);
    // Declare data type and name
    Geek<int> intGeek(10, 20);
    Geek<double> doubleGeek(3.14, 6.28);
    // Access the templates values
    intGeek.getValues();
    Geeks<int, double, string> intDoubleStringGeeks(10, 3.4, "Hello");
    // STACKKKKK
    stack<int> st;
    st.push(10); st.push(5); // -> (10, 5)
    // Accessing element 
    st.top();
    if (st.empty()){cout << "Stack is empty" << endl;} // Stack_size: st.size()
    return 0;
}