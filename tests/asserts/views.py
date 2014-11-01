def assert_redirects(response, location, base_url='http://localhost'):
    """
    Check if response is an HTTP redirect to the given location.

    :param response: Flask response
    :param location: relative URL (i.e. without **http://localhost**)
    """
    assert response.status_code in (301, 302)
    assert response.location == base_url + location
