# Submission Link : https://leetcode.com/submissions/detail/230808975/

void swap(int *x, int *y){
    
    int t = *x;
    *x = *y;
    *y = t;
    
}

void moveZeroes(int* nums, int numsSize){
    
    int count_zero = 0;
    for(int i = 0; i<numsSize; i++){
        if (nums[i] == 0)
            count_zero +=1;
    }
    
    while(count_zero)
    {
        for(int i = 0; i<numsSize-1; i++){
        if (nums[i] == 0)
            swap(&nums[i], &nums[i+1]);
            
    }
        count_zero -=1;
    
    }
    

}

