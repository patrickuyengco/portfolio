from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


# def write_to_file(data):
#     with open('database.txt', 'a') as txt:
#         email = data['email']
#         subject = data['subject']
#         message = data['message']
#         file_input = f'From: {email}\nSubject: {subject}\nMessage:\n{message}\n\n'
#         txt.write(file_input)


def write_to_csv(data):
    with open('database.csv', 'a') as csvdb:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csvdb, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Data not saved to database.'
    else:
        return 'Something went wrong. Please try again.'
