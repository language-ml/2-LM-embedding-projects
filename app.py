# Author: Moein Salimi

import random
from flask import Flask, render_template, request

app = Flask(__name__)

def autocomplete(sentence):
    # this function is related to Problem 2.
    # 'sentence' is input arg and output should be completed version of sentence.
    # you should call your function in line 13 and return it line 14.
    chrs = 'ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی'
    return sentence + ''.join(random.choices(chrs, k=3))


def convert_formal2informal(sentence):
    # this function is related to Problem 1.
    # 'sentence' is input arg and output should be formal version of sentence.
    # you should call your function in line 21 and return result.
    return "خروجی به صورت استرینگ بازگشت داده شود"


@app.route('/informal_text_to_formal', methods=['GET', 'POST'])
def informal_text_to_formal():
    sentence = request.form['text2']
    if not sentence:
        sentence = "متنی در ورودی وارد نکرده‌اید!"
    else:
        sentence = convert_formal2informal(sentence)
    return render_template("index.html", formal_text=sentence)

@app.route('/complete_current_word', methods=['GET', 'POST'])
def complete_current_word():
    old_sentence = request.form['text1']
    if not old_sentence:
        sentence = "متنی در ورودی وارد نکرده‌اید!"
    else:
        sentence = autocomplete(old_sentence)
    return render_template("index.html", old_sentence=old_sentence, completed_sentence=sentence)

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=9595)