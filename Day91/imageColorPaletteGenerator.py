
from flask import Flask, render_template, request, url_for, flash, abort, redirect
from forms import ImageForm
from color_finder import get_image, get_length, find_top_colors, reshape_colors
from base64 import b64encode
from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ImageForm()
    if request.method=='POST':
        if form.validate_on_submit():
            image_file = request.files.get('image')
            encoded = b64encode(image_file.read()).decode('utf-8')
            mime = "image/jpeg"
            image_uri = f"data:{mime};base64,{encoded}"

            image_array = get_image(image_file)
            image_length = get_length(image_array)

            top_colors = find_top_colors(image_array)
            if top_colors is False:
                flash('Arquivo inválido!')
                return render_template('index.html', form=form)
            ## Reshape the top 10 colors into dictionary of hexcodes
            top_colors = reshape_colors(top_colors, image_length)
            return render_template('result.html', image=image_uri, colors=top_colors)
        else:
            flash('Arquivo inválido, certifique-se de que a imagem é .jpg ou .png!')
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)