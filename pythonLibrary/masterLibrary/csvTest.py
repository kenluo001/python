import csv
import random

with open('scores.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)
        # writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)


with open('scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for data_list in reader:
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()


# 将来如果大家使用Python做数据分析，很有可能会用到名为pandas的三方库，它是Python数据分析的神器之一。pandas中封装了名为read_csv和to_csv的函数用来读写CSV文件，其中read_CSV会将读取到的数据变成一个DataFrame对象，而DataFrame就是pandas库中最重要的类型，它封装了一系列用于数据处理的方法（清洗、转换、聚合等）；而to_csv会将DataFrame对象中的数据写入CSV文件，完成数据的持久化。read_csv函数和to_csv函数远远比原生的csvreader和csvwriter强大。