# -*- coding: UTF-8 -*-
import smtplib  
from email.mime.text import MIMEText  

mailto_list=['wuzhuqing123@outlook.com'] #收件地址
mail_host="10.100.1.33"  #设置服务器
mail_user="admin"    #用户名
mail_pass="admin"   #口令 
mail_postfix="miantiao.me"  #发件箱的后缀

def send_mail(to_list,sub,content):  
    me="Haraka"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='utf-8')
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print str(e)  
        return False  
if __name__ == '__main__':
    for mail in mailto_list:
        if send_mail([mail],"测试邮件的标题","""这是测试邮件"""):
            print "发送成功"
        else:
            print "发送失败"
