'''

'''

a = ['cwh', 'ts','m3', 'df']
b = ['rasp', 'cv', 'android', 'ios']

# for i in range(0,len(a)):
#     print('computer used by ', a[i], "is", b[i])


for i in range(0,len(a)):
    template = "computer used by {1} is {0}"
    print(template.format(a[i],b[i]))