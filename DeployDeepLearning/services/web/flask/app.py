from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from waitress import serve

import os
import model

flask_app = Flask(__name__, template_folder='Template')
Bootstrap(flask_app)

"""
Routes
"""
@flask_app.route('/', methods=['GET','POST'])
def predict():
    static_image = os.path.join('static', 'index.png')
    static_result = {
        'image_path':static_image
    }
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = model.get_prediction(image_path)
            result = {
                'class_name': class_name,
                'image_path': image_path,
            }
            return render_template('result.html', result = result)
    return render_template('index.html', result = static_result)

#if __name__ == '__main__':
#    flask_app.run(debug = True, port=8501)
#    serve(flask_app, host='0.0.0.0', port =5001)