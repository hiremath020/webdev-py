from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'bangalore',
        'salary': 'Rs 1,50,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi',
        'salary': 'Rs 15,50,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'remort',
        'salary': 'Rs 12,50,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'remort',
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Jovian')
 
@app.route("/jobs")
def list_jobs( ):
    return jsonify(JOBS)   



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
