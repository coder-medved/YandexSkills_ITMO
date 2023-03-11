message = \
    """
    Вопрос:
    Как подать заявку на получение справки/документа о предыдущем образовании?
    
    Ответ:
    Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
    """

tts = \
    """
    Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
    """

buttons = [
    "Назад",
    "Выйти",
    "Помощь"
]

card = {
    'type': 'BigImage',
    'image_id': '937455/40f0536e426907808499',
    'title': 'СПРАВКА/ДОКУМЕНТ О ПРЕДЫДУЩЕМ ОБРАЗОВАНИИ',
    'description': \
        """
        Вопрос:
        Как подать заявку на получение справки/документа о предыдущем образовании?
        Ответ:
        Вам необходимо перейти на портал ИСУ, а дальше все просто! Подайте заявку через ту форму, которую предлагает система.
        """
}

session_state = {
    "branch": "studentOffice"
}


def getConfig():
    return {
        'message': message,
        'tts': tts,
        'buttons': buttons,
        'card': card,
        'session_state': session_state
    }
