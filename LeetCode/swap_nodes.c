// Submission Link : https://leetcode.com/submissions/detail/230112144/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* swapPairs(struct ListNode* head){

        struct ListNode *tmp;
    tmp = head;
    
    while(tmp!= NULL && tmp->next!=NULL){
        int p = tmp->next->val;
        tmp->next->val = tmp->val;
        tmp->val = p;
        
        if (tmp->next->next != NULL)
            tmp = tmp->next->next;
        else
            break;
        
    }
    
    return head;
}

