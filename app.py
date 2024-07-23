from flask import Flask, jsonify

app = Flask(__name__)

widget = {
  "type": "scaffold",
  "args": {
    "appBar": {
      "type": "app_bar",
      "args": {
        "title": {
          "type": "text",
          "args": {
            "text": "Dynamic Widget"
          }
        }
      }
    },
    "body": {
      "type": "center",
      "child": {
        "type": "text",
        "args": {
          "text": "This is a very important message!"
        }
      }
    }
  }
}

@app.route('/mainpage', methods=['GET'])
def get_mainpage():
  return jsonify(widget)

if __name__ == '__main__':
  app.run(debug=True)
