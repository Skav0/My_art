int addDigits(int num) {
    int n;
    n = num;
    while (10 <= n) {
        n = (n % 10) + (n / 10);
    }
    return n;
}
