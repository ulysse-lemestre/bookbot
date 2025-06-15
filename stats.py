def get_num_words(bookContent):
    listOfWords = bookContent.split(maxsplit = -1)
    return len(listOfWords)

def get_num_char_dic(bookContent):
    dic = {}
    for char in bookContent.lower():
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

def sort_on(dic):
    return dic["num"]

def get_char_count_list(dic):
    ls = []
    for e in dic:
        ls.append({"char":e, "num":dic[e]})
    
    ls.sort(reverse = True, key = sort_on)
    return ls