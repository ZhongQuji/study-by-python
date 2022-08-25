import os
class ReciteLogic:
    def __init__(self):
        self.user_name =''

    # 首页
    def welcome(self, name):
        self.user_name = name
        print('=' * 20)
        print(name + '的生词记录本')
        print('1.查看单词')
        print('2.背单词')
        print('3.添加新单词')
        print('4.删除单词')
        print('5.清空单词')
        print('6.退出')
        print('=' * 20)
        while True:
            option = input("请输入功能选项（生词本）：\n")
            if option == '1':
                self.see_words()
            elif option == '2':
                self.recite_words()
            elif option == '3':
                self.add_words()
            elif option == '4':
                self.del_words()
            elif option == '5':
                self.clear_words()
            elif option == '6':
                break

    # 文件中的数据转换为字典
    def convert_data(self):
        info_li = []
        with open('./' + self.user_name + '.txt', mode='r+', encoding='utf8') as f:
            info_data = f.readlines()
            for i in info_data:
                info_dict = dict()
                # 替换{ 和 } 并去掉空格
                step_one = i.replace('{', '').replace('}', '')
                # 以冒号进行分隔
                step_two = step_one.split(':')
                en = step_two[0].split(',')[0].replace("'", '').strip()
                zh = step_two[1].split(',')[0].replace("'", '').strip()
                info_dict[en] = zh
                # 保存到列表中
                info_li.append(info_dict)
        return info_li

    # 查看单词
    def see_words(self):
        if os.path.exists('./' + self.user_name + '.txt') is not True:
            print('当前无数据，请先添加单词')
        else:
            words_data = self.convert_data()
            if len(words_data)==0:
                print("生词本内容为空")
            else:
                #  读取文件数据
                with open('./' + self.user_name + '.txt', mode='r+', encoding='utf8') as f:
                    info_data = f.readlines()
                for i in info_data:
                    print(i.replace('{', '').replace('}', '').strip())

    # 背单词
    def recite_words(self):
        if os.path.exists('./' + self.user_name + '.txt') is not True:
            print('当前无数据，请先添加单词')
        else:
            words_data = self.convert_data()
            if len(words_data) == 0:
                print("生词本内容为空")
            else:
                words_li = self.convert_data()
                # 所有英文单词
                en_li = []
                for i in words_li:
                    for j in i.keys():
                        en_li.append(j)
                # 随机产生的英语单词
                for random_word in set(en_li):
                    # 获取该单词在en_li中的索引
                    random_word_index = en_li.index(random_word)
                    # 获取该单词所对应的中文
                    words_zh = words_li[random_word_index][random_word]
                    in_words = input("请输入" + random_word + '翻译' + '：\n')
                    # 判断翻译是否正确
                    if in_words ==words_zh:
                        print('太棒了')
                    else:
                        print('再想想')

    # 添加新单词
    def add_words(self):
        if os.path.exists('./' + self.user_name + '.txt') is not True:
            with open('./' + self.user_name + '.txt', mode='w+', encoding='utf8') as f:
                f.write('')
        word_data_dict = dict()
        new_words = input('请输入新单词：')
        # 判断输入的单词是否已存在
        words_li = self.convert_data()
        # 所有英文单词
        en_li = []
        for i in words_li:
            for j in i.keys():
                en_li.append(j)

        if new_words in en_li:
            print('添加的单词已存在')
        else:
            translate = input('请输入单词翻译：')
            if os.path.exists('./' + self.user_name + '.txt') is not True:
                with open('./' + self.user_name + '.txt', mode='w', encoding='utf8') as f:
                    f.write('')
            word_data_dict[new_words] = translate
            with open('./' + self.user_name + '.txt', mode='a+', encoding='utf8') as info_data:
                info_data.write(str(word_data_dict) + "\n")

    # 删除单词
    def del_words(self):
        if os.path.exists('./' + self.user_name + '.txt') is not True:
            print('当前无数据，请先添加单词')
        else:
            words_data = self.convert_data()
            if len(words_data) == 0:
                print("生词本内容为空")
            else:
                words_li = self.convert_data()
                # 所有英文单词
                en_li = []
                for i in words_li:
                    for j in i.keys():
                        en_li.append(j)
                del_words = input("请输入要删除的单词：\n")
                if del_words not in en_li:
                    print('删除的单词不存在')
                else:
                    # 获取要删除单词的索引
                    del_words_index = en_li.index(del_words)
                    # 删除单词
                    words_li.pop(del_words_index)
                    print('单词删除成功')
                    # 重新写入数据
                    with open('./' + self.user_name + '.txt', mode='w+', encoding='utf8') as f:
                        f.write('')
                    for i in words_li:
                        with open('./' + self.user_name + '.txt', mode='a+', encoding='utf8') as info_data:
                            info_data.write(str(i) + '\n')

    # 清空单词
    def clear_words(self):
        if os.path.exists('./' + self.user_name + '.txt') is not True:
            print('当前无数据，请先添加单词')
        else:
            with open('./' + self.user_name + '.txt', mode='w+', encoding='utf8') as f:
                f.write('')

