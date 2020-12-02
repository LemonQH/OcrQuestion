from OcrQuestion import *
import os
class Question():
    def __init__(self,file_paths,result_path):
        self.file_paths=file_paths
        self.result_path=result_path

    def start_ocr(self):
        for file_path in self.file_paths:
            result=connect(file_path)
            print(file_path)
            self.save_result(file_path,result)


    def save_result(self,file_path,result):
        result_file_name=os.path.basename(file_path).split('.')[0]+'_result.txt'
        f=open(self.result_path+'/'+result_file_name,'w',encoding='utf-8')
        f.write(str(result))
        f.close()

