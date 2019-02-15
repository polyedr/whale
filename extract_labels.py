import os


with open('test.csv', 'w') as f:
    print("Image", file=f)
    for x in os.listdir('.'+'/source/test/'):
        print(x, file=f)
