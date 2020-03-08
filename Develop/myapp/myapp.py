import time
import datetime
from flask import Flask
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import tools
import string



myapp=Flask(__name__,template_folder=r'D:\COVvisualization\COVvisualization\Leading\templates',static_folder=r'D:\COVvisualization\COVvisualization\Leading\js')
myapp.debug=True

@myapp.route('/')
def h_1():
    return render_template('main.html')

@myapp.route('/time')
def get_time():
    return tools.get_time()

@myapp.route('/mid1')
def get_mid1():
    data=tools.get_mid1()
    return {"confirm":str(data[0]),"suspect":str(data[1]),"heal":str(data[2]),"dead":str(data[3])}


@myapp.route('/mid2')
def get_mid2():
    res=[]
    for tup in tools.get_mid2():
        res.append({"name":tup[0],"value":int(tup[1])})
    return {"data":res}
@myapp.route('/left1')
def get_left1():
    data=tools.get_left1()
    day,confirm,suspect,heal,dead=[],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return {"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead}
@myapp.route('/left2')
def get_left2():
    data=tools.get_left2()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return {"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add}

@myapp.route('/right1')
def get_right1():
    data=tools.get_right1()
    city,confirm=[],[]
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return {"city":city,"confirm":confirm}
@myapp.route('/right2')
def get_right2():
    data=tools.get_right2()
    d=[]
    for i in data:
        k=i[0].rstrip(string.digits)
        v=i[0][len(k)]
        ks=extract_tags(k) #jieba
        for j in ks:
            if not j.isdigit():
                d.append({"name":j,"value":v})
    return {"kws":d}
if __name__ == '__main__':
    myapp.run()