#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    int firstDiagonal=0;
    int secondDiagonal=0;

    cin >> n;
    int count=n-1;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }

    for(int i=0; i<n; i++)
    { 
        firstDiagonal+=a.at(i).at(i);
        secondDiagonal+=a.at(count).at(i);
        count--;
    }

    cout << abs(firstDiagonal-secondDiagonal);

    return 0;
}
