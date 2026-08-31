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
    void reorderList(ListNode* head) {
        if(!head || !head->next) return;
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* curr = slow->next;
        ListNode* prev = slow->next = nullptr;
        while (curr != nullptr){
            ListNode* next = curr->next;    
            curr->next = prev;
            prev = curr;
            curr = next;   
        }

        ListNode* list1 = head;
        ListNode* list2 = prev;
        while(list1 || list2){
            ListNode* tmp = list1->next;
            list1->next = list2;
            list1 = list2;
            list2 = tmp;
        }
    
    }
};
