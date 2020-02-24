# code:utf-8
from flask import Flask, redirect, url_for, session, request, send_from_directory, abort, make_response
import json, os, hashlib, time
from flask_uploads import UploadSet, configure_uploads, ALL, patch_request_class

# from osdef import isHavefile

app = Flask(__name__)
Version = "0.0.1b"
app.config["SECRET_KEY"] = "renyizifuchuan"
prpath = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOADED_EXCHANGE_DEST'] = "E:/UnitAi-Project/Newserver/upload"
exchangeupload = UploadSet('exchange', ALL)
configure_uploads(app, exchangeupload)
patch_request_class(app)
porject_path = os.getcwd()


def hash(word):
    sha256 = hashlib.sha256()
    sha256.update(str(word).encode('utf-8'))
    res = sha256.hexdigest()
    return res


def exchangefile(rec):
    print(rec)
    if rec != None:
        name = rec["filename"]
        print(rec["filename"])
        path = prpath + "/download/exchange/" + rec["filename"]
        if os.path.isfile(path):
            # print("Ok")
            path = prpath.replace("\\", "/") + "/download/exchange"
            print(path)
        response = send_from_directory(path, name, as_attachment=True)
        return response
    # else:
    # return abort(301)


@app.route('/login', methods=['POST'])
def login():
    # user = request.form['nm']
    # data = json.loads(request.get_data(as_text=True))
    # print(data)
    print(request.json)
    rec = request.json
    user = rec["acc"]
    print(user)
    # print(type(request.headers))
    # access=hash(user+str(time.time()))
    access = hash(user + "123")  # TODO: Test use
    session[user] = access
    # session["name"] = "python"
    # name = session.get("name")
    # print(name)
    return {
        'code': '0',
        'access-token': access

    }


@app.route('/logincheck', methods=['POST'])
def logincheck():
    rec = request.json
    user = rec["acc"]
    # print(user)
    # name = session.get(user)
    # print(name)
    if rec["access"] == session.get(user):
        return {
            "code": "0"
        }
    else:
        return abort(401)


@app.route('/test/<filename>', methods=['GET'])
def test(filename):
    path = prpath.replace("\\", "/") + "/download/exchange"
    response = make_response(
        send_from_directory(path, filename, as_attachment=True))
    return response
    # return send_from_directory(path, name, as_attachment=True)


# return send_from_directory( "E:/UnitAi-Project/Newserver/download/exchange", "1.ppt", as_attachment=True)

@app.route('/ConnectTest', methods=['GET'])
def ConnectTest():
    return {
        "Version": Version
    }


@app.route('/download/<type>', methods=['POST'])
def download(type):
    print(type)
    if type == "exchange":
        return exchangefile(request.json)
    # else:
    # abort(404)


@app.route('/upload/exchange', methods=['POST'])
def upload():
    if request.files != None:
        print(request.files)
        filename_past = exchangeupload.save(request.files["ex"])
        print(filename_past)
        result = request.form.to_dict()
        print(type(result))
        if "filename" in result.keys():
            filename = result["filename"]
            print(filename)
            path = porject_path + "/upload/" + filename
            if os.path.exists(path):
                os.remove(path)
            os.rename(porject_path + "/upload/" + filename_past, path)
            if "order" in result.keys():
                order = 1
            else:
                order = 0
            if "md5" in result.keys() and (os.path.getsize(path) <= 102400 or order == 1):
                f = open(path, 'rb')
                myHash = hashlib.md5()
                while True:
                    d = f.read(8096)
                    if not d:
                        break
                    myHash.update(d)
                md5 = myHash.hexdigest()
                f.close()
                if md5 != result["md5"]:
                    return abort(400)
            return {"code": "0"}
    else:
        abort(401)
    # file_url = exchangeupload.url(filename)


if __name__ == '__main__':
    app.run(port=19150)
