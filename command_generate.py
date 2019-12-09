'''
@Author: SaminShi
@Date: 2019-11-07 20:54:56
@LastEditors: SaminShi
@LastEditTime: 2019-12-08 19:29:06
@Description: example
@Email: shizhimin0406@163.com
@Company: xxx
@version: 1.0
'''
# -*- coding: utf-8 -*-

def command_dict_gereate(frame = 0,slot = 1,pid = 0,ontid = 0,*args,**kwargs):
    bid,portid = slot,pid
    command_dicts = {}
    result_dicts = {}
    line_profile_id = kwargs.get('line_profile_id') or 1
    srv_profile_id = kwargs.get('srv_profile_id') or 1
    command_dicts[0]= [
        'interface gpon 0/{0}'.format(bid),
        'display ont ver {0} {1}'.format(portid,ontid)
        ]

    command_dicts[1]= [
        'interface gpon111 0/{0}'.format(bid),
        'display ont ver1111 {0} {1}'.format(portid,ontid)
        ]
    
    command_dicts[2]= [
        'interface gpon2222 0/{0}'.format(bid),
        'display ont ver2222 {0} {1}'.format(portid,ontid)
        ]
    command_dicts[3]= [
        'interface gpon2222 0/{0}'.format(bid),
        'lineprofile profile {0}'.format(line_profile_id),
        'srvprofile profile {0}'.format(srv_profile_id)
        ]

    if len(args) == 0:
        return None
    else:
        for val in args:
           result_dicts[val] = command_dicts[val]
        return result_dicts

command_list = [1,2]

other_para = {'line_profile_id':2}

print(command_dict_gereate(0,1,2,3,*command_list,**other_para))
