import gettext
import os
import app

path_to_localedir = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '../locale'
))

translater = gettext.translation(
    'messages',
    localedir=path_to_localedir,
    languages=['ja_JP'],
    fallback=True
)

translater.install()
app.main()
