/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int len = 0;
        ListNode* tmp = head;
        while(tmp != nullptr){
            len++;
            tmp = tmp->next;
        }
        if(len == n) return head->next;
        ListNode* prev = nullptr;
        tmp = head;
        for(int i=0; i < len-n; i++){
            prev = tmp;
            tmp = tmp->next;
        }
        prev->next = tmp->next;
        return head;

    }
};
