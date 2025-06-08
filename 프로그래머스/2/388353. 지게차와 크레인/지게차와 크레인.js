let dx = [-1, 0, 1, 0];
let dy = [0, 1, 0, -1];

function checkAccess(storage) {
    let checked = Array.from(new Array(storage.length), ()=> Array.from(new Array(storage[0].length), ()=> false));
    for (let i=0; i<storage.length; i++) {
        for (let j=0; j<storage[0].length; j++) {
            if (storage[i][j] === '-1') {
                let que = [[i,j]];
                while (que.length>0) {
                    let [cx,cy] = que.pop()
                    for (let k=0; k<4; k++) {
                        let nx = cx+dx[k];
                        let ny = cy+dy[k];
                        if (nx>-1 && ny>-1 && nx<storage.length && ny<storage[0].length && storage[nx][ny] === '0') {
                            storage[nx][ny] = '-1';
                            que.push([nx,ny]);
                        }
                    }
                    
                }
            }
        }
    }
}

function lift(storage, goal) {
    let takeOut = 0;
    for (let i=0; i<storage.length; i++) {
        for (let j=0; j<storage[0].length; j++) {
            if (storage[i][j] === goal) {
                for (let k=0; k<4; k++) {
                    let nx = i+dx[k];
                    let ny = j+dy[k];
                    if (nx>-1 && ny>-1 && nx<storage.length && ny<storage[0].length && storage[nx][ny] === '-1') {
                        storage[i][j] = '0';
                        takeOut += 1;
                        break;
                    }
                }
            }
        }
    }
    return takeOut;
}

function crane(storage, goal) {
    let takeOut = 0;
    for (let i=0; i<storage.length; i++) {
        for (let j=0; j<storage[0].length; j++) {
            if (storage[i][j] === goal) {
                storage[i][j] = '0';
                takeOut += 1;
            }
        }
    }
    return takeOut;
    
}

function solution(storage, requests) {
    var answer = storage.length * storage[0].length;
    let newStorage = [
        Array.from(new Array(storage[0].length+2), ()=> '-1'),
        ...storage.map((line)=>['-1',...line,'-1']),
        Array.from(new Array(storage[0].length+2), ()=> '-1')
    ]
    for (request of requests) {
        if (request.length === 1) {
            answer -= lift(newStorage, request);
        } else {
            answer -= crane(newStorage, request[0]);
        }
        checkAccess(newStorage);
    }
    return answer;
}