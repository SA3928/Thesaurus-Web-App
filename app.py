from flask import Flask, render_template, url_for, request, redirect, flash
from submitform import input_form
from findword import wordsearch

app=Flask(__name__)

app.config['SECRET_KEY'] = 'e94f3b6383f1a6a03ffcc8a397011fad'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search", methods=['POST','GET'])
def search():
    form=input_form()
    thesaurus = wordsearch(r"C:\Users\srija\AppData\Local\Programs\Python\Python38\venv1\Scripts\first_app\thesaurus_data.json")

    if form.validate_on_submit() :
        meaning = thesaurus.search(form.word.data)
        if type(meaning) != str :
            outp=""
            for i in meaning:
                outp=outp+"\n\n\n"+i
        else:
            outp=meaning
        return render_template("output.html",title="Meaning",final_meaning=outp)
    return render_template("search.html", title="Search", form=form)



app.run(debug=True)