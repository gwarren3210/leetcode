class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int l = 0;
        int m = 0;
        for (int r = 0; r < s.size(); r++){
            if (charSet.find(s[r]) == charSet.end()){
                m = max(m, r-l+1);
            } else {
                while(charSet.count(s[r])) {
                    charSet.erase(s[l++]);
                }
            }
            charSet.insert(s[r]);
        }
        return m;
    }
};
