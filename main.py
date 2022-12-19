
from chatterbot import ChatBot
from flask import Flask, request
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask_cors import CORS, cross_origin


app = Flask('__name__')
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
bot = ChatBot('chatterbot', storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')


@app.route('/')
@cross_origin()
def home():
    return str('Welcome to my App')


@app.route('/chat', methods=['POST'])
@cross_origin()
def user():
    json_file = request.json
    data = json_file['msg']
    return str(bot.get_response(data))


app.run()
