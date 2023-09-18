import wikipedia

page_name = input("Please enter a title or search sentence")
page_name = page_name.title()
while page_name:
    if page_name == "":
        break
    result_page = wikipedia.search(str(page_name))[0]
    whole_page = wikipedia.page(result_page, auto_suggest=False)
    print(whole_page.title)
    print(wikipedia.summary(title=str(result_page), sentences=3))
    print(whole_page.url)
    page_name = input("Please enter a title or search sentence")

