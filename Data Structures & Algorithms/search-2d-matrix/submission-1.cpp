class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int nrows = matrix.size();
        int ncols = matrix.at(0).size();
        int size = nrows* ncols;
        int l = 0;
        int r = size-1;
        while (l <= r){
            int mid = l + (r-l)/2;
            int curr = matrix.at(mid / ncols).at(mid % ncols);
            if (target > curr) l = mid+1;
            else if (target < curr) r = mid-1;
            else return true;
        }
        return false;
    }
};
