// Submission Link :    https://leetcode.com/submissions/detail/230099283/




void rotate(int* nums, int numsSize, int k){
    
    int p[numsSize];
    
    for(int i = 0; i< k; i++){
        p[i] = nums[numsSize-k+i];
    }
    
    for(int j = k; j<numsSize; j++){
        
        p[j] = nums[j-k];
    }
    
    for(int i = 0; i< numsSize; i++){
        nums[i] = p[i];
    }
}



