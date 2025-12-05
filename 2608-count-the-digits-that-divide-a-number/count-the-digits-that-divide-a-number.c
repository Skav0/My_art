int countDigits(int num) {
    int x, c, n;
    x = num;
    c = 0;
    while (x != 0) {
        n = x % 10;
        if (num % n == 0) {
            c = c + 1;
        }
        x = x / 10;
    }
    return c;
}