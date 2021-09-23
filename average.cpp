#include <iostream>

int main() {

    int a = 1;
    int a1 = 1;
    int num;
    int x = 0;

    std::cout << "amount of nums";
    std::cin >> a;
    a1 = a *1;
    std::cout << a1;
 

    while (a > 0)
    {
        std::cin >> num;
        x = x + num;
        a--;
    }
    x = x / a1;
    std::cout << x << std::endl;

    return 0;
}
