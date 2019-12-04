// codeforces 1204B - 59154860
// human solve time: 582s
#include <bits/stdc++.h>
using namespace std;

const int N = 1234;

int a[N], b[N];
int n, l, r;    

int main() {
  scanf("%d %d %d", &n, &l, &r);
  for (int i = 0; i < n; i++)
    a[i] = b[i] = 1;
  int mt = 2;
  for (int i = 0; i < l - 1; i++) {
    a[i] = mt;
    mt *= 2;
  }
  mt = 2;
  for (int i = 0; i < r - 1; i++) {
    b[i] = mt;
    mt *= 2;
  }
  if (r - 2 >= 0)
    for (int i = r - 1; i < n - 1; i++)
      b[i] = a[r - 2];
  int x = accumulate(a, a + n, 0);
  int y = accumulate(b, b + n, 0);
  printf("%d %d\n", x, y);
  return 0;
}
