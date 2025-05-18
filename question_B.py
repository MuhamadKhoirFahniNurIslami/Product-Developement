def pattern_count(text: str, pattern: str) -> int:
    # Jika pattern kosong, tidak ada yang bisa dicocokkan
    if len(pattern) == 0:
        return 0

    count = 0
    len_text = len(text)
    len_pattern = len(pattern)

    # Loop melalui text, cek apakah substring cocok dengan pattern
    for i in range(len_text - len_pattern + 1):
        match = True
        for j in range(len_pattern):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            count += 1

    return count

print(pattern_count("palindrom", "ind"))     
print(pattern_count("abakadabra", "ab"))     
print(pattern_count("hello", ""))     
print(pattern_count("ababab", "aba"))        
print(pattern_count("aaaaaa", "aa"))         
print(pattern_count("hell", "hello"))        