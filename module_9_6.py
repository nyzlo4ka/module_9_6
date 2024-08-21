def all_variants(text):
    for item in range(1, len(text) + 1):
        for j in range(len(text) - item + 1):
            yield text[j:j + item]


a = all_variants("abc")
for i in a:
    print(i)
