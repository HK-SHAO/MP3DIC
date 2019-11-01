import csv
import os
import re

def fi(l):
    return ' ' in l[0] and re.search(r'\d|\W', l[0].replace(' ', '')) is None

dic = []
words = []
with open('ecdict.csv','r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for w in reader:
        if fi(w):
            words.append(w[0].replace(' ', ''))
            dic.append(w)

def fo(s):
    n = 0
    for w in words:
        if s == w[:len(s)]:
            n += 1
    if n < 13:
        for w in words:
            if s == w[:len(s)]:
                del w
        return True
    return False

for line in dic:
    w = line[0]
    l3r = ''
    if line[3] is not '':
        l3r = '\n' + line[3].replace('\\n', '；')
    l2r = ''
    if line[2] is not '':
        l2r = '\n英文释义：{}'.format(line[2].replace('\\n', '；').replace('：n ', '：n. ').replace('；n ', '；n. '))
    l10r = ''
    if line[10] is not '':
        l10r = '\n' + line[10].replace('p:', '过去式：').replace('d:', '过去分词：').replace('i:', '现在分词：').replace('r:', '比较级：').replace('t:', '最高级：').replace('s:', '复数：').replace('3:', '三单：').replace('0:', '原型：').replace('1:', '形式：').replace('/', '；')
    l7r = ''
    if line[7] is not '':
        l7r = '\n考试要求：' + line[7].replace('zk', '中考').replace('gk', '高考').replace('cet4', '四级').replace('cet6', '六级').replace('ky', '考研').replace('ielts', '雅思').replace('toefl', '托福').replace('gre', 'GRE').replace(' ', '；')
    l1r = ''
    if line[1] is not '':
        l1r = '\n/{}/'.format(line[1])
    string = '【{}】{}{}{}{}{}'.format(w, l1r, l3r, l10r, l2r, l7r)

    path = ''
    b = ''
    for l in w:
        if l == ' ':
            b = ''
            continue
        b += l
        path += '{}-/'.format(b)
        if fo(b.replace(' ', '')):
            break
    path = 'DIC/' + path.lower()
    if not os.path.exists(path):
        os.makedirs(path)
        print(path)
    with open('{}-{}.txt'.format(path, w),'w', encoding='utf-8') as f:
        f.write(string)
    # print(string)