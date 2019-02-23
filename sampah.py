@app.route('/hikmat')
def hikmat():
    return ("waduh", "gitu")

@app.route('/summation/<firstNum>/<secondNum>')
def summation(firstNum, secondNum):
    firstNum = int(firstNum)
    secondNum = int(secondNum)
    result = firstNum + secondNum
    # saya yang bernama xxx mempunyai nilai yyy
    return str(result)

@app.route('/summation')
def summation2():
    firstNum = request.args.get('firstNum')
    secondNum = request.args.get('secondNum')
    result = firstNum + secondNum
    
    return str(result)

@app.route('/')
def home():
    return "Mobil baru"


historyUser = []

@app.route('/codewars/history')
def getSearchHistory():
    historyFile = open("history-user", 'r') 
    return historyFile.read()

@app.route('/codewars/<username>')
def getUserInfo(username):
    historyFile = open("history-user", "a")
    historyFile.write(username)
    
    historyUser.append(username)

    data = requests.get("https://www.codewars.com/api/v1/users/%s" % username)
    theName = data.json()["name"]
    theHonor = data.json()["honor"]

    result = "saya yang bernama %s mempunyai nilai %s" % (theName, theHonor)
    return result

@app.route('/questions/<questionNumber>')
def getQuestion(questionNumber):
    questionFile = open('./question-file.json')
    questionData = json.load(questionFile)
    print(type(questionData))

    for question in questionData["questions"]:
        # loads itu, dari string ke json
        # dumps itu, dari singlequotes ke doublequotes
        question = json.loads(question)
        if question["question-number"] == int(questionNumber):
            return str(question)

    return "gaketemu soalnya"


# ```
# 1. ngebaca dokumentasi api codewars
# 2. nyobain si api di insomnia/postman
# 3. nginstall si `requests` di si flask
# 4. kita pake si `requests` buat minta data dari api codewars
# 5. si yang 4, kita mintanya di rute tertentu. bentuknya dinamis karena pake <params>
# 6. kita bikin string dari beberapa data dari response api-nya codewars
# ====iklan: nyobain port random, sama ip 0.0.0.0, via `app.run()`
# 7. kita nyobain bikin variabel dan membuktikan itu temporary alias ilang pas servernya di restart: e.g. nyimpen di array
# 8. supaya ga ilang, kita nyoba simpen di sebuah file
# 9. baca filenya
# 10. segitu
# ```

# ```
# 1. kita nyobain POST
# ```

@app.route('/ngebuktiin', methods=['POST'])
def ngebuktiin():
    body = request.json
    print(body)
    print(json.dumps(body))

    return "beres"


# ```
# 1. Pertama, kita bikin grup nya
#     caranya mirip sama yang question
# 2. bagian add question, yang bawah itu 
# ```


@app.route('/<anything>')
def anythingHandler(anything):
    abort(404)

@app.errorhandler(404)
def errorNih(error):
    return "ga ada"


data = []

@app.route('/cobain/<data>')
def cobainRender(data):
    return render_template('index.html', beybeh = data)

@app.route('/', methods=["POST"])
def tryAja():
    body = request.json
    data.append(body["name"])

    return jsonify(data)
        # if body["todo"] == "encrypt":
        #     return encrypt(body["data"])
        # elif body["todo"] == "decrypt":
        #     return decrypt(body["data"])

@app.route('/<name>', methods=["DELETE", "PUT"])
def modifyData(name):
    body = request.json

    if request.method == "DELETE":        
        data.remove(name)
    elif request.method == "PUT":
        index = data.index(name)
        data[index] = body["new-name"]

    return jsonify(data)

def encrypt(string):
    return string + "encrypted"

def decrypt(string):
    return string + "decrypted"

# delete quis sama edit informasi tentang kuisnya
# @app.route('/quizzes/<quizId>', methods=["PUT", "DELETE"])
