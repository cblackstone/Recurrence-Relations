#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

vector<int> recurrence;

void compute(string confirmation, int an1, int c, int an2, int x, int an3, int d, int an4, int y, int a0, int a1, int n){
	string filename = confirmation + "_results.txt";
	ofstream my_file;
	my_file.open(filename);

	int EvenResult;
	int OddResult;
	
	recurrence.push_back(a0);
	recurrence.push_back(a1);

	my_file << "A0 :\t " << recurrence[0] << "\t" << endl;
	my_file << "A1 :\t " << recurrence[1] << "\t" << endl;

	for(int i = 2; i <= n; ++i){
	
		if( i % 2 == 0 ){
			//Even 
			EvenResult = recurrence[i-an1] + (c * recurrence[i-an1]) + x;  
			recurrence.push_back(EvenResult);
		//	}
		}else if( i % 2 == 1){
			//Odd
			OddResult = recurrence[i-an1] + (d * recurrence[i-an2]) + y;				 			
			recurrence.push_back(OddResult);
		}	
		my_file << "A" << i << " :\t" << recurrence[i] << endl;
			
	}
	my_file.close();	
}

int main(){
//even - a(2n) = a [n-?] + c * 2[n-?] + x
//odd - a(2n-1) = a [n-?] + d * 2[n-?] + y

ifstream fin ("inputs.txt");
string fileline;

//for even

//confirmation number
string confirmation;
fin >> confirmation;


//(first n-?)
string an1_s;
fin >> an1_s;
int an1 = stoi(an1_s);



string c_s;
fin >> c_s;
int c = stoi(c_s);

//second n-?
string an2_s;
fin >> an2_s;
int an2 = stoi(an2_s);

string x_s;
fin >> x_s;
int x = stoi(x_s);

//for odd

//first n-?
string an3_s;
fin >> an3_s;
int an3 = stoi(an3_s);

string d_s;
fin >> d_s;
int d = stoi(d_s);

//second n-?
string an4_s;
fin >> an4_s;
int an4 = stoi(an4_s);

string y_s;
fin >> y_s;
int y = stoi(y_s);


//value of A0
string a0_s; 
fin >> a0_s;
int a0 = stoi(a0_s);

//value of A1
string a1_s; 
fin >> a1_s;

//amount of times run
string n_s;
fin >> n_s;
int n = stoi(n_s);
int a1 = stoi(a1_s);

fin.close();

compute(confirmation,an1, c, an2, x, an3, d, an4, y, a0, a1, n);

return 0;
}	
