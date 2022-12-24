api_bot_utl = 'https://api.telegram.org/bot{API_KEY}/{method}'
from functools import wraps
import requests

def tg_api_method(func):
    @wraps(func)
    def wrapper(self, **parameters):
        required_parameters = func(self)

        url = api_bot_utl.format(API_KEY = self.API_KEY, method = func.__name__)

        for param in required_parameters:
            if param["required"] == True and param["name"] not in parameters:
                raise Exception('Not Valid parameters. Call method.__doc__')

        responce = requests.get(url, params=parameters)
        return responce.json()
    return wrapper

class TgBot():
    API_KEY = None
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    @tg_api_method
    def sendMessage(self):
        parameters = [
            {
                'name': 'chat_id',
                'type': 'Integer or String',
                'required': True,
                'description': 'Unique identifier for the target chat or username of the target channel (in the format @channelusername)'
            },
            {
                'name': 'text',
                'type': 'String',
                'required': True,
                'description': 'Text of the message to be sent, 1-4096 characters after entities parsing'
            },
            {
                'name': 'parse_mode',
                'type': 'String',
                'required': False,
                'description': 'Mode for parsing entities in the message text. See formatting options for more details.'
            },
            {
                'name': 'message_thread_id',
                'type': 'Integer',
                'required': False,
                'description': 'Unique identifier for the target message thread (topic) of the forum; for forum supergroups only'
            },
            {
                'name': 'entities',
                'type': 'Array of MessageEntity',
                'required': False,
                'description': 'A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode'
            },
            {
                'name': 'disable_web_page_preview',
                'type': 'Boolean',
                'required': False,
                'description': 'Disables link previews for links in this message'
            },
            {
                'name': 'disable_notification',
                'type': 'Boolean',
                'required': False,
                'description': 'Sends the message silently. Users will receive a notification with no sound.'
            },
            {
                'name': 'protect_content',
                'type': 'Boolean',
                'required': False,
                'description': 'Protects the contents of the sent message from forwarding and saving'
            },
            {
                'name': 'reply_to_message_id',
                'type': 'Integer',
                'required': False,
                'description': 'If the message is a reply, ID of the original message'
            },
            {
                'name': 'allow_sending_without_reply',
                'type': 'Boolean',
                'required': False,
                'description': 'Pass True if the message should be sent even if the specified replied-to message is not found'
            },
            {
                'name': 'reply_markup',
                'type': 'InlineKeyboardMarkup or ReplyKeyboardMarkup or ReplyKeyboardRemove or ForceReply',
                'required': False,
                'description': 'Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.'
            },
        ]
        return parameters
