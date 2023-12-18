from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'Ksh. 300,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Mombasa, Kenya',
    'salary': 'Ksh. 600,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Kisumu, Kenya',
    'salary': 'Ksh. 450,000'
  }
]



@app.route('/')
def hello_denmal():
  return render_template('home.html',jobs=JOBS,company_name='Denmal')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)