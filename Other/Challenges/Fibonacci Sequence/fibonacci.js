function fibonacci(n) {
    let prevNum = 0;
    let currentNum = 1;
    let temp = 0;
    console.log(0);
    for (let i = 0; i < n - 1; i++) {
        console.log(currentNum);
        temp = currentNum;
        currentNum += prevNum;
        prevNum = temp;
    }
};

fibonacci(5);
