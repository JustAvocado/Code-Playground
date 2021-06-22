function fibonacci(n) {
    let n1 = 0, n2 = 1, temp = 0;
    for (let i = 0; i < n; i++) {
        console.log(n1);
        temp = n1;
        n1 += n2;
        n2 = temp;
    }
};

fibonacci(5);
