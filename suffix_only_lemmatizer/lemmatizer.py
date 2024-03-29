def stemmer(word) :
    
    temp = 0
    
    suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"क",u"स",u"र",u"ज",u"ई"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें",u"ाऊ",u"िक",u"ित",u"ीय",u"ीच",u"ेद",u"ेय",u"कर",u"जी",u"तः",u"ता",u"पन",u"गत",u"ाऊ",u"वट",u"गी",u"वर",u"वट",u"मय",u"पा",u"पन",u"ाप",u"ाव"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं",u"ाना",u"ावा",u"िका",u"ियत",u"िया",u"ीला",u"कार",u"जनक",u"दान",u"दार",u"बाज",u"वाद",u"वान",u"मान",u"वती",u"ाकू",u"हीन",u"जनक",u"गार",u"शील",u"विध"u"वार",u"वाँ",u"खोर",u"खेज",u"करण",u"रान",u"मयी",u"मती",u"मंद",u"बंद",u"नेर",u"नाक",u"त्व",u"वाँ",u"ाका",u"ावट",u"ाहट",u"िकी",u"ीं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां",u"ीकरण",u"कारक",u"गिरी",u"वादी",u"वाला",u"वाले",u"शाली",u"शुदा",u"वाना",u"गिरी",u"गवार",u"शुदा",u"वासी",u"वाली",u"वाला",u"वाई‎",u"कारी",u"कारी",u"यारा",u"बारी",u"बाज़",u"धारी",u"दायक"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां",u"क्कड़",u"स्तान",u"मुक्त",u"बाज़ी",u"ार्थी",u"परायण",u"परस्त",u"ात्मक",u"गर्दी",u"कर्मी",u"कर्ता"],
    6: [u"ग्रस्त",u"पूर्वक"]
     }


    for L in 6, 5, 4, 3, 2, 1 :
        if len(word) > L + 1 :
            for suf in suffixes[L] :
                if word.endswith(suf) :
                    stem = word[:-L]
                    return stem


    return word




def lemmatize(word) :
    
    database = [line.rstrip('\n') for line in open('root_word_database.txt')]
    
    stem = stemmer(word)

    vowels = {u'\u0900',u'\u0901',u'\u0902',u'\u0903',u'\u093A',u'\u093B',u'\u093C',u'\u093D',u'\u093E',u'\u093F',u'\u0940',u'\u0941',u'\u0942',u'\u0943',u'\u0944',u'\u0945',u'\u0946',u'\u0947',u'\u0948',u'\u0949',u'\u094A',u'\u094B',u'\u094C',u'\u094D',u'\u094E',u'\u094F',u'\u0951',u'\u0952',u'\u0953',u'\u0954',u'\u0955',u'\u0956',u'\u0957',u'\u0970',u'\u0971'}

    wt_vowel = 0.5
    wt_consonant = 1



    if stemmer(stem) in database :
        
        return stemmer(stem)
        
    else :
        if stem in database :
            return stem
        


    stem_tokens = [char for char in stem]


    db_index = 0
    values = []
    
    for db_word in database :
        db_word_tokens = []
        db_word_tokens = [char for char in db_word]
        
        values.append(0)
        i = 0
        j = 0
        while (i < len(stem_tokens) and j < len(db_word_tokens)) :
            if stem_tokens[i] == db_word_tokens[j] :
                if stem_tokens[i] in vowels :
                    values[db_index]+=(wt_vowel*wt_vowel)
                else :
                    values[db_index]+=(wt_consonant*wt_consonant)
                i+=1
                j+=1
            else :
                if stem_tokens[i] in vowels and db_word_tokens[j] in vowels :
                    values[db_index]-=(wt_vowel*wt_vowel)
                    i+=1
                    j+=1
                elif stem_tokens[i] not in vowels and db_word_tokens[j] not in vowels :
                    values[db_index]-=(wt_consonant*wt_consonant)
                    i+=1
                    j+=1
                elif stem_tokens[i] in vowels :
                    values[db_index]-=(wt_vowel*wt_vowel)
                    i+=1
                elif db_word_tokens[j] in vowels :
                    values[db_index]-=(wt_vowel*wt_vowel)
                    j+=1
        if i == len(stem_tokens) :
            while j < len(db_word_tokens) :
                if db_word_tokens[j] in vowels :
                    values[db_index]-=(wt_vowel*wt_vowel)
                else :
                    values[db_index]-=(wt_consonant*wt_consonant)
                j+=1
        elif j == len(db_word_tokens) :
            while i < len(stem_tokens) :
                if stem_tokens[i] in vowels :
                    values[db_index]-=(wt_vowel*wt_vowel)
                else :
                    values[db_index]-=(wt_consonant*wt_consonant)
                i+=1


        db_index+=1


    return database[values.index(max(values))]


# lemma = lemmatize(u"व्यावसायिक")
# lemma = lemmatize(u"शारीरिक")
# lemma = lemmatize(u"नियमित")
lemma = lemmatize(u"व्यावसायिकता")
# lemma = lemmatize(u"चारित्र्य")
# lemma = lemmatize(u"लड़कपन")
# lemma = lemmatize(u"विद्यावान")
# lemma = lemmatize(u"विद्यार्थी")
# lemma = lemmatize(u"संभावना")
# lemma = lemmatize(u"संख्यात्मक")
# lemma = lemmatize(u"सम्बन्धी")
# lemma = lemmatize(u"गलतियों")
# lemma = lemmatize(u"सफाई")
# lemma = lemmatize(u"कालिक")
# lemma = lemmatize(u"सामाजिक")
# lemma = lemmatize(u"कालापन")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"मिठास")
# lemma = lemmatize(u"लोहार")
# lemma = lemmatize(u"सुगंधित")
# lemma = lemmatize(u"भुलक्कड़")
# lemma = lemmatize(u"नाटककार")
# lemma = lemmatize(u"टिकाऊ")
# lemma = lemmatize(u"बिकाऊ")
# lemma = lemmatize(u"गाड़ीवाला")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"लिखावट")
# lemma = lemmatize(u"औषधीय")
# lemma = lemmatize(u"औषधीय")

# print("the root word : ",lemma)



inputWords = [line.rstrip('\n') for line in open('root_word_database.txt')]
outputFile = open("output_database.txt","w+")




# inputWords = [line.rstrip('\n') for line in open('input.txt')]
# outputFile = open("output.txt","w+")


for word in inputWords :
    outputFile.write(str(word) + " : " + str(lemmatize(word)) + "\n")

