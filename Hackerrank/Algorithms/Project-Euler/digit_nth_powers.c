// Problem Statement : https://www.hackerrank.com/contests/projecteuler/challenges/euler030

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
int p;
    scanf("%d",&p);
   int i,a,b,c,d,e,f,n,sum;
  double number;
  sum =0;
  
  for (i=10;i<100;i++){
    a = i%10;
    b = i/10;
    number=pow(a,p)+pow(b,p);
    if ((int)number==i)
      sum+=(int)number;
  }

  for (i=100;i<1000;i++){
    n=i;
    a = n%10;
    n /= 10;
    b = n%10;
    n /= 10;
    c = n;
    number=pow(a,p)+pow(b,p)+pow(c,p);
    if ((int)number==i)
      sum+=(int)number;
  }

  for (i=1000;i<10000;i++){
    n=i;
    a = n % 10;
    n /= 10;
    b = n % 10;
    n /= 10;
    c = n % 10;
    n /= 10;
    d = n % 10;    
    number=pow(a,p)+pow(b,p)+pow(c,p)+pow(d,p);    
    if ((int)number==i)
      sum+=(int)number;
  }

  for (i=10000;i<100000;i++){
    n=i;
    a = n%10;
    n /= 10;
    b = n%10;
    n /= 10;
    c = n%10;
    n /= 10;
    d = n%10;
    n /= 10;
    e = n;
    number=pow(a,p)+pow(b,p)+pow(c,p)+pow(d,p)+pow(e,p);
    if ((int)number==i)
      sum+=(int)number;
  }

  for (i=100000;i<1000000;i++){
    n=i;
    a = n%10;
    n /= 10;
    b = n%10;
    n /= 10;
    c = n%10;
    n /= 10;
    d = n%10;
    n /= 10;
    e = n%10;
    n/=10;
    f=n;
    number=pow(a,p)+pow(b,p)+pow(c,p)+pow(d,p)+pow(e,p)+pow(f,p);
    if ((int)number==i)
      sum+=(int)number;
  }
  
  printf("%d\n",sum);  
  
return 0;
}
