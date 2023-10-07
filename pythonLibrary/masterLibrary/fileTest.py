
file = open('fileTest.txt', 'r', encoding='utf-8')
print(file.read())
file.close()

# file = open('fileTest.txt', 'a', encoding='utf-8')
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')
# file.write('\n')
# file.close()

for x in range(1,100):
    file = open('fileTest.txt', 'a', encoding='utf-8')
    file.write('\n第几个：'+str(x))
    file.write('\n标题：《致橡树》')
    file.write('\n作者：舒婷')
    file.write('\n时间：1977年3月')
    file.write('\n')
    file.close()
