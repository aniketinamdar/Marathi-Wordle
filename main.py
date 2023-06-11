import random

word_length = 3
chances = 4
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

print("Wordle Table")
for i in range(chances):
    for j in range(word_length):
        print("-", end=' ')
    print()

word_list = ['कमळ', 'वळण', 'वजन', 'मलई', 'नरम', 'गरम' , 'नजर', 'आभाळ', 'नयन', 'वरद', 'कपाळ', 'फणस', 'उत्तर', 'पालक', 
             'वार्षिक', 'परीक्षा', 'अमृत', 'मराठी', 'सरळ', 'पतंग']

#final output print
a = [] 



selected_word = random.choice(word_list)
selected_word_list=[]
selected_word_list = Convert(selected_word)
answer_list = []
for i in range (chances):
    user_input = input("Enter three lettered word (_ _ _) : ")
    
    user_input_list = []
    user_input_list = Convert(user_input)
    count = 0
    list_final = []
    
    for j in range(word_length):
        if selected_word_list[j] == user_input_list[j]:
            list_final.append(selected_word_list[j])
            count+=1
        else:
            #underline the wrong word
            temp = '_'+user_input_list[j]+'_'
            list_final.append(temp)

    if count==word_length:
        print("Done")
        a.append(''.join(list_final))
        for j in range(len(a)):
            print(a[j])
        break

    else:
        print("Wrong answer!")
        a.append(''.join(list_final))
        for j in range(len(a)):
            print(a[j])
