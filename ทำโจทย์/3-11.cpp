#include<bits/stdc++.h>
#define vec vector
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);
    string num ; cin >> num;
    int mod_3 = 0 , mod_11 = 0;
    for(int i = 0 ; i < num.size() ; i++ ){
        mod_3 += (num[i] - '0') % 3;
    }
    mod_3 %= 3;
    reverse(num.begin(),num.end());
    for(int i = 0 ; i < num.size() ; i++){
        if(i % 2 == 0){
            mod_11 += num[i] - '0';
        }
        else{
            mod_11 += 11 - (num[i] - '0');
        }
    }
    mod_11 %= 11;
    cout << mod_3 << " " << mod_11;
    return 0;
}