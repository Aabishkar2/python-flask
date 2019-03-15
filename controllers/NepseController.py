from flask import Flask
from flask import jsonify 
from flask import render_template
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

price = 0

def nepseJSON(self=None):
    list_stock = []
    table_head = []
    table_body = []
    tabbb = []
    gethtml = requests.get('https://www.sharesansar.com/today-share-price')
    html = gethtml.text
    bs = BeautifulSoup(html, "lxml")
    table = bs.find('table',{'class':'dataTable'})
    th = table.findAll('th')
    td = table.findAll('td')
    for tab_h in th:
        t_h = tab_h.text.strip()
        table_head.append(t_h)
    for tab_d in td:
        t_d = tab_d.text.strip()
        table_body.append(t_d)
    c_l = len(table_head) #length of table column
    r_l = len(table_body)//c_l #length of table row

    #algorithm to divide rows and column
    a = 0
    b = c_l
    for j in range(0, r_l):
        if j>0:
            a = b
            b = b + c_l
            c = table_body[a:b]
            tabbb.append(c)
        else:
            c = table_body[a:b]
            tabbb.append(c) 
    cf = pd.DataFrame([tabbb[0]],columns=table_head)
    for i in range(1,len(tabbb)):
        a = pd.DataFrame([tabbb[i]],columns=table_head)
        list_stock.append(a)
    for i in list_stock:
        cf = cf.append(i)
    cf.rename(columns={'Company Name': 'company_name'}, inplace=True)
    nepjson = json.loads(cf.to_json(orient='records'))
    return jsonify(nepjson)
    # nepsejson = jsonify(nepjson)
    # return nepsejson
    # return render_template("json.html", nepsejson=nepjson)

