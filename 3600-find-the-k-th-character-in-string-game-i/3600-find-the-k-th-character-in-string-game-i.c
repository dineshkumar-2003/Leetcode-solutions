char nextChar(char c) {
    return (c == 'z') ? 'a' : (c + 1);
}

char kthCharacter(int k) {
    char word[100000]; 
    int len = 1;
    word[0] = 'a';

    while (len < k) {
        int current_len = len;
        for (int i = 0; i < current_len && len < k; ++i) {
            word[len++] = nextChar(word[i]);
        }
    }

    return word[k - 1]; 
}

