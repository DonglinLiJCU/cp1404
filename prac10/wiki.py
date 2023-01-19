import wikipedia

user_search = input("Search: ")
while user_search != "":
    try:
        wiki_page = wikipedia.page(user_search, auto_suggest=False)
        print("Title: " + wiki_page.title)
        print(wikipedia.summary(user_search))
        print("URL: " + wiki_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        pass
    user_search = input("Search: ")
