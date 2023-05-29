# working with tuples

fruits = ('orange' , 'mango' , 'banana' , 'sweet apple' , 'kiwi' , 'cherry' , 'pineaples' , 'water melon')
print(type (fruits))

#accessing your tuple items
fruits = ('orange' , 'mango' , 'banana' , 'sweet apple' , 'kiwi' , 'cherry' , 'pineaples' , 'water melon')

print (fruits)




#Dictionararies

student = {
    'name': 'Ebenezer',
    'Country' : 'Nigeria',
    'Sex':'Male',
    'City': 'Lagos'
}
print(student)

#accessing your dictionary

student = {
    'name': 'Rafique',
    'Country' : 'Ghana',
    'Sex':'Male',
    'City': 'Kumasi'
}
print(student['Country'])


#update dictionaires

student = {
    'name': 'Ebenezer',
    'Country' : 'Nigeria',
    'Sex':'Male',
    'City': 'Lagos'
}
student.update({'city': 'Abuja'})
print(student)


#conditional statement
#if statement

a=33
b=200
if b>a:
    print('b is greater than a')

    #elif statement
    a=33
    b=33
    if b>a:
        print('b is greater than a')
    elif a==b:
        print('a and b are equal')


    #else statement
    a=200
    b=33
    if b>a:
        print('b is greater than a')
    elif a==b:
        print('a and b are equal')
    else:
        print('a is greater than b')

        #else with elif statement

        a=200
        b=33
        if b>a:
            print('b is greater than a')
        else:
            print('b is not greater than a')

            #And keyword


            
        