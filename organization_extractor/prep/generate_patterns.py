# -*- coding: utf-8 -*-
from os.path import dirname, realpath
from os import listdir
import re, pickle
directory_of_this_file = dirname(realpath(__file__))
directory_of_keywords = directory_of_this_file + "/keywords"
directory_of_patterns = directory_of_this_file + "/patterns"

# load keywords from files into dictionary
language_keyword_pattern = {}
for filename in listdir(directory_of_keywords):
    language = filename.split(".")[0]
    print "language is", language

    path_to_keywords_file = directory_of_keywords + "/" + filename

    with open(path_to_keywords_file) as f:
        keywords = f.read().decode("utf-8").splitlines()

        # sort keywords by length, because we want to match the longest ones first
        # wouldn't want to accidentaly match Institute instead of Institutes
        keywords = sorted(keywords, key=lambda x: -1*len(x))

    pattern = u"(?:" + u"|".join(keywords) + u")"
    language_keyword_pattern[language] = pattern


language_org_pattern = {}
#######################################################
##########################       English
################################################
keyword = language_keyword_pattern['English']
citation = u"(?: ?\[\d{1,3}\] ?)*"
seperator = u"(?:, |,|\u200E|\u200E | \u200E| \u200E | or |;|; ){1,3}"
# accept a as uppercase because sometimes used in acronymns such as Jash al-... Ja...
#upper = u"[^\W\d_b-z:]"
# make sure upper case for English chars only and not Arabic
upper = u"[^\W\d_b-z:\u0621-\u06ff]"
lower = u"(?:[^\W\d_A-Z:\u0621-\u06ff]|')"
acronym = upper + u'{2,}'
titled = u"(?:\d+(?:st|nd|th)[ ])?(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?" + upper + lower + "{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?"+upper+lower+"{2,})*"
alias = u"(?:(?:"+upper+lower+"{3,}: ?|meaning\")?" + "("+titled+")" + "|" + '('+acronym+')' +  ")"
name = u"((?:"+titled+" )*" + keyword + "(?: "+titled+")*)" + citation
aliases = "(?: ?\(" + alias + "(?: ?" + seperator + alias + ")*" + ")*"
org = name + "(?: or " + name + ")?" + aliases

# make sure doesn't start with flag, of, or lowercase character
org = "(?!(?:About|After|Although|Coat|Current|Emblem|List|Flag|Hundreds|Logo|Millions|of|Politics|Thousands|[a-z]))" + org

# make sure doesn't end with ...
org = org + "(?<!(?:Logo|Flag|also| and))(?<!(?:als|[a-z]ly|[a-z]e[d|s]))"

language_org_pattern['English'] = org




###########################################
###########            ARABIC
##########################################
keyword = language_keyword_pattern['Arabic']
print "keyword is", keyword
# \u0648 is waw and used to match when the name is like group of the thing and the other thing thing
# it will also incidentally match group and the person, but we'll have to see if this construct is actually an issue
#pattern = u"(?:" + keyword + u"(?: (?:(?:\u0648?\u0627\u0644[^ .,\u060c\n\r<\";]*)|\u0641\u064a|(?:\u0628[^ .,\u060c\n\r<\"\u200e;]*)))+)"

# the negative look behind at the end makes sure it doesn't end in fee
pattern = u"(?:" + keyword + u"(?: (?:(?:\u0648?\u0627\u0644[^)( .,\u060c\n\r<\";\u200e]*)|\u0641\u064a|(?:\u0628[^)( .,\u060c\n\r<\"\u200e;]*)))+)(?<!\u0641\u064a)"
language_org_pattern['Arabic'] = pattern


# write all patterns to their respective files
for language, pattern in language_org_pattern.iteritems():
    with open(directory_of_patterns + "/" + language + ".txt", "wb") as f:
        f.write(pattern.encode("utf-8"))
