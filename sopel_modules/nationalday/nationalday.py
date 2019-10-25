from sopel.module import commands, example
from sopel import web

import sopel.module
import socket

import datetime
import mechanize


def nationalday_lookup(bot, nick, url, day):
    day_str = day.strftime("%B %d, %Y")
    br = mechanize.Browser()
    br.open("https://nationaldaycalendar.com/what-is-today/")
    links = [x for x in br.links() if x.text[0:16] == day_str]
    if len(links) == 1:
        link = links[0]
        bot.say(f"{link.text} - {link.url}")
    elif len(links) == 0:
        bot.say(f"{nick} found no results for {url} -- {day}")
    else:
        bot.say(f"{nick} found too many results for {url} -- {day}")


@sopel.module.commands('today')
@sopel.module.example('.today')
def nationalday_today(bot, trigger):
    return nationalday_lookup(bot, trigger.nick, "https://nationaldaycalendar.com/what-is-today/", datetime.date.today())

#TODO: this is more complicated to parse
#@sopel.module.commands('tomorrow')
#@sopel.module.example('.tomorrow')
#def nationalday_tomorrow(bot, trigger):
#    return nationalday_lookup(bot, trigger.nick, "https://nationaldaycalendar.com/tomorrow/", datetime.date.today() + datetime.timedelta(days=1))
