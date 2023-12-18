def file_open(file_name):
        with open(file_name) as file:
                first_file = file.read()
                for line in first_file:
                        first_file = first_file.replace('\n', ' ')

        symbo_list = {'!': '.', '?': '.', '.': '.', '."': '".', '?"': '".', '!"': '".'}
        for a, b in symbo_list.items():
                if a in first_file:
                        first_file = first_file.replace(a, b)

        clean_file = first_file
        split_file = clean_file.split('.') 
        new_split_file = []
        for i in split_file:
                clean_line = ''
                for word in i:
                        if  word.isalpha():
                                clean_line += word
                        elif word == '"' or ' ' or '.' or ',':
                                clean_line += word
                new_split_file.append(clean_line)
        return new_split_file

def find_sirs(file):
        name_list =[]
        symbol_list = {1: ':', 2: ',', 3: '"'}
        for line in file:
                line = line.replace(symbol_list[1], ' ')
                line = line.replace(symbol_list[2], ' ')
                line = line.replace(symbol_list[3], ' ')
                words = line.split() 
                for index in range(len(words)):
                        if words[index] == 'Sir':
                                if words[index + 1] not in name_list:
                                        name_list.append(words[index + 1])
                        if words[index] == 'Sirs':
                                next_index = index + 1
                                if words[next_index] not in name_list:
                                        name_list.append(words[next_index])

                                while words[next_index + 1] != 'and':
                                        next_index = next_index + 1
                                        next_index
                                        if words[next_index] not in name_list:
                                                name_list.append(words[next_index])
                                else:
                                        stop_index = next_index + 1
                                        last_index = stop_index + 1
                                        if words[last_index] not in name_list:
                                                name_list.append(words[last_index])
        return sorted(name_list)

def find_saying(file):
        symbol_list = {1: ':', 2: ',', 3: '"'}
        condition = {}
        for line in file:
                if '"' in line:
                        split_line = line.split()
                        saying_index = []
                        saying = []
                        rest_saying = []
                        for word in split_line:
                                if '"' in word:
                                        saying_index.append(split_line.index(word))

                        if saying_index[0] == 0:
                                rest_saying.append(' '.join(split_line[saying_index[1] + 1:]))
                                saying.append(' '.join(split_line[saying_index[0]: saying_index[1] + 1]))

                        else:
                                rest_saying.append(' '.join(split_line[:saying_index[0]]))
                                rest_saying.append(' '.join(split_line[saying_index[1] + 1:]))
                                saying.append(' '.join(split_line[saying_index[0]: saying_index[1] + 1]))
                        
                        for sentence in rest_saying:
                                split_sentence = sentence.split()
                                for word in split_sentence:
                                        if word == 'Sir':
                                                name = split_sentence[split_sentence.index(word) + 1]
                                                name = name.replace(symbol_list[1], '')
                                                name = name.replace(symbol_list[2], '')

                        for sentence in saying:
                                sentence = sentence.replace(symbol_list[3], ' ')
                                sentence = sentence.replace(symbol_list[2], ' ')
                                sentence = sentence.replace('I ', 'Sir ' + name + ' ')
                                
                                condition[name] = condition.get(name, []) + [sentence]
        return condition


def check_condition(sentence, one_answer, name_list):
        split_sentence = sentence.split()
        person_list = []
        Knight_number = 0
        Knave_number = 0
        special_dic = {1: 'or', 2: 'cc'}
        for word in split_sentence:
                word.replace(',', '')
                if word in name_list:
                        if special_dic[1] in word:
                                person_list.append(word) 
                                split_sentence[split_sentence.index(word)] = word.replace(special_dic[1], special_dic[2])
                        else:
                                person_list.append(word)
                elif word == 'us':
                        person_list = name_list
                        
        sentence = ' '.join(split_sentence)

        if 'least one' in sentence or 'or' in sentence:
                if split_sentence[-1] == 'Knight' or split_sentence[-1] == 'Knights':
                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 1:
                                        Knight_number += 1
                        if Knight_number >= 1:
                                real_talk = True
                        else:
                                real_talk = False
        
                elif split_sentence[-1] == 'Knave' or split_sentence[-1] == 'Knaves':

                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 0:
                                        Knave_number += 1
                        if Knave_number >= 1:
                                real_talk = True
                        else:
                                real_talk = False
                        
        elif 'most one' in sentence:
                if split_sentence[-1] == 'Knight' or split_sentence[-1] == 'Knights':

                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 1:
                                        Knight_number += 1
                        if Knight_number <= 1:
                                real_talk = True
                        else:
                                real_talk = False
                                


                elif split_sentence[-1] == 'Knave' or split_sentence[-1] == 'Knaves':

                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 0:
                                        Knave_number += 1
                        if Knave_number <= 1:
                                real_talk = True
                        else:
                                real_talk = False
                                
        
        elif 'xactly one' in sentence:
                if split_sentence[-1] == 'Knight' or split_sentence[-1] == 'Knights':

                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 1:
                                        Knight_number += 1
                        if Knight_number == 1:
                                real_talk = True
                        else:
                                real_talk = False
                                


                elif split_sentence[-1] == 'Knave' or split_sentence[-1] == 'Knaves':

                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 0:
                                        Knave_number += 1
                        if Knave_number == 1:
                                real_talk = True
                        else:
                                real_talk = False
                                
        else:
                split_sentence = sentence.split()
                if split_sentence[-1] == 'Knight' or split_sentence[-1] == 'Knights':
                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 1:
                                        Knight_number += 1
                        if Knight_number == len(person_list):
                                real_talk = True
                        else:
                                real_talk = False


                elif split_sentence[-1] == 'Knave' or split_sentence[-1] == 'Knaves':
                        for name in person_list:
                                name = name.replace(',', '')
                                name_index = name_list.index(name)  
                                if one_answer[name_index] == 0:
                                        Knave_number += 1
                        if Knave_number == len(person_list):
                                real_talk = True
                        else:
                                real_talk = False
        
                                
        return real_talk

def find_answer(condition, name_list):
        from itertools import product
        possible_answer = list(product((0, 1), repeat=len(name_list)))

        answer = 0
        answer_list = []
        for one_answer in possible_answer:
                        finally_win = True
                        for person, person_saying in condition.items():
                                person_index = name_list.index(person)
                                if one_answer[person_index] == 1:
                                        is_Knight = True
                                else:
                                        is_Knight = False

                                totally_win = True
                                for saying in person_saying:
                                        sentence = saying
                                        real_condition = check_condition(sentence, one_answer, name_list)
                                        if is_Knight == True and real_condition == True:
                                                is_win = True
                                        elif is_Knight == False and real_condition == False:
                                                is_win = True
                                        else:
                                                is_win = False

                                        if is_win == False:
                                                totally_win = False
                                                break

                                if totally_win == False:
                                        finally_win = False
                                        break

                        if finally_win == True:
                                answer_list.append(one_answer)
                                answer += 1
        return answer, answer_list
                
def final_answer(answer, name_list):
        print('The Sirs are: ' + ' '.join(name_list))

        if answer[0] == 0:
                print('There is no solution.')
        elif answer[0] == 1:
                print ('There is a unique solution:')
                answer_list = answer[1][0]
                for i in range(len(name_list)):
                        if answer_list[i] == 0:
                                print('Sir ' + name_list[i] + ' is a Knave.' )
                        elif answer_list[i] == 1:
                                print('Sir ' + name_list[i] + ' is a Knight.' )
        else:
                print('There are ' + str(answer[0]) + ' solutions.')


file_name = input('Which text file do you want to use for the puzzle? ')
file = file_open(file_name)
name_list = find_sirs(file)
condition = find_saying(file)
answer = find_answer(condition, name_list)
final_answer(answer, name_list)
