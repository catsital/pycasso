def test_index_route(client, loaded_template):
    route = "/"
    request = client.get(route)
    assert request.status_code == 200
    assert len(loaded_template) == 1
    template, context = loaded_template[0]
    assert template.name == "index.html"


def test_api_route(client, img, slice_size, seed):
    route = "/api"

    slice_width, slice_height = slice_size

    response = client.post(
        route,
        content_type='multipart/form-data',
        data={
            'img_data': img,
            'img_slice_width': slice_width,
            'img_slice_height': slice_height,
            'img_seed': seed
        }
    )

    assert response.status_code == 200
