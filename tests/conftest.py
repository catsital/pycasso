import pytest
import os

from io import BytesIO
from flask import template_rendered

from app import app


@pytest.fixture
def index():
    _app = app.create_app()
    ctx = _app.test_request_context()
    ctx.push()

    _app.config["TESTING"] = True
    _app.testing = True

    yield _app

    ctx.pop()


@pytest.fixture
def client(index):
    client = index.test_client()
    yield client


@pytest.fixture
def loaded_template(index):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, index)

    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, index)


@pytest.fixture
def img(img_path):
    with open(img_path, 'rb') as img_file:
        img_bytes = BytesIO(img_file.read())

    return (img_bytes, 'img_file.png')


@pytest.fixture(scope="session")
def img_path(request):
    return os.path.join(os.path.dirname(__file__), "data/test_image.jpg")


@pytest.fixture(scope="session")
def slice_size(request):
    return (50, 50)


@pytest.fixture(scope="session")
def seed(request):
    return "Pycasso"


@pytest.fixture(scope="class")
def fixtures_class(request, img_path, slice_size, seed):
    class Fixtures:
        def __init__(self):
            self.img_path = img_path
            self.slice_size = slice_size
            self.seed = seed

    request.cls.params = Fixtures()
