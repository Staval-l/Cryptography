#include <iostream>
#include <bits/stdc++.h>
#include <random>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using boost::multiprecision::cpp_int;


void Read_Data(vector<int>& arr, int size, const string& str) {
    arr.resize(size);

    ifstream data;
    data.open(str);

    if(data.is_open()) {
        for(int & i : arr) {
                data >> i;
        }
    }

    data.close();
}


bool Is_Prime(cpp_int n, vector<int>& arr) {
    if (n == 1 || n == 0) return false;

    for(int & i : arr) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}


unsigned long long Generate_Number(vector<int>& arr) {
    unsigned long long N = 0;

    while (true) {
        std::random_device rd;
        std::mt19937_64 gen(rd());

        std::uniform_int_distribution<unsigned long long> dis;

        N = dis(gen);

        string Num = to_string(N);
        Num[0] = '1';
        Num[Num.size() - 1] = '1';
        N = stoull(Num);

        if (Is_Prime(N, arr)) {
            cout << N << endl;
            return N;
        }
    }
}


cpp_int GCD(cpp_int x, cpp_int y) {
    cpp_int g;
    g = y;
    while (x > 0) {
        g = x;
        x = y % x;
        y = g;
    }

    return g;
}


cpp_int Pow_Mod(cpp_int base, cpp_int exponent, cpp_int mod) {
    cpp_int x (1);
    cpp_int y (base);
    while (exponent > 0) {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}


bool Ferma_Test(cpp_int N, int iterations) {
    for (int i = 0; i < iterations; ++i) {
        cpp_int a (rand() % N + 1);
        cpp_int nod = GCD(a, N);
        if (nod != 1)
            return false;

        a = Pow_Mod(a, N-1, N);
        if (a != 1)
            return false;
    }
    return true;
}


int main() {
    srand(time(nullptr));
    vector<int> arr;
    Read_Data(arr, 303, R"(C:\Users\Staval\CLionProjects\Cryptography\Lab_3\Simple_nums.txt)");

    string Num = "237872255594258043774847393226284347433624176637030230451693327943175528879072338325687937350075597933223667720801775719974288065664806498607970502309626485355936095165568224879163374199768959376376195753658195140051275782298822604303145423104616773980711963067501960023289349641123537747609039016523";
    boost::multiprecision::cpp_int n(Num);

    cpp_int N (6609719587371582529);

    bool f = Is_Prime(n, arr);

    if (!f) {
        cout << "Not a prime number" << endl;
        return 0;
    }

    f = Ferma_Test(n, 5);

    if (!f) {
        cout << "Not a prime number" << endl;
        return 0;
    }
    else {
        cout << "A prime number" << endl;
    }

    return 0;
}
