print('s\nst\nstr\nstri\nstring\nstri\nstr\nst\ns')
def translate (phrase):
    translation =''
    for a in phrase:
        if a in "aeiouAEIOU":
            translation=translation +"g"
        else :
            translation = translation + a
    return translation
print(translate (input("enter a phrase")))
