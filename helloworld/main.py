def hello_world(request):

    # Pre-flight request for CORS
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*', # access from specific domains or * for all domains
            'Access-Control-Allow-Methods': 'POST', # access via any method '*'
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600' # remember headers for 1hr (3600 secs) for future requests
        }
        return '', 204, headers
        # 204 status means No Content
    
    # Set headers for CORS
    headers = {
        'Access-Control-Allow-Origin': '*'
    }


    # returns a dictionary or none
    request_args = request.args

    # silen= True sents the var to none, if no json object is present
    request_json = request.get_json(silent=True)


    if request_args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'World'
        lastname = ''

    return f'Hello {name} {lastname}', 200, headers
    # 200 status code for OK
