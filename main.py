# https://phrase.com/blog/posts/i18n-advantages-babel-python/
# https://phrase.com/blog/posts/translate-python-gnu-gettext/
# http://oz123.github.io/writings/2013-08-04-Localizing-with-gettext/index.html
# https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/
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
#print(new_lang.__dir__())
print(new_lang._info)
print(gettext.find('base', 'locale'))

print(gettext.gettext('This is a translatable string.'))
print(_('This is a translatable string.'))
