import werkzeug
import sys
werkzeug.cached_property = werkzeug.utils.cached_property
import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
def getattendance(rollnumber,password):
    # print("hii")
    br = RoboBrowser(history=False, parser='html.parser')
    url = 'http://erp.iitbbs.ac.in'
    response = br.open(url)
    # print(response)
    form = br.get_form(action='login.php')
    form['email'].value = rollnumber
    form['password'].value = password
    br.submit_form(form)
    # print(br)
    s = str(br.url)
    s =s.strip()
    # print(s)
    t="https://erp.iitbbs.ac.in/home.php"
    # print(t ,s)
    if s !=t:
        print("wrong credentials")
        return
    br.open("https://erp.iitbbs.ac.in/biometric/list_students.php")

    soup = BeautifulSoup(br.response.text, 'html.parser')
    # content = soup.find('div', attrs={'id': 'content'})
    # table = content.find('table')
    # print(table)
    table = soup.find_all("td")
    # print(table.get)
    # print(soup.get_text())
    # print(table)
    table = table[3:]
    attend =[]
    # print(len(table))
    l = len(table)
    for i in range(0,l,5):
        # print(i,i+4)
        a =[]
        a.append(table[i].get_text().strip())
        a.append(table[i+1].get_text().strip())
        a.append(table[i+2].get_text().strip())
        a.append(table[i+3].get_text().strip())
        a.append(table[i+4].get_text().strip())
        attend.append(a)
        # i =i+4
    i = 1
    print("-"*103)
    # print("-"*86)
    print("|",end="")
    print("{:<6}".format("S.No"),end="")
    print("|",end="")
    print("{:<13}".format("Subject Code"),end="")
    print("|",end="")
    print("{:<50}".format("Subject Name"),end="")
    print("|",end="")
    print("{:<11}".format("attended"),end="")
    print("|",end="")
    print("{:<11}".format("conducted"),end="")
    print("|",end="")
    print("{:<5}".format("%"),end="")
    print("|\n",end="")
    print("-"*103)
    for t in attend:
        # print(t)
        print("|",end="")
        print("{:<6}".format(i),end="")
        print("|",end="")
        print("{:<13}".format(t[0]),end="")
        print("|",end="")
        print("{:<50}".format(t[1]),end="")
        print("|",end="")
        print("{:<11}".format(t[2]),end="")
        print("|",end="")
        print("{:<11}".format(t[3]),end="")
        print("|",end="")
        print("{:<5}".format(t[4]),end="")
        print("|\n",end="")
        i = i+1
    print("-"*103)


if __name__ == "__main__":
    # print("hello")
    # print(sys.argv[1])
    # if(len(sys.argv))
    if str(sys.argv[1]) == "help" or str(sys.argv[1]) == "--help" or str(sys.argv[1]) == "--help" :
        print("enter  your username and password in this format : python attendance.py username password")
    else:
        user = str(sys.argv[1])
        paswd = str(sys.argv[2])
        getattendance(user,paswd)