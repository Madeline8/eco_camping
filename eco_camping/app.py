import os

@app.errorhandler(404)
def not_found(e):
    """
    404 error handling page
    """
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    """
    500 error handling page
    thanks to Flask Documentation (credited in README)
    """
    return render_template("500.html"), 500
