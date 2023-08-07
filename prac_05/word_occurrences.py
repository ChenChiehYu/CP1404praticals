TEXT_COUNT = dict()
input_text = input("Text: ")
input_text = input_text.split()

for text in input_text:
    if text in TEXT_COUNT:
        TEXT_COUNT[text]+=1
    else:
        TEXT_COUNT[text]=1
sorted_text_count = sorted(TEXT_COUNT.items())
for i in sorted_text_count:
    print(f"{i[0]:{11}} : {i[1]}")