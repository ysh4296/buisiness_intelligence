# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
from itertools import combinations

vec = []
min_sup = 0.5
dictionary = {1 :{'list size': 1}}
item_type = set()
buyer_cnt = 0
node_cnt = 0
combination_set = []
Erase_list = []
result = {0:{0:0}}

def get_support(min_num_of_item): # calculating support for current combination set
    cnt = 0.0
    temp = []
    for list in combination_set:
        res = 0
        for i in range(min_num_of_item,max_size_of_basket + 1):
            for Map in dictionary.get(i).items(): #Map[0] == tuple of itemset
                fit = True
                for item in list:
                    if item not in Map[0]:# not in tuple
                        fit = False
                        break
                if fit == True:
                    res += Map[1]
        res /= buyer_cnt
        print("--------")
        print("support : "  + str(res))
        if float(res) < min_sup: # reject data
            print("erase   : " + str(list))
            cnt+=1
            Erase_list.append(list)
        else:
            print("save   : " + str(list))
            temp.append(list)
            if min_num_of_item in result:
                result[min_num_of_item][tuple(list)] = res
            else:
                result[min_num_of_item] = {tuple(list):res}
        print("--------")
    return temp

if __name__ == '__main__':
    f = open('data.csv','r' , encoding = 'utf-8')
    rdr = csv.reader(f)
    Set = []
    temp = 1
    max_size_of_basket = 0
    for line in rdr:
        if line[0] == 'Transaction': continue
        if line[1] not in item_type:
            item_type.add(line[1])
        if temp == int(line[0]): #in the same buyer
            find = False
            for item in Set:
                if item == line[1]:
                    find = True
            if not find:
                Set.append(line[1])
        else: # end of shopping
            size_of_set = len(Set)
            print("buyer : " + str(temp))
            print("size of set  : "+ str(size_of_set))
            print("set : " + str(Set))
            tup = tuple(Set)
            find = False
            for key, value in dictionary.items():
                if key == size_of_set:
                    find = True
                    break
            if find == False:
                dictionary[size_of_set] = {'list size':size_of_set} # initialization
            find = False
            for Map in dictionary.get(size_of_set).items():
                if tup == Map[0]:
                    find = True
                    dictionary[size_of_set][tup] = dictionary[size_of_set][tup] + 1
                    buyer_cnt += 1
                    break
            if find == False:
                dictionary[size_of_set][tup] = 1
                buyer_cnt += 1
                node_cnt += 1
            temp = int(line[0])
            if max_size_of_basket < len(Set):
                max_size_of_basket = len(Set)
            Set = []
            Set.append(line[1])
    f.close()
    # deal with last element----------
    tup = tuple(Set)
    find = False
    for key, value in dictionary.items():
        if key == size_of_set:
            find = True
            break
    if find == False:
        dictionary[size_of_set] = {'list size': size_of_set}  # initialization
    find = False
    for Map in dictionary.get(size_of_set).items():
        if tup == Map[0]:
            find = True
            dictionary[size_of_set][tup] = dictionary[size_of_set][tup] + 1
            break
    if find == False:
        dictionary[size_of_set][tup] = 1
        node_cnt += 1
    buyer_cnt += 1
    # --------------------------------

    for item in item_type:
        temp = []
        temp.append(item)
        combination_set.append(temp)
    depth = 2
    combination_set = get_support(1)
    while len(combination_set) > 0: # there's possible way for combination
        Set = set()
        for item in combination_set:
            for index in item:
                if index in Set:
                    continue
                else:
                    Set.add(index)
        comb = list(combinations(Set, depth))
        combination_set = []
        for item in comb:
            valid = True
            for Erased in Erase_list:
                cnt = 0
                for index in Erased:
                    if index in item:
                        cnt += 1
                        continue
                if cnt == depth - 1:
                    valid = False
            if valid:
                combination_set.append(item)
        Erase_list = []
        print("pruned combination set   : " + str(combination_set))
        combination_set = get_support(depth)
        depth += 1

    print("printing result --------------")
    for i in range(1,depth-1):
        for item in result.get(i).items():
            print("accept combination : " + str(item[0]))
            print("support  : " + str(item[1]))
            
