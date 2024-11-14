def all_variants(text):
    for i in range(len(text)):
        yield text[i]
        if i == 2:
            for j in range(len(text)):
                if j < 2:
                    yield text[j]+text[j+1]
                else:
                    yield text







a = all_variants("abc")
for i in a:
    print(i)