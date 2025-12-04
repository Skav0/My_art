int mostWordsFound(char **sentences, int sentencesSize) {
    int max, j, i, spc;

    max = 0;

    for (i = 0; i < sentencesSize; i++) {
        j = 0;
        spc = 1;

        while (j < strlen(sentences[i])) {
            if (sentences[i][j] == ' ') {
                spc = spc + 1;
            }
            j = j + 1;
        }

        if (spc > max) {
            max = spc;
        }
    }

    return max;
}
