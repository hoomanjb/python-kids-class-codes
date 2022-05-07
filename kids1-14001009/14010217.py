# a = 'sala'
# b = 5 * a
# print(b)

# define
# def mohasebe_sanie_bar_asase_saat(days):
#     hours = days * 24
#     minutes = 60 * hours
#     seconds = minutes * 60
#     return seconds
#
#
# user_input = input('yek rooz vared konid: ')
# result = mohasebe_sanie_bar_asase_saat(days=int(user_input))
# print(result)

q1 = 'natijeye moadeleye roo b roo che mishavad ->  3 + 4 = ?  : '
q2 = 'natijeye moadeleye roo b roo che mishavad ->  5 * 2 = ?  : '
q3 = 'paytakht iran tehran ast ya kheir:  1)bale  2)kheir  : '

score = 0

def validate_questions(question, answer):
    user_answer = input(question)
    if int(user_answer) == answer:
        print('afarin dorost javab dadi')
        return 1
    else:
        print('javabe shoma eshtebah ast')
        return 0

score += validate_questions(question=q1, answer=7)
score += validate_questions(question=q2, answer=10)
score += validate_questions(question=q3, answer=1)

print('bazi tamam shod')
print('emtiaze nahaii shoma shode: ', score)