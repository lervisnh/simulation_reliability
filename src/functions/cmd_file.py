import sys
sys.path.append("../") 

from config import get_run_environ
temp_path, app_path = get_run_environ()

import os

class cmd_file(object):
        def __init__(self, file_name):
                curr_path = os.getcwd() #当前路径

                os.chdir( temp_path+"/model_"+file_name )
                #print( os.getcwd() )
                cmd_line = 'abaqus cae noGUI='+os.getcwd()+'\\'+file_name+'.py'
                os.system( cmd_line )

                os.chdir( curr_path ) #返回到当前路径
