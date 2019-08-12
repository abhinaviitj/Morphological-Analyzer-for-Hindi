import codecs
suffixes_list = []
female_list = ["कुभु","कुर्रम","कुभा","काबुल","वितस्ता","झेलम","आस्किनी","चिनाव","पुरुष्णी","रावी","शतुद्रि","सतलज","विपाशा","व्यास","सदानीरा","गंडक","दृषद्वती","घग्घर","गोमती","गोमल","सुवास्तु","स्वात","सिन्ध","सरस्वती","घघ्घर","सुषोमा","सोहन","मरुद्वृधा","मरुवर्मन"
]
male_list = [" रविवार","सोमवार","मंगलवार","बुधवार","गुरुवार","शुक्रवार","शनिवार","मंगल","बुध","वरूण","शनि","पृथ्‍वी","बृहस्‍पति","अरूण","शुक्र","अटलांटिक","पसिफ़िक","इंडियन","आर्कटिक ","साउथर्न","अंटार्कटिक","मोती","माणिक","मूंगा","पुष्कराज","हीरा","नीलम","गोमेद",""]

suffixes_list.append(u'\u0938' + u'\u0940')
suffixes_list.append(u'\u0916' + u'\u0940')
suffixes_list.append(u'\u0930' + u'\u0940')
suffixes_list.append(u'\u0928' + u'\u0940')
suffixes_list.append(u'\u092C' + u'\u0928')
suffixes_list.append(u'\u092F' + u'\u093E')
suffixes_list.append(u'\u0924' + u'\u093E')
suffixes_list.append(u'\u0907' + u'\u092F' + u'\u093E')
suffixes_list.append(u'\u0908')
suffixes_list.append(u'\u0905' + u'\u093E' + u'\u0908')
suffixes_list.append(u'\u0905' + u'\u093E' + u'\u0935' + u'\u091F')
suffixes_list.append(u'\u093F' + u'\u092F' + u'\u093E' + u'\u0901')
suffixes_list.append(u'\u0915' + u'\u0940')
suffixes_list.append(u'\u0928')
suffixes_list.append(u'\u0928' + u'\u0947' + u'\u0902')
# suffixes_list.append(u'\u0905' + u'\u093E' + u'\u0908')
# suffixes_list.append(u"\u0901")
# suffixes_list.append(u"\u093E" + u"\u0902")
outfile = open("output.txt","w")
with codecs.open("hindi.txt", encoding="utf-8") as f:
    for line in f:
        for word in line.split():
            if word in female_list:
                outfile.write(word+" Feminine\n")
            elif word in male_list:
                outfile.write(word+"Masculine\n")
            else:
                flag = 0;
                for suffix in suffixes_list:
                    if word.endswith(suffix):
                        outfile.write(word+" Feminine\n")
                        flag = 1
                        break;
                if flag==0:
                    outfile.write(word+" Masculine\n")
outfile.close()
