#this is based on gradings masured by a system

percent = float(input('input percent of test in numbers'))

if percent >= 80 and percent < 101:
    print ('Student is Excelling')
elif percent >= 55 and percent < 80:
    print ('Student is Secure')
elif percent >= 30 and percent < 55:
    print ('Student is Developing')
elif percent >= 0 and percent < 30:
    print ('Student is foundation')
else:
    print('invalid interger')
