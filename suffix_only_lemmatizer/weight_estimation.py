# import numpy as np
# import array

def stemmer(word) :
    temp = 0
    suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा",u"क"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें",u"ाऊ",u"िक",u"ित",u"ीय",u"ीच",u"ेद",u"ेय",u"कर",u"जी",u"तः",u"ता",u"त्व",u"पन",u"गत",u"त्व"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं",u"ाना",u"ावा",u"िका",u"ियत",u"िया",u"ीला",u"कार",u"जनक",u"दान",u"दार",u"बाज़",u"वाद",u"वान"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां",u"ात्मक",u"ीकरण",u"कारक",u"गर्दी",u"गिरी",u"वादी",u"वाला",u"वाले",u"शाली",u"शुदा"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"] }
    for L in 5, 4, 3, 2, 1 :
        if len(word) > L + 1 :
            for suf in suffixes[L] :
                if word.endswith(suf) :
                    stem = word[:-L]
                    return stem
    return word



def difference(word, root_word, wt_consonant, wt_vowel) :
    stem = stemmer(word)
    vowels = {u'\u0900',u'\u0901',u'\u0902',u'\u0903',u'\u093A',u'\u093B',u'\u093C',u'\u093D',u'\u093E',u'\u093F',u'\u0940',u'\u0941',u'\u0942',u'\u0943',u'\u0944',u'\u0945',u'\u0946',u'\u0947',u'\u0948',u'\u0949',u'\u094A',u'\u094B',u'\u094C',u'\u094D',u'\u094E',u'\u094F',u'\u0951',u'\u0952',u'\u0953',u'\u0954',u'\u0955',u'\u0956',u'\u0957',u'\u0970',u'\u0971'}


    stem_tokens = [char for char in stem]
    root_word_tokens = [char for char in root_word]

    value_word = 0
    value_root_word = 0

    i = 0
    j = 0
    while (i < len(stem_tokens) and j < len(root_word_tokens)) :
        if stem_tokens[i] == root_word_tokens[j] :
            if stem_tokens[i] in vowels :
                value_word+=(wt_vowel*wt_vowel)
            else :
                value_word+=(wt_consonant*wt_consonant)
            i+=1
            j+=1
        else :
            if stem_tokens[i] in vowels :
                value_word-=(wt_vowel*wt_vowel)
                i+=1
            elif root_word_tokens[j] in vowels :
                value_word-=(wt_vowel*wt_vowel)
                j+=1
            else :
                value_word-=(wt_consonant*wt_consonant)
                i+=1
                j+=1
    if i == len(stem_tokens) :
        while j < len(root_word_tokens) :
            if root_word_tokens[j] in vowels :
                value_word-=(wt_vowel*wt_vowel)
            else :
                value_word-=(wt_consonant*wt_consonant)
            j+=1
    elif j == len(root_word_tokens) :
        while i < len(stem_tokens) :
            if stem_tokens[i] in vowels :
                value_word-=(wt_vowel*wt_vowel)
            else :
                value_word-=(wt_consonant*wt_consonant)
            i+=1



    i = 0
    while i < len(root_word_tokens) :
        if root_word_tokens[i] in vowels :
            value_root_word+=(wt_vowel*wt_vowel)
        else :
            value_root_word+=(wt_consonant*wt_consonant)
        i+=1



    return (value_root_word-value_word)







# print(difference(u"व्यावसायिक", u"व्यवसाय", 1, 0.5))


file = open("weight_estimation_dataset.txt", "r")
words = []
rootwords = []

line = file.readline()
for line in file:
    token = line.split()
    words.append(token[0])
    rootwords.append(token[1])


# print(words)
# print(rootwords)





# word = words[3]
# rootword = rootwords[3]

# print(difference(word, rootword, 1, 0.5))
min = 1000
optimal_vowel_weight = 0
values = []
wtVowel = 0.05
j = 0
while wtVowel < 10 :
    values.append(0)
    i=0
    while i < len(words) :
        word = words[i]
        rootword = rootwords[i]
        value = difference(word, rootword, 3, wtVowel)
        values[j]+=value
        i+=1

    if values[j] < min :
        optimal_vowel_weight = wtVowel

    j+=1
    wtVowel+=0.05

print(optimal_vowel_weight)





"""
values = []
# for i in range(0,15):
    # val.append([])
# print(sum)
sum_index = 0
vowel_weight = 0
consonent_weight = 0
length = len(word)
# print(len)
i=0
j=0
k=0
x=0
count = 0
while i<6:
    while j<4:
        while k<len-1:
            val[count].append(0)
            while x<len-1:
                print(word[x],rootword[x])
                val[count][k]+= differ(word[x],rootword[x],i,j)
                x+=1
            k+=1
            x=0
        j+=1
        k=0
        count+=1
    i+=1
    j=0
print(sum)
result = []
i=0
j=0
while i<6:
    while j<4:
        sums = val[count].sum()
        j+=1
        count+=1
        result.append(sums)
i+=1
j=0

for i in range(1,6):
    for j in range(1,4):
        for k in range(0,2):
            for x in range(0,2):
                print(i,j,k,x)
                x+=1

            k+=1
        j+=1
    i+=1
"""
