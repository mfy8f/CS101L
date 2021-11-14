punctuation = '.?!,:;'
word_dict = {}

def get_file():
    while True:
        file_name = input('Enter file')
        try:
            with open(file_name, 'r') as open_file:
                x = open_file.readlines()
                return x
        except:
            print('Input a correct file name')
            continue


def clean_words(word_list):
    for value in word_list:
        for pun in value:
            if pun in punctuation:
                word_list = word_list.replace(pun,"")
    return word_list




def word_counts(word_list):
    word_list = word_list.split()
    for value in word_list:
        x = value.lower()
        for x in word_list:
            y = len(x)
            if y > 3:
                if x not in word_dict.keys():
                    word_dict[x] = 1
                else:
                    word_dict[x] += 1
    return word_dict


def output_top_ten(word_dict):
    global new_word
    new_word = list(word_dict.items())
    new_word.sort(key= lambda item: item[1], reverse = True)
    return new_word

def main():
    word_list = str(get_file())
    update_word_list = clean_words(word_list)
    print(word_counts(update_word_list))
    print(output_top_ten(word_dict))
    for x, y in new_word:
        print(x, '       ' , y   )
    print(f'There are {len(x)} words that occur only once')
    print(f'There are {len(word_dict)} unique words')

if __name__ == "__main__":
    main()
