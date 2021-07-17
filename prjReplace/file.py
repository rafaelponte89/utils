import  os
import shutil

class File():

    def dir_create(self, path_current, dir_bkp):
        try:
            path_current = os.path.join(path_current, dir_bkp)
            os.makedirs(dir_bkp)
            return path_current
        except FileExistsError:
            return path_current

    def write_files_md(self,list_files, files_replace):
        for i in range(0, len(list_files)):
            text = open(list_files[i], 'w')
            for j in range(0, len(files_replace[i])):
                text.write(str(files_replace[i][j])+'\n')
                #print(list_files[i])
                #print(files_replace[i][j])
            text.close()
        return 1

    def write_files_md_words(self, list_files, files_replace):
        for i in range(0, len(list_files)):
            text = open(list_files[i], 'w')
            for j in range(0, len(files_replace[i])):
                text.write(str(files_replace[i][j]) + ' ')
                # print(list_files[i])
                #print(files_replace[i][j])
            text.close()
        return 1

    def open_file_split_lines(self,list_files):

        list_content = []
        for i in list_files:
            text = open(i,'r')
            content = text.read().split('\n')
            text.flush()
            text.close()
            list_content.append(content)
        return list_content

    def list_files(self, path_current):
        list_files = os.listdir(path_current)
        for i in list_files:
            if i[-4] != '.':
                list_files.remove(i)
        return list_files

    def bkp_files(self, list_files, path_bkp):
        # list_files = self.list_files(path)
        if len(os.listdir(path_bkp)) == 0:
            for i in list_files:
                shutil.copy(i, path_bkp)

    def open_file_split_words(self, list_files):

        list_content = []
        for i in list_files:
            text = open(i, 'r')
            content = text.read().split(' ')
            text.flush()
            text.close()
            list_content.append(content)
        return list_content
