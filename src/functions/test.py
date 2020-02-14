from copy_jnl_modify_paras import copy_jnl_modify_paras
from cmd_file import cmd_file

content = copy_jnl_modify_paras(copy_path='D:\\radar_project\\src\\abaqus\\demo_cae_file\\demo.jnl', to_add_paras=-1.5)
content = content.write_to_file( 'test_jnl_to_py' )
cmd_file('test_jnl_to_py')