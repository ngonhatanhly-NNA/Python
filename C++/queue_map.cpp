# include <iostream>
# include <queue>
# include <map>
using namespace std;
int main(){
    // FIFO
    queue<int> q; q.push(10); q.push(20); q.pop();
    // Accessing element
    q.front();
    q.back();
    // Map allow searching, insertion, and deletion and take O(logn) time
    // Map automatically avoid duplicate keys
    // Keys are stored in ascending order
    // Compared to unordered_map, the times taken for search, insert, and delete
    // are more in map, but we get items in sorted order and it supports additional 
    // functions like upper_bound() and lower_bound()
    
    // Creating an empty map
    map<int, string> m1;
    // Initialize map with list
    map<int, string> m2 = {{1, "Geeks"}, {2, "For"}, {3, "Geeks"}};
    for (auto& p: m2) // a pair
        cout << p.first << " " << p.second << endl;
    // Accessing element
    cout << m2[1] << endl; cout << m2.at(2) << endl; // pretty similar to dictionary 
    // Updating value
    m2[0] = "Tweaks";
    // Finding element with key 2
    map <int, string> m = {{1, "Geeks"}, {2, "For"}, {3, "Geeks"}};
    auto it = m.find(2); // if not 3, pointer
    if (it != m.end()) cout << it->first << " " << it->second;
    else cout << "Key Not Found";
    return 0;

}