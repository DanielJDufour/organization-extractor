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
upper = u"[^\W\d_b-z:]"
lower = u"(?:[^\W\d_A-Z:]|')"
acronym = upper + u'{2,}'
titled = u"(?:\d+(?:st|nd|th)[ ])?(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?" + upper + lower + "{2,}(?:(?: |-i-)(?:al-|ash-|ath-|bin |of |of the |wal-|wa-)?"+upper+lower+"{2,})*"
alias = u"(?:(?:"+upper+lower+"{3,}: ?|meaning\")?" + "("+titled+")" + "|" + '('+acronym+')' +  ")"
name = u"((?:"+titled+" )*" + keyword + "(?: "+titled+")*)" + citation
aliases = "(?: ?\(" + alias + "(?: ?" + seperator + alias + ")*" + ")*"
org = name + "(?: or " + name + ")?" + aliases
language_org_pattern['English'] = org




###########################################
###########            ARABIC
##########################################
keyword = language_keyword_pattern['Arabic']
print "keyword is", keyword
pattern = u"(?:" + keyword + u"(?: (?:(?:\u0627\u0644[^ .,\u060c\n\r<\"]*)|\u0641\u064a|(?:\u0628[^ .,\u060c\n\r<\"]*)))+)"
language_org_pattern['Arabic'] = pattern


# write all patterns to their respective files
for language, pattern in language_org_pattern.iteritems():
    with open(directory_of_patterns + "/" + language + ".txt", "wb") as f:
        f.write(pattern.encode("utf-8"))
