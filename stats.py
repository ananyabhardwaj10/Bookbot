def count_words(words):
    num_words = words.split()
    return len(num_words)

def count_characters(char):
    char_holder = {}
    char = char.lower()
    counter = 1
    for c in char:
        if c in char_holder:
            char_holder[c] += 1 
        else:
            char_holder[c] = 1
    
    #print (char_holder)
    return char_holder

def sorted_report(ch_holder):
    ch_dict = []
    for c, n in ch_holder.items():
        small_dict = {"char": c, "num": n}
        ch_dict.append(small_dict)

      
    def sort_on_count(items):
        return items["num"]

    ch_dict.sort(reverse=True, key = sort_on_count)
    return ch_dict
    


