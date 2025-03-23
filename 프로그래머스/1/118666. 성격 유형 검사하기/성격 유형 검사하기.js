function solution(survey, choices) {
    var answer = '';
    let types = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0};
    for (let i=0; i<survey.length; i++) {
        switch (choices[i]) {
            case 1:
                types[survey[i][0]] += 3;
                break;
            case 2:
                types[survey[i][0]] += 2;
                break;
            case 3:
                types[survey[i][0]] += 1;
                break;
            case 4:
                break;
            case 5:
                types[survey[i][1]] += 1;
                break;
            case 6:
                types[survey[i][1]] += 2;
                break;
            case 7:
                types[survey[i][1]] += 3;
                break;       
        }
    }
    
    answer += types['R'] >= types['T'] ? 'R' : 'T';
    answer += types['C'] >= types['F'] ? 'C' : 'F';
    answer += types['J'] >= types['M'] ? 'J' : 'M';
    answer += types['A'] >= types['N'] ? 'A' : 'N';
    
    return answer;
}