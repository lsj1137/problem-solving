function priceCombi(priceList) {
    let price = priceList[0];
    if (priceList.length===1) {
        return [[[price*9/10, 10]], [[price*8/10, 20]], [[price*7/10, 30]], [[price*6/10, 40]]];
    }
    let result = [];
    let rest = priceList.slice(1);
    let saleRate = 9;
    for (let i=0; i<4; i++) {
        priceCombi(rest).map((combi)=>{
            result.push([[price*saleRate/10, (10-saleRate)*10], ...combi])
        })
        saleRate -= 1;
    }
    return result;
}

function buyEmo(user, priceList) {
    let [saleStd, totalStd] = user;
    let [join, total] = [0,0];
    for (price of priceList) {
        if (price[1]>=saleStd) {
            total += price[0];
        }
    }
    if (total>=totalStd) {
        total = 0;
        join += 1;
    }
    return [join, total];
}

function solution(users, emoticons) {
    var answer = [];
    let possiblePrices = priceCombi(emoticons);
    let [join, total] = [0,0];
    for (prices of possiblePrices) {
        let [tempJoin, tempTotal] = [0,0];
        for (user of users) {
            let [j, t] = buyEmo(user, prices);
            tempJoin += j;
            tempTotal += t;
        }
        if (tempJoin>join) {
            join = tempJoin;
            total = tempTotal;
        } else if (tempJoin===join && tempTotal>total) {
            total = tempTotal;
        }
    }
    answer = [join, total];
    return answer;
}