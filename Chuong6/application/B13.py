from flask import request, Flask


app = Flask(__name__) 

@app.route('/upload', methods=['GET', 'POST'] )

def upload_file():

    if request.method == 'POST':

        f = request.files['the_file']

        f.save('uploaded_file.txt')
    

if __name__ == "__main__":
    app.run()
