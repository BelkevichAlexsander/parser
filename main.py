import pandas

from parser_name import search_name
from parser_company import search_company
from parser_hello import search_hello
from parser_bye import search_bye


def main():
    '''
        The function reads the file and checks each line of the file 
        for the presence of the desired words
    '''

    # read the file format csv into pandas dataframe
    file = pandas.read_csv("test_data_copy.csv")


    # The dictionary to store values by keys
    dct_words = {}
    # The list to store all information
    lst_words = []

    #iterate through rows of file
    for index, row in file.iterrows():
        # getting text from a file.csv
        text = row["text"]
        
        # call a function to check if the name is in the string 
        # and if the name is parsed add it to the dictionary
        name_manager = search_name(text, row)
        if name_manager != None:
            dct_words.update(name_manager)

        # call a function to check if the company is in the string 
        # and if the name is parsed add it to the dictionary
        name_company = search_company(text, row)
        if name_company != None:
            dct_words.update(name_company)
        
        # call a function to check if the greeting is in the string 
        # and if the name is parsed add it to the dictionary
        hi = search_hello(text, row)
        if hi != None:
            dct_words.update(hi)
        
        # call a function to check if a goodbye is in the string 
        # and if the name is parsed add it to the dictionary
        bye = search_bye(text, row)
        if bye != None:
            dct_words.update(bye)

        # check to separate information by dialogue 
        # or add information from the last dialogue     
        if row['line_n'] == 0 and dct_words != {} or index == (len(file) - 1):
            lst_words.append(dct_words)
            dct_words = {}
    
    __print_data(lst_words)


def __print_data(lst):
    '''
        Function for outputting data to the console
    '''

    count = 0
    for x in lst:
        count += 1

        # manager requirements check
        if x.get('hi') == None or x.get('bye') == None:
            result = 'no'
        else:
            result = 'yes'
            
        print(f'Dialog {count} \nGreeting: {x.get("hi")} \nName manager: {x.get("name")}\n' + 
                f'Company: {x.get("company")} \nGoodbye: {x.get("bye")} \n' + 
                f'Requirement for manager: {result}\n\n')


if __name__ == '__main__':
    main()