import csv

from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

# we can delete all the routes below and parametrise the page name as follow:
#@app.route('/contact')
#def contact():
   #return render_template('contact.html')

#@app.route('/about')
#def about():
   #return render_template('about.html')
@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)

# let's write a function to inputs data to our database text file

def write_to_file(data):
   with open("database.txt", mode="a") as database:
      email= data["email"]
      subject = data["subject"]
      message = data["message"]
      file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
   with open('database.csv', newline='', mode='a') as database2:
      email= data["email"]
      subject = data["subject"]
      message = data["message"]
      csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
   if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
      except:
        return "data did not save!"
   else:
      return "Ops, something went wrong! Please try again!"

