import sys
import time


def get_current_time_in_millis():
    return int(round(time.time() * 1000000))


def open_file(file_name):
    with open(file_name, encoding='iso-8859-1') as file:
        return file.read().splitlines()


def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list


def anagram_solver(word: str, dictionary: list):
    result_list = []
    permutations = permute_string(word)
    for perm in permutations:
        if perm in dictionary:
            result_list.append(perm)
    return result_list


if __name__ == '__main__':
    start_time = get_current_time_in_millis()

    dict_path = sys.argv[1]
    anagrammed_word = sys.argv[2]
    print(anagrammed_word)
    dictionary = open_file(dict_path)
    anagrams = anagram_solver(anagrammed_word, dictionary)

    end_time = get_current_time_in_millis()
    print(f"{end_time - start_time},{','.join(anagrams)}")
