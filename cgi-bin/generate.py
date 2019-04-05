#!/usr/bin/python3.6
import cgi, os
import cgitb; cgitb.enable()
import traceback


form = cgi.FieldStorage()
# Get filename here.
fileitem1 = form['filename1']

#Test if the file was uploaded
if fileitem1.filename:
   try:
       import md
       html,table = md.generate_tuplepage(fileitem1)
       # fileitem3.file.seek(0)
       # md.upload_table(tablen,fileitem3)

       # message = "<p><font size=\"6\"><b>Your table has been successfully uploaded!</b></font></p>"
       # message = message + "<p>To load your new table, enter your new table's name and click load.</p>"
       # message = message + "<p><strong>Note:</strong> Save your old table before loading your new table or the data will be lost.</p>"
       # message = message + "<p>Below is a preview of one tuple pair page:</p>"
       message = """
       <div class="panel panel-info">
           <div class="panel-heading"> You have successully uploaded the table!

               <div class="clearfix"></div>
           </div>
           <div class="panel-body">
             <form enctype = "multipart/form-data"
                               action = "/cgi-bin/generate2.py" method = "post">
             <div>

       """

       message += html
       message += """             <p><input type = "submit" value = "Continue" /></p>
                    </form>
                  </div>
              </div>
              <style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Table Preview</h2>

<table>"""
       message +=  table
       message +=   """</table> """
   except Exception as e:

       message = "<p><font size=\"6\"><b>An error has occured!</b></font></p>"
       message = message + "<p>Please check your csv files according to the error message!</p>"
       message = message + "<p>Key Word for the error is: " + str(e) + "</p>"
       message = message + "<p>Detailed traceback: </p><p>" + traceback.format_exc() + "</p>"

else:
   message = 'Please choose three CSV files'


print ("""\
Content-Type: text/html\n
<html>
   <p>%s</p>
</html>
""" % (message))
