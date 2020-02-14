# -*- coding: utf-8 -*-
import os
class abaqus_postprocesser(object):
    def __init__(self, odb_path):
        #printer
        self.odb_printer_template = "#-*- coding: mbcs -*-\nfrom abaqus import *\nfrom abaqusConstants import *\nfrom caeModules import *\nfrom odbAccess import *\nimport os\n    \ndef ODBPrinter(odbPath, variable, wid=400, heig=250):\n    filePath = os.path.dirname(odbPath)\n    PngName = odbPath.split('\\\\')[-1].split('.')[0]\n    PngPath = os.path.join(filePath, PngName+'_'+variable)\n    o = session.openOdb(name=odbPath)\n    myViewport = session.viewports['Viewport: 1']\n    myViewport.restore()\n    myViewport.setValues(displayedObject=o, width=wid, height=heig)\n    if variable=='S':\n        myViewport.odbDisplay.setPrimaryVariable(variableLabel='S',\n                                                 outputPosition=INTEGRATION_POINT, \n                                                 refinement=(INVARIANT, 'Mises'))\n    elif variable=='U':\n        myViewport.odbDisplay.setPrimaryVariable(variableLabel='U',\n                                                 outputPosition=NODAL, \n                                                 refinement= (INVARIANT, 'Magnitude'))\n    session.pngOptions.setValues(imageSize=(4096,4096))\n    myViewport.odbDisplay.display.setValues(plotState = CONTOURS_ON_DEF)\n    session.printOptions.setValues(vpDecorations=OFF, reduceColors=False)\n    session.printToFile(fileName=PngPath, format=PNG, canvasObjects=(myViewport, ))\n    o.close()\n    \nif __name__ == '__main__':\n    odbPath='odb file path mark'\n    for variable in ('S', 'U'):\n        ODBPrinter(odbPath=odbPath, variable=variable)"
        #data reader
        self.odb_data_reader_template = "#-*- coding: mbcs -*-\nfrom odbAccess import *\nimport os\n    \ndef ODBDataReader(odbPath, variable):\n    filePath = os.path.dirname(odbPath)\n    odb = openOdb(path=odbPath)\n    odb_name = odbPath.split('\\\\')[-1].split('.')[0]\n    #the set of nodes\n    #node_set_names = list(odb.rootAssembly.nodeSets.keys())\n    #all_nodes_set = node_set_names[0]\n    #steps frames\n    step_names = list(odb.steps.keys())\n    last_step = odb.steps[step_names[-1]]\n    last_frame = last_step.frames[-1]\n    \n    #  U  S\n    if variable=='U':\n        with open(filePath+'\\\\'+odb_name+'_'+variable+'.txt', 'w') as f:\n            f.writelines(', '.join(['nodeLabel','X','Y','Z','magnitude'+'\\n']) )\n            for v in last_frame.fieldOutputs[variable].values:\n                #nodeLabel  #XYZ U   #U\n                a_ndoe_data = [str(v.nodeLabel),\n                               str(v.data[0]),str(v.data[1]),str(v.data[2]),\n                               str(v.magnitude)+'\\n']\n                f.writelines( ', '.join(a_ndoe_data) )\n    elif variable=='S':\n        with open(filePath+'\\\\'+odb_name+'_'+variable+'.txt', 'w') as f:\n            f.writelines(', '.join(['elementLabel','mises','press','tresca'+'\\n']) )\n            for v in last_frame.fieldOutputs[variable].values:\n                # elementLabel  #mises press tresca \n                a_ndoe_data = [str(v.elementLabel),\n                               str(v.mises),str(v.press),str(v.tresca)+'\\n']\n                f.writelines( ', '.join(a_ndoe_data) )\n        \n    \nif __name__ == '__main__':\n    odbPath='odb file path mark'\n    for variable in ('S', 'U'):\n        ODBDataReader(odbPath=odbPath, variable=variable)"
        self.odb_path = odb_path
        self.odb_name = odb_path.split("\\")[-1].split(".")[0]
    
    #printer
    def _generate_printer_py(self):
        odb_printer = self.odb_printer_template.replace('odb file path mark',self.odb_path.replace("\\","\\\\"))
        file_path = os.path.dirname(self.odb_path)+"\\"+self.odb_name+"_odbPrinter.py"
        with open(file_path, 'w') as f:
            f.write(odb_printer)
        return file_path #printer .py file path
        
    def _printer(self):
        curr_path = os.getcwd() #当前路径
        
        printer_file_path = self._generate_printer_py()
        
        os.chdir( os.path.dirname(printer_file_path) )
        cmd_line = 'abaqus cae noGUI='+printer_file_path
        os.system( cmd_line )
        
        os.chdir( curr_path ) #返回到当前路径
        
    def printing_pngs(self):
        self._printer()

    #  data reader
    def __generate_data_reader_py(self):
        odb_data_reader_template = self.odb_data_reader_template.replace('odb file path mark',self.odb_path.replace("\\","\\\\") )
        file_path = os.path.dirname(self.odb_path)+"\\"+self.odb_name+"_odbDataReader.py"
        with open(file_path, 'w') as f:
            f.write(odb_data_reader_template)
        return file_path #printer .py file path
    
    def _data_reader(self):
        curr_path = os.getcwd() #当前路径
        
        data_reader_file_path = self.__generate_data_reader_py()
        
        os.chdir( os.path.dirname(data_reader_file_path) )
        cmd_line = 'abaqus cae noGUI='+data_reader_file_path
        os.system( cmd_line )
        
        os.chdir( curr_path ) #返回到当前路径

    def reading_data(self):
        self._data_reader()


if __name__ == '__main__':
    aba_pp = abaqus_postprocesser(odb_path="D:\\radar_project\\src\\data\\temp\\model_4\\Jobasad.odb")
    aba_pp._generate_printer_py()
    #aba_pp._printer()
    #aba_pp.printing_pngs()
    aba_pp.reading_data()