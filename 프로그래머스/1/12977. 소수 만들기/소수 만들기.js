function solution(nums) {
    var answer = 0;
    let eratos = Array.from(new Array(3000),() => true);
    for (let i=2; i<eratos.length; i++) {
        if (eratos[i]) {
            for (let j=i*2; j<eratos.length; j+=i) {
                eratos[j] = false;
            }
        }
    }
    for (let i=0; i<nums.length-2; i++) {
        for (let j=i+1; j<nums.length-1; j++) {
            for (let k=j+1; k<nums.length; k++) {
                answer += eratos[nums[i]+nums[j]+nums[k]] ? 1 : 0
            }
        }
    }
    
    return answer;
}