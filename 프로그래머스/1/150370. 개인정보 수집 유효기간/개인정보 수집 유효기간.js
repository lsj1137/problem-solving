function calDate(date, plus) {
    let [year, month, day] = date.split('.').map((v)=>parseInt(v));
    month += plus;
    while (month>12) {
        year += 1;
        month -= 12;
    }
    return `${year}.${month.toString().padStart(2,'0')}.${day.toString().padStart(2,'0')}`;
}

function solution(today, terms, privacies) {
    var answer = [];
    let term = {};
    for (t of terms) {
        [k, v] = t.split(' ');
        term[k] = parseInt(v);
    }
    for (p in privacies) {
        let [contractDate, type] = privacies[p].split(' ');
        let expireDate = calDate(contractDate, term[type]);
        if (expireDate<=today) {
            answer.push(parseInt(p)+1);
        }
    }
    return answer;
}