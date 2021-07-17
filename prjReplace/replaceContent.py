from path import Path
from file import File
from replace import Replace

config_path = Path()
path = input('Set path: ')
path = config_path.path_set(config_path.path_format(path))
file = File()
file.bkp_files(file.list_files(path),file.dir_create(path,'files_bkp'))
list_find=[]
list_replace=[]

find = input('Find.Find: ')
replace = input('Replace.Replace: ')
list_find= find.split('.')
list_replace= replace.split('.')
content = file.open_file_split_words(file.list_files(path))

replace = Replace()

list_replaced = replace.replace_words_for_word(list_find,list_replace,content)
file.write_files_md_words(file.list_files(path),list_replaced[0])

print('Changes writes: ')
print(list_replaced[1])




