#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, num;
    vector<int> ar(100);
    
    cin >> n;
    vector<int> helpInt(n);
    vector<string> helpStr(n);
    
    for(int i=0; i<n; i++)
    {
        string s;
        cin >> num;
        cin >> s;
        if(i >= n/2)
            helpStr[i] = s;
        else
            helpStr[i] = "-";
        helpInt[i] = num;
        ar[num]++;
    }
    
    int oldCount, total = 0;
    for(int i=0; i<n; i++)
    {
        oldCount = ar[i];
        ar[i] = total;
        total += oldCount;
    }
    
    vector<string> output(n);
    for(int i=0; i<n; i++)
    {
        output[ar[helpInt[i]]] = helpStr[i];
        ar[helpInt[i]]++;
    }
    
    string outString = output[0];
    for(int i=1; i<n; i++)
    {
        outString = outString + " " + output[i];
    }
    cout << outString << endl;
    
    return 0;
}
