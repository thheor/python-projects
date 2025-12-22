import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def getFunFact(_):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.get(url)
    data = json.loads(response.text)
    uselessFact = data['text']

    style(put_text(uselessFact), 'color: blue; font-size: 30px')

if __name__ == '__main__':
    put_html(
        '<p align="left">'
        '<h2><img src="https://avatars.githubusercontent.com/u/245702024?v=4" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    put_buttons(
        [dict(label = 'Click me', value = 'clicked', color = 'success')],
        onclick = getFunFact
    )
    hold()