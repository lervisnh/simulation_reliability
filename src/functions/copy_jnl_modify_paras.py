import sys
sys.path.append("../") 

from config import get_run_environ
temp_path, app_path = get_run_environ()

import os
import shutil

class copy_jnl_modify_paras(object):
    # 构造说明

    #传入参数
    def __init__(self, copy_path, ext_path, to_add_paras):
        self.model_id = copy_path.split('\\')[-1].split('.')[0]
        if ext_path: #is not None
            self.ext_path = ext_path.replace("\\", "\\\\")
            #print( ext_path )
        else:
            self.ext_path = ext_path
        self.copy_path = copy_path
        self.to_add_paras = to_add_paras
        
    def _copy_jnl(self): #读取文件内容
        with open(self.copy_path, 'r') as copy_file:
            content = copy_file.read()
        return content

    def _job_name(self):
        content = self._copy_jnl()

        job_start_index = content.find( "mdb.Job" )
        job_name_start_index = content[job_start_index:].find( "name=" )
        job_name_end_index = content[job_start_index+job_name_start_index:].find( "'," )
        job_name = content[ job_start_index+job_name_start_index+6 : job_start_index+job_name_start_index+job_name_end_index ]
        return job_name
    
    def _modify_paras(self):#修改参数
        content = self._copy_jnl()
        
        job_name = self._job_name()
        #print( job_name )
        if self.ext_path:
            ext_model_start_index = content.find( "mdb.openStep('" )
            ext_model_end_index = content[ext_model_start_index:].find( "'," ) + ext_model_start_index
            content = content[:ext_model_start_index+14]+self.ext_path+content[ext_model_end_index:]
            
        set_value_index = content.find( "magnitude" )
        while set_value_index >= 0 :
            bracket_index = content[set_value_index:].find(')') + set_value_index #后括号位置
            comma_index = content[set_value_index:].find(',') + set_value_index #逗号位置
                       
            content = content[0:set_value_index] +"magnitude=" +str(self.to_add_paras)+\
                        content[min(bracket_index,comma_index):]
                        
            if content[set_value_index+1 :].find("magnitude") >= 0:
                set_value_index += content[set_value_index+1 :].find("magnitude")+1
            else:
                set_value_index = -1 #找不到匹配，返回为-1
        
        if "mdb.jobs['"+job_name+"'].submit" not in content:
            content += "\nmdb.jobs['"+job_name+"'].submit()\n"
        
        return content
    
    def get_content(self):
        return self._modify_paras()

    def write_to_file(self, file_name):
        curr_path = os.getcwd() #当前路径
        
        content = self.get_content()
        if os.path.exists(temp_path+"/model_"+self.model_id):#路径存在
            shutil.rmtree( temp_path+"/model_"+self.model_id )
        os.makedirs(temp_path+"/model_"+self.model_id)
        os.chdir( temp_path+"/model_"+self.model_id )
        #print( os.getcwd() ) 
        file_path = file_name+".py"
        with open(file_path, 'w') as f:
            f.write(content)
        
        os.chdir( curr_path ) #返回到当前路径
        
if __name__=='__main__':
    content = copy_jnl_modify_paras(copy_path='D:\\Projects\\python\\radar_project\\src\\abaqus\\demo_cae_file\\demo.jnl', 
                                    to_add_paras=-1000)
    content_str = content._modify_paras()
    #print( content_str )