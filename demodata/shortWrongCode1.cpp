#include <iostream>

using namespace std;

int main()
{
    int x, y;
    cin >> x >> y;
    int z = x + x;  // "x + x"  should be replaced to "x + y"
    cout << 2 * z << endl;
}