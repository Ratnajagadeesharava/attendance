import werkzeug
import sys
werkzeug.cached_property = werkzeug.utils.cached_property
import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
def getattendance(rollnumber,password):
    br = RoboBrowser(history=False, parser='html.parser')
    url = 'http://erp.iitbbs.ac.in'
    response = br.open(url)
    form = br.get_form(action='login.php')
    form['email'].value = rollnumber
    form['password'].value = password
    br.submit_form(form)
    s = str(br.url)
    s =s.strip()
    t="https://erp.iitbbs.ac.in/home.php"
    if s !=t:
        print("wrong credentials")
        return
    br.open("https://erp.iitbbs.ac.in/biometric/list_students.php")

    soup = BeautifulSoup(br.response.text, 'html.parser')
    table = soup.find_all("td")
    table = table[3:]
    attend =[]
    l = len(table)
    for i in range(0,l,5):
        a =[]
        a.append(table[i].get_text().strip())
        a.append(table[i+1].get_text().strip())
        a.append(table[i+2].get_text().strip())
        a.append(table[i+3].get_text().strip())
        a.append(table[i+4].get_text().strip())
        attend.append(a)
    i = 1
    print("-"*103)
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
    if str(sys.argv[1]) == "help" or str(sys.argv[1]) == "--help" or str(sys.argv[1]) == "--help" :
        print("enter  your username and password in this format : python attendance.py username password")
    else:
        user = str(sys.argv[1])
        paswd = str(sys.argv[2])
        getattendance(user,paswd)
