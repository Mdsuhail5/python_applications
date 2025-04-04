from flask import Flask

app = Flask("__main__")


@make_bold
def bold():
    return f'<b>{bye}<b>'


@make_emphasis
def emphasis():
    pass


@make_underlined
def underlined():
    pass


@app.route("/bye")
@make_bold
def bye():
    return 'Bye!'


if __name__ == "__main__":
    app.run(debug=True)
