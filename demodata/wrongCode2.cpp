// codeforces 1204B - 59150167
// human solve time: 252s
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<ctime>
#define up(i,x,y) for(int i = x;i <= y;i ++)
#define down(i,x,y) for(int i = x;i >= y;i --)
#define mem(a,b) memset((a),(b),sizeof(a))
#define mod(x) ((x)%MOD)
#define lson p<<1
#define rson p<<1|1
using namespace std;
typedef long long ll;
const int SIZE = 500010;
const int INF = 2147483640;
const double eps = 1e-8;

inline void RD(int &x)
{
    x = 0;  char c; c = getchar();
    bool flag = 0;
    if(c == '-')    flag = 1;
    while(c < '0' || c > '9')   {if(c == '-')   {flag = 1;} c = getchar();}
    while(c >= '0' && c <= '9') x = (x << 1) + (x << 3) + c - '0',c = getchar();
}

ll sum1,sum2;
ll n,l,r;

int main(int argc, char const *argv[])
{
	scanf("%lld%lld%lld",&n,&l,&r);
	sum1 = (1ll << l) - 1ll + (ll)(n - l);
	sum2 = (1ll << r) - 1ll + (1ll << (l-1ll))*(ll)(n-r);
	printf("%lld %lld\n",sum1,sum2);
	return 0;
}
