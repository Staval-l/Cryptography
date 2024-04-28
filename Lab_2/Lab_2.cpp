#include <iostream> 
#include <vector>
#include <bitset>
#include <fstream>


using namespace std;


void LFSR_1(bitset<8> &input)
{
	//x^5 + x^2 + 1 
	bool XOR = input[5] ^ input[2] ^ input[0];
	bool res = input[7];
	input <<= 1;
	input[0] = XOR;
}

void LFSR_2(bitset<8>& input) {
	//x^5 + x^4 + x^3 + x^2 + 1 
	bool XOR = input[5] ^ input[4] ^ input[3] ^ input[2] ^ input[0];
	bool res = input[7];
	input <<= 1;
	input[0] = XOR;
}


vector<bool> generate_sequence(bitset<8>& x1, bitset<8>& x2, size_t n) {
	vector<bool> result;
	while (result.size() < n) {
		LFSR_1(x1);
		LFSR_2(x2);
		for (int i = 0; i < x2.size(); i++) {
			if (x2[i] == 1) {
				result.push_back(x1[i]);
			}
		}
	}
	return result;
	
}

void write_sequence(vector<bool> sequence, size_t n) {
	ofstream out("1.txt");
	if (out.is_open())
	{
		for (int i = 0; i < n; i++) {
			out << sequence[i];
		}
	}
	out.close();
}


int main(){
	size_t n = 1000000;
	bitset <8> x1 = 123;
	bitset <8> x2 = 212;
	bitset <8> x3 = 52;
	vector<bool> sequence = generate_sequence(x1,x2, n);
	write_sequence(sequence, n);
	return 0;
}