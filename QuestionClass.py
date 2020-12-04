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
            self.save_result_format(file_path,result)
            #self.save_result(file_path,result)


    def save_result(self,file_path,result):
        result_file_name=os.path.basename(file_path).split('.')[0]+'_result.txt'
        f=open(self.result_path+'/'+result_file_name,'w',encoding='utf-8')
        f.write(str(result))
        f.close()
    def save_result_format(self,file_path,result):
        result_file_name=os.path.basename(file_path).split('.')[0]+'_result.html'
        f=open(self.result_path+'/'+result_file_name,'w',encoding='utf-8')
        result_json= json.loads(result)
        if result_json['errorCode'] == '0':
            data=result_json['data']
            questions=data["questions"]
            text=data["text"]
            f.write("题目识别：<br/>"+text)
            i=0
            for answers in questions:
                i=i+1
                subject="科目："+answers["subject"]+"<br>"
                answer="答案：" +answers["answer"]+"<br>"
                analysis="分析："+answers["analysis"]+"<br>"
                knowledge="知识点："+answers["knowledge"]+"<br>"
                print(subject+answer+analysis+knowledge)
                result_each="<h3>搜题结果"+str(i)+"<br></h3>"
                result_each=result_each+subject+answer+analysis+knowledge+"<br>=================这是一条分隔符============<br>"
                f.write(result_each)
        else:
            f.write("result error code:"+result_json['errorCode'])







