def is_new_word(word, char_count):
    temp_char_count = [0] * 26
    for ch in word:
        temp_char_count[ord(ch) - ord('a')] += 1

    for i in range(26):
        if char_count[i] != temp_char_count[i]:
            return False
    return True

def new_word_discovery(content, word):
    word_length = len(word)
    content_length = len(content)
    char_count = [0] * 26
    new_word_count = 0

    for ch in word:
        char_count[ord(ch) - ord('a')] += 1

    for i in range(content_length - word_length + 1):
        if is_new_word(content[i:i + word_length], char_count):
            new_word_count += 1
    return new_word_count

content = input().strip()
word = input().strip()

result = new_word_discovery(content, word)
print(result)
