import os
import base64

from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

from pycasso import Canvas


def create_app():
    app = Flask(__name__, template_folder='template', static_folder='static')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/ok', methods=['GET'])
    def ok():
        return 'computer'

    @app.route('/api', methods=['GET', 'POST'])
    def api():
        if request.method == 'POST':
            img_data = request.files['img_data']
            input = base64.b64encode(img_data.read()).decode()

            img_compare = request.form.get('img_compare')

            img_slice_width = int(request.form.get('img_slice_width'))
            img_slice_height = int(request.form.get('img_slice_height'))

            img_seed = request.form.get('img_seed')
            img_mode = request.form.get('img_mode')
            img_format = request.form.get('img_format')

            filename = secure_filename(img_data.filename)
            base_filename, input_ext = os.path.splitext(filename)
            input_ext = input_ext.split(".")[1]

            img = Canvas(
                img=img_data,
                slice_size=(img_slice_width, img_slice_height),
                seed=img_seed
            ).export(
                mode=img_mode,
                format=img_format
            )

            if img_compare:
                output = base64.b64encode(img.getvalue()).decode()
                return render_template(
                    'index.html',
                    input_img=input,
                    output_img=output,
                    input_ext=input_ext,
                    output_ext=img_format
                )
            else:
                img.seek(0)
                return get_image(img_format, img)

    return app


def get_image(img_format, output):
    return send_file(output, mimetype=f"image/{img_format}")


if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
