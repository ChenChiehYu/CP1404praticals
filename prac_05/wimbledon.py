def main():
    CHAMPIONS = dict()
    COUNTRYS = dict()
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        lines = in_file.readlines()
        result = get_rows(lines, 1, 2)
        count_result(CHAMPIONS, COUNTRYS, result)
    print_result(CHAMPIONS, COUNTRYS)


def count_result(CHAMPIONS, COUNTRYS, result):
    for word in result:
        if len(word) > 3:
            if word in CHAMPIONS:
                CHAMPIONS[word] += 1
            else:
                CHAMPIONS[word] = 1
        else:
            COUNTRYS[word] = 1


def get_rows(lines, row1, row2):
    result = []
    for words in lines:
        result.append(words.split(',')[row1])
        result.append(words.split(',')[row2])
    return result

def print_result(CHAMPIONS, COUNTRYS):
    print("Wimbledon Champions: ")
    for i in CHAMPIONS.items():
        print(f"{i[0]} {i[1]}")
    print()
    countries = sorted(COUNTRYS.keys())
    print(f"These {len(countries)} countries have won Wimbledon:")
    for j in range(0, len(countries)):
        print(countries[j], end=", ")

main()