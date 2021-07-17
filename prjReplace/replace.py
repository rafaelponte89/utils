
class Replace():
    def __init__(self):
        self.count_word = {}

    def start_dict(self, list_words):
        for i in list_words:
            self.count_word[str(i)] = 0
        return self.count_word

    def count_replace(self, word, dict_word):
        dict_word[word] +=1
        return dict_word


    def replace_words_in_line(self,list_found,list_replace, list_content):
        h = 0
        c = 0
        for i in range(0, len(list_content)):
            for j in range(0, len(list_content[h])):
                while c < len(list_found):
                    if str(list_found[c]) in list_content[i][j]:
                        list_content[i][j] = str(list_content[i][j]).replace(list_found[c], list_replace[c])

                    c += 1
                c = 0
            h+=1
        return list_content

    def replace_words_for_word(self,list_found,list_replace, list_content):
        h = 0
        c = 0
        replace = Replace()
        dict_word = replace.start_dict(list_found)
        for i in range(0, len(list_content)):
            for j in range(0, len(list_content[h])):
                while c < len(list_found):
                    if replace.format_word(str(list_found[c])) == replace.format_word(list_content[i][j]):
                        format_word = replace.format_word(str(list_found[c]))
                        replace.count_replace(format_word,dict_word)
                        list_content[i][j] = str(list_content[i][j]).replace(list_found[c], list_replace[c])
                    c += 1
                c = 0
            h+=1
        return list_content, dict_word

    def format_word(self,string):
        sign = (',', '.', ':', ';', '?', '!','\n')
        size = len(string)-1
        string = str(string)
        if string.endswith(sign):
            return string[0:size]
        else:
            return string

#
#
# replace = Replace()
# path_format = replace.path_format('home.rafael.arquivos')
# set = replace.path_set(path_format)
# bkp = replace.dir_create(set,'bkp_files')
# lista = replace.list_files(set)
# replace.bkp_files(lista,bkp)
# #content = replace.open_file_split_lines(lista)
# content = replace.open_file_split_words(lista)
# print(content)
# p =['beleza','filha','Cinderela', 'rico', 'floresta']
# po = ['tristeza','daughter','Cadela', 'cisco','deserto']
# #listaReplace = replace.replace_words_in_line(p,po,content)
# listaReplace = replace.replace_words_for_word(p,po,content)
# print(listaReplace[1])
# #print(replace.write_files_md_words(lista,listaReplace))
# #replace.format_word('oi!')
# #print(replace.count_replace('oi'))
# # td = {}
# # td['tudo'] = 2
# # td['tudo'] +=1
# # td['outro'] = 0
# # td['outro'] +=1
# # print(td)
# dici = replace.start_dict(p)
# print(replace.start_dict(p))
# #print (replace.count_replace('beleza',dici))
#
