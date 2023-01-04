#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); // 동기화를 비활성화
    
    // cin과 cout의 묶음을 풀어
    cin.tie(NULL);
    cout.tie(NULL);

    int a[9];
    
    
    // 입력
    for(int i = 0; i < 9; i++)
    {
        cin >> a[i];
    }

    sort(a, a + 9); // 오름차순 정렬

    // 순열
    do{
        int sum = 0;

        // 7개만 잘라서 합을 구함
        for(int j = 0; j < 7; j++)
        {
            sum += a[j];
        }

        if(sum == 100)
        {
            break;
        }
        
    }while(next_permutation(a, a + 9));

    // 출력
    for(int i = 0; i < 7; i++)
    {
        cout << a[i] << "\n";
    }

    return 0;
}
