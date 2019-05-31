// Submission Link : https://leetcode.com/submissions/detail/230806029/


void swap(int *x, int *y){
    
    int t = *x;
    *x = *y;
    *y = t;
    
}

int findKthLargest(int* nums, int numsSize, int k){
    
    
    int swaps = 0;
    int current_swaps;
    
    while(1){     
        current_swaps = swaps;
        for(int i = 0; i< numsSize-1; i++){
            
            if (nums[i] > nums[i+1]){
                
                swap(&nums[i], &nums[i+1]);
                swaps += 1;
                
            }
           
          
            
        }
        
        if(swaps == current_swaps)
            break;
}
    
   
    return nums[numsSize-k];
    
}

