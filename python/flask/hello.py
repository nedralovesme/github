from flask import Flask
app = Flask("MyApp")

@app.route("/")
def hello():
    return "<h1>Hello, world</h1>"

# rule      = "/"
# view_func = hello
# # they go as arguments here in 'flask/app.py'
# def add_url_rule(self, rule, endpoint=None, view_func=None, **options):
#     pass


if __name__=="__main__":
    app.run(debug=True)
