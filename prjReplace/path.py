import os

class Path():

    def path_format(self,path):
        try:
            list_path = path.split('.')
            or_path = ''
            for item in list_path:
                or_path = os.path.join(or_path, item)
            if '/' in or_path:
                or_path = or_path.replace('/', '//')
                or_path = '//' + or_path
                return or_path
            elif '\\' in or_path:
                or_path = or_path.replace('\\', '\\\\')
                or_path = '\\\\' + or_path
                return or_path
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print('Invalid Path!!!')
            print('Try Again!!')
            path = input('Set Path: ')
            return self.path_format(path)


    def path_set(self, path_format):

        os.chdir(path_format)
        path_set = os.getcwd()
        return path_set

