function solution(nums) {
    var answer = 0;
    let dictionary = {};
    for (let i=0; i<nums.length; i++) {
        if (!dictionary[nums[i]]) {
            dictionary[nums[i]] = true;
        }
        if (Object.keys(dictionary).length===nums.length/2) {
            break;
        }
    }
    answer = Object.keys(dictionary).length;
    return answer;
}