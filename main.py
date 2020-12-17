# https://phrase.com/blog/posts/i18n-advantages-babel-python/
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
# http://oz123.github.io/writings/2013-08-04-Localizing-with-gettext/index.html
"""
pybabel update -i locale/base.pot -d locale
pybabel compile -d locale

"""

import os
import gettext
localepath = os.path.join(os.getcwd(), "locale")
print(localepath)
new_lang = gettext.translation('base', localedir=localepath, languages=['de'])
new_lang.install()

print(gettext.gettext('This is a translatable string.'))
