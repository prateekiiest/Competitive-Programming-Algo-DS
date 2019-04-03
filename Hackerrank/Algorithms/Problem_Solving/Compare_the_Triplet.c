
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int a0; 
    int a1; 
    int a2; 
    scanf("%d %d %d",&a0,&a1,&a2);
    int b0; 
    int b1; 
    int b2; 
    scanf("%d %d %d",&b0,&b1,&b2);
    int count_a, count_b;
    count_a =0;
    count_b =0;
    if(a0>b0)
        count_a++;
    if(a1>b1)
        count_a++;
    
    if(a2>b2)
        count_a++;
    
    
    
    if(b0>a0)
        count_b++;
    if(b1>a1)
        count_b++;
    
    if(b2>a2)
        count_b++;
    
    printf("%d %d",count_a,count_b);
    
    return 0;
}
