import wikipedia

def get_wiki():
    user_input = 'blank'
    while input != '':
        try:
            user_input = input('Search for a wikipedia page: ')
            page = wikipedia.page(user_input)
        except wikipedia.exceptions.DisambiguationError as e:
            print('The pages that "{0}" could refer to are: \nPlease be more specific with your search'.
                  format(user_input))
            print(e.options)
        except wikipedia.exceptions.PageError:
            print('{0} does not match any pages, try another query!'.format(user_input))
        else:
            print(page.url)
            print(page.title)
            print(page.summary)

get_wiki()



