#!/usr/bin/python3
import random
import shutil
import requests
import os
from bs4 import BeautifulSoup

def getCode(url,urlsession):
    
    url = str(url)
#    response = urlsession.get(url, stream=True)
#    with open(filename+'.png', 'wb') as out_file:
#        shutil.copyfileobj(response.raw, out_file)
#    del response
    path = str(os.getenv("OPENSHIFT_DATA_DIR")) + 'code.png'
    response = urlsession.get(url, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

def headers(referer):

    headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-TW,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'infosys.nttu.edu.tw',
        'Origin':'https://infosys.nttu.edu.tw',
        'Referer': referer,
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
#        'X-MicrosoftAjax':'Delta=true',
#        'X-Requested-With':'XMLHttpRequest',
        
        }
    return headers

def infosys(s, account, passwd, code):
    
    infosys = "https://infosys.nttu.edu.tw/"
    html = s.get(infosys)

    soup = BeautifulSoup(html.text, 'html.parser')

    __VIEWSTATE = str(soup.find(id='__VIEWSTATE').get('value'))
    __VIEWSTATEGENERATOR = str(soup.find(id ='__VIEWSTATEGENERATOR').get('value'))
    __EVENTVALIDATION = str(soup.find(id='__EVENTVALIDATION').get('value'))


    print("教學意見反映")
#    account = input("學號:")
#    passwd = input("密碼：")
#    code = input("驗證碼:")

    data = {
    '__LASTFOCUS':'',
    '__VIEWSTATE':__VIEWSTATE,
    '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':'',
    '__EVENTVALIDATION':__EVENTVALIDATION,
    'txtUserName':account,
    'txtPassword':passwd,
    'ddlSolution':'sln_CourseBase',
    'tbCheckCode':code,
    'OKButton.x':'35',
    'OKButton.y':'9',
    'hfOValue':'',
    'hfNValue':'',
    'ddlDataBase':'NTTU_TEST',

    }
    html = s.post(infosys,data=data)

    soup = BeautifulSoup(html.text, 'html.parser')
    logined = str(soup.find(id='btnChangepassword'))
    if logined != 'None':
        print("登入成功！")
    else:
        print("登入失敗！")

    questions = "https://infosys.nttu.edu.tw/n_CourseBase_Question/StudQuestion.aspx?ItemParam="
    html = s.get(questions)
    #print(html.text)


    soup = BeautifulSoup(html.text, 'html.parser')
    __VIEWSTATE = str(soup.find(id='__VIEWSTATE').get('value'))
    __VIEWSTATEGENERATOR = str(soup.find(id ='__VIEWSTATEGENERATOR').get('value'))
    __EVENTVALIDATION = str(soup.find(id='__EVENTVALIDATION').get('value'))



    lists = soup.findAll('tr', attrs={'class','NTTU_GridView_Row'})
    
    output_message = ""
    for i in lists:
        
        #output_message += "<tr><td>"+i.find_all('td')[3].text +"</td><td>"+ i.find_all('td')[5].text+"</td></tr>"
        output_message += "<tr><td>"+i.find_all('td')[5].text+"&nbsp;&nbsp;&nbsp;&nbsp;</td><td>"+ i.find_all('td')[3].text+"</td></tr>"
        print(i.find_all('td')[3].text, i.find_all('td')[5].text)
        num = "UpdatePanel2|"+i.find_all('input')[0].get('name')
        num2 = i.find_all('input')[0].get('name')
        data1 = {
        #'ToolkitScriptManager1':'UpdatePanel2|GridView2$ctl02$Button1',
        'ToolkitScriptManager1':num,
        'ToolkitScriptManager1_HiddenField':'',
        'DropDownList1':'1042',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__LASTFOCUS':'',
        '__VIEWSTATE':__VIEWSTATE,
        '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
        '__SCROLLPOSITIONX':'0',
        '__SCROLLPOSITIONY':'0',
        '__EVENTVALIDATION':__EVENTVALIDATION,
        '__VIEWSTATEENCRYPTED':'',
        '__ASYNCPOST':'true0',
        num2:'作答',

        }

        html = s.post(questions,data=data1,headers=headers(questions))
        #print(html.text)
        #xd = input("Y/N")
        soup = BeautifulSoup(html.text, 'html.parser')
        __VIEWSTATE = str(soup.find(id='__VIEWSTATE').get('value'))
        __VIEWSTATEGENERATOR = str(soup.find(id ='__VIEWSTATEGENERATOR').get('value'))
        __EVENTVALIDATION = str(soup.find(id='__EVENTVALIDATION').get('value'))




        data2 = {
        'ToolkitScriptManager1':'UpdatePanel1|Button1',
        'ToolkitScriptManager1_HiddenField':'',
        'DropDownList1':'1042',
        'RadioButtonList1':'3',
        'RadioButtonList2':'1',
        'RadioButtonList3':'1',
        'GridView1$ctl02$RadioButtonList5':'5',
        'GridView1$ctl03$RadioButtonList5':'4',
        'GridView1$ctl04$RadioButtonList5':'5',
        'GridView1$ctl05$RadioButtonList5':'4',
        'GridView1$ctl06$RadioButtonList5':'5',
        'GridView1$ctl07$RadioButtonList5':'4',
        'GridView1$ctl08$RadioButtonList5':'5',
        'GridView1$ctl09$RadioButtonList5':'4',
        'GridView1$ctl10$RadioButtonList5':'5',
        'GridView1$ctl11$RadioButtonList5':'4',
        'RadioButtonList6':'3',
        'TextBox1':'',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__LASTFOCUS':'',
        '__VIEWSTATE':__VIEWSTATE,
        '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
        '__SCROLLPOSITIONX':'0',
        '__SCROLLPOSITIONY':'0',
        '__EVENTVALIDATION':__EVENTVALIDATION,
        '__VIEWSTATEENCRYPTED':'',
        '__ASYNCPOST':'true',
        'Button1':'完成送出問卷',
        }
        test = {
        'ToolkitScriptManager1':'UpdatePanel1|Button2',
        'ToolkitScriptManager1_HiddenField':'',
        'DropDownList1':'1042',
        'RadioButtonList1':'3',
        'RadioButtonList2':'1',
        'RadioButtonList3':'1',
        'GridView1$ctl02$RadioButtonList5':'5',
        'GridView1$ctl03$RadioButtonList5':'4',
        'GridView1$ctl04$RadioButtonList5':'5',
        'GridView1$ctl05$RadioButtonList5':'4',
        'GridView1$ctl06$RadioButtonList5':'5',
        'GridView1$ctl07$RadioButtonList5':'4',
        'GridView1$ctl08$RadioButtonList5':'5',
        'GridView1$ctl09$RadioButtonList5':'4',
        'GridView1$ctl10$RadioButtonList5':'5',
        'GridView1$ctl11$RadioButtonList5':'4',
        'RadioButtonList6':'3',
        'TextBox1':'自動填單',
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__LASTFOCUS':'',
        '__VIEWSTATE':__VIEWSTATE,
        '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
        '__SCROLLPOSITIONX':'0',
        '__SCROLLPOSITIONY':'0',
        '__EVENTVALIDATION':__EVENTVALIDATION,
        '__VIEWSTATEENCRYPTED':'',
        '__ASYNCPOST':'true',
        'Button2':'暫時儲存',
        }


        html = s.post(questions,data=data2,headers=headers(questions))
        #print(html.text)
        print("填寫完畢")
   
    logout = infosys + "webClientMain.aspx" 
    html = s.get(logout)
    #print(html.text)


    soup = BeautifulSoup(html.text, 'html.parser')
    __VIEWSTATE = str(soup.find(id='__VIEWSTATE').get('value'))
    __VIEWSTATEGENERATOR = str(soup.find(id ='__VIEWSTATEGENERATOR').get('value'))
    __EVENTVALIDATION = str(soup.find(id='__EVENTVALIDATION').get('value'))



    logoutdata = {
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__LASTFOCUS':'',
            'tView_ExpandState':'',
            'tView_SelectedNode':'',
            'tView_PopulateLog':'',
            '__VIEWSTATE':__VIEWSTATE,
            '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
            '__EVENTVALIDATION':__EVENTVALIDATION,
            'btnLogOut':'登出',
            'tbCaption':'',
            'ddlSolution':'sln_CourseBase',
    }

    html = s.post(logout, data=logoutdata, headers=headers(infosys))
    #print("out",html.text) 

    return output_message 

