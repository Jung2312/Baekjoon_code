#include <bits/stdc++.h>
using namespace std;

string str;
int cnt[26]; // 알파벳

int main(){
    ios_base::sync_with_stdio(false); // 동기화를 비활성화
    
    // cin과 cout의 묶음을 풀어
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> str;

    // == cnt[c - 97]++, a = 0, b = 1, c = 2...
    for(char c : str)  cnt[c - 'a']++; // 배열의 값이 증가

    for (int i = 0; i < 26; i++) cout << cnt[i] << " ";
    
    return 0;
}