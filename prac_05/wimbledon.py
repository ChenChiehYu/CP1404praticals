def main():
    CHAMPIONS = dict()
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readline()
        for line in lines:
            line=line.split("\n")
            for text in line:
                if text in CHAMPIONS:
                    CHAMPIONS[text]+=1
                else:
                    CHAMPIONS[text]=1

    print(CHAMPIONS)



def print_champions(champions):
    for key in champions:
        print(champions[key], champions)

def sort_country(countries):
    sorted_countries=sorted(countries)
    return sorted_countries

main()