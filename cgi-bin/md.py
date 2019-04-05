#!/usr/bin/python3.6
import pandas as pd
from io import StringIO
import datetime

def generate_tuplepage(file1):

    #decode because in python3, stringIO need str not bytes
    io1 = StringIO(file1.file.read().decode("utf-8"))
    A = pd.read_csv(io1)
    headers = list(A)
    html = ""
    cdate  = str(datetime.datetime.now())
    html += """<p>Upload File Name: <input type="text" name="filename1" value="%s" readonly></p>
    <p>Upload Date: <input type="text" name="date" value="%s" readonly></p>
    <p>Please select the column and click continue</p>
    <select name="column" required>
    """ % (file1.filename,cdate)
    for header in headers:
        html += """<option value="%s">%s</option>"""% (header,header)

    html +=  "</select>\n"

    table = "<tr>"
    for header in headers:
        table += """<th>%s</th>"""% (header)
    table += "</tr>"
    # io1.seek(0)
    # html += io1.read()
    count = 30
    for i in A.itertuples():
        first = True
        if count == 0:
            break
        else:
            count -= 1
        table += "<tr>"
        for k in i:
            if first:
                first = False
                continue
            table += "<th>" + str(k) + "</th>"
        table += "</tr>"
    A.to_csv("./data/" + cdate + "ddd" + file1.filename)
    return html, table
