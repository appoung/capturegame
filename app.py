from flask import Flask,render_template,redirect, request, url_for, jsonify,make_response
import json
app = Flask(__name__)
@app.before_first_request
def chooseRole():
    import choose
    from choose import member,password_list
    global member
    global password_list
    global spy
    spy = choose.chooseRole()
@app.before_first_request
def chooseTeam():
    global teams
    import choose
    teams = choose.chooseTeam(spy)
    teams = json.dumps(teams,ensure_ascii=False)
    teams = make_response(teams)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/post",methods=['POST'])
def post():
    username = request.form['username']
    password = request.form['password']
    return redirect(url_for('checkRole',username=username,password=password))
@app.route("/role/<username>/<password>")
def checkRole(username,password):
    member = ["한병준","임준혁","김동현","정연우","임성준"]
    if username == spy:
        role = "스파이"
    else:
        role = "시민"
    if username not in member:
        return "없는 멤버입니당"
    else:
        if password not in password_list:
            return "비밀번호 틀렸어요"
        else:
            return role
@app.route('/teams/0872')
def teams():
    return teams
if __name__ == '__main__':
    app.run(use_reloader=False,debug=True)  