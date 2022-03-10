def hellopython(requests):
    request_args = requests.args
    request_json = requests.get_json(silent=True)
    if request_args and "fname" in request_args and "lname" in request_args:
        fname = request_args["fname"]
        lname = request_args["lname"]
    elif request_json and "fname" in request_json and "lname" in request_json:
        fname = request_json["fname"]
        lname = request_json["lname"]
    else:
        fname = "Rohith"
        lname = "P"
    return f"hello{fname} for {lname}"
