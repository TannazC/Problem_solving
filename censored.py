#Some on-line forums censor inappropriate language by using simple replacement
#algorithms. For instance, the word “damn” might be replaced by the word “dang” to placate the
#easily-offended. Create a (polite!) list of words to be replaced in a given string, and a second list
#containing their replacements, then use both lists to replace all inappropriate words in the string.

string=input("Enter a sentance: ")

curse=["damn", "hell"]
replace=["dang","heck"]

for word in curse:
    if word in string and string.count(word)==1:
        curse_pos=curse.index(word)
        new=replace[curse_pos]
        str_pos=string.find(word)
        newstr=string[0:str_pos]+new+string[str_pos+len(new):]
        string=newstr
    elif word in string and string.count(word)>1:
        for instance in range(0,string.count(word)):
            curse_pos=curse.index(word)
            new=replace[curse_pos]
            str_pos=string.find(word)
            newstr=string[0:str_pos]+new+string[str_pos+len(new):]
            string=newstr
           

print(newstr)