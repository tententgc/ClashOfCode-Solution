#include <bits/stdc++.h>
using namespace std;
main()
{
    int n, m, l, k, c, sum = 0, a;
    cin >> n >> m >> l >> k >> c;

    for (int j = 0; j < m * n; j++)
    {
        cin >> a;
        sum += a;
    }

    sum += l * c * k;

    cout << sum / c + (sum % c == 0 ? 0 : 1);
}
