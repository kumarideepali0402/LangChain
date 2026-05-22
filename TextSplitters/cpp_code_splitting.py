from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> num=nums;
        sort(nums.begin(),nums.end());
        int left=0;
        int right =nums.size()-1;
        int l=-1;
        int r=-1;
        while(left<right){
            if (nums[left]+nums[right]==target){
                for(int i=0;i<nums.size();i++){
                    if(num[i]==nums[left] && l==-1) l=i;
                    else if(num[i]==nums[right]) r=i;
                }
                

            return {l,r};
            }
           
        
            else if(nums[left]+nums[right]<target){
                left++;
                
            }
            else right--;
        }
        return{};
    }
};"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.CPP,
    chunk_size = 100,
    chunk_overlap = 0
)

result = splitter.split_text(text)

print(result)
print (len(result))