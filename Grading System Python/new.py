num=int(input(' Please Enter Your Mark: \n'))
if num<=100 and num>=80:
    print(' You are a Genious and You got A+ grade!')
elif num<79 and num>75:
    print('You got A grade')
elif num < 75 and num > 70:
    print('You got A- grade')
elif num < 70 and num > 65:
    print('You got B+ grade')
elif num < 65 and num > 60:
    print('You got B grade')
elif num <60 and num >50:
    print('You got C+ grade')
elif num <50 and num >40:
    print('You got C grade')
elif num<0:
    print('Invalid Option!')

else :
    print('Sorry! You are fail')









