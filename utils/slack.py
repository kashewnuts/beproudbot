import slacker
from slackbot import settings


def get_user_name(user_id):
    """指定された Slack の user_id に対応する username を返す

    Slacker で users.list API を呼び出す
    - https://github.com/os/slacker
    - https://api.slack.com/methods/users.info

    :prams str user_id: SlackのユーザーID
    :return str: Slackのユーザー名
    """
    webapi = slacker.Slacker(settings.API_TOKEN)
    response = webapi.users.info(user_id)
    if response.body['ok']:
        return response.body['user']['name']
    else:
        return ''
