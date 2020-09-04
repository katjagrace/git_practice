

def factorial(n):
    answer = 1
    for i in range(n+1)[1:]:
        answer = answer * i
    return answer

def probability(kids, eggs, p=.1):
    answer = factorial(eggs)/(factorial(eggs-kids)*factorial(kids))*(((1-p)**(eggs-kids))*(p**kids))
    return answer

def egg_kid_chances(total_eggs, p=0.1):
    for eggs in range(total_eggs+1):
        print('\nfor {} eggs:'.format(eggs))
        for kids in range(eggs+1):
            score = probability(kids, eggs)
            print('{} chance of {}'.format(round(score, 3), kids))

egg_kid_chances(40)
