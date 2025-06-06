function solution(cap, n, deliveries, pickups) {
    var answer = 0;
    let dPointer = n-1;
    let pPointer = n-1;
    let dTruck = cap;
    let pTruck = cap;
    while (deliveries[dPointer]!==undefined && deliveries[dPointer]===0) {
        dPointer -= 1;
    }
    while (pickups[pPointer]!==undefined && pickups[pPointer]===0) {
        pPointer -= 1;
    }
    while (dPointer>=0 || pPointer>=0) {
        let dist = Math.max(dPointer+1, pPointer+1);
        answer += dist*2;
        while (dTruck>0) {
            let post = Math.min(dTruck, deliveries[dPointer]);
            dTruck -= post;
            deliveries[dPointer] -= post;
            if (deliveries[dPointer] === 0) {
                dPointer -= 1;
            }
        }
        while (deliveries[dPointer]!==undefined && deliveries[dPointer]===0) {
            dPointer -= 1;
        }
        while (pTruck>0) {
            let post = Math.min(pTruck, pickups[pPointer]);
            pTruck -= post;
            pickups[pPointer] -= post;
            if (pickups[pPointer]===0) {
                pPointer -= 1;
            }
        }
        while (pickups[pPointer]!==undefined && pickups[pPointer]===0) {
            pPointer -= 1;
        }
        dTruck = cap;
        pTruck = cap;
    }
    return answer;
}