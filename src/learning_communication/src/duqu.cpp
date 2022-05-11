#include<fstream>

#include<iostream>

using namespace std;

int main()

{


   ifstream fin("1.txt");

   float temp[12] = {0.0};
   float *p = &temp[0];
   for(int i = 0;i<12;i++) 
   {fin>>*p;           
    p++;}   
cout << temp[2]<< endl;

   fin .close();

   return 0;

}
