#!/usr/bin/env python
# -*- coding: utf-8 -*-
ACT_TRANS = (
    ("I ..., am ...ing", "You (s) ..., are ing",\
            "He/she/it ..., is ...ing", "We ..., are ...ing",\
            "You (pl) ..., are...ing", "They ..., are ...ing"),
    ("I ..., was ...ing", "You (s) ..., were ing",\
            "He/she/it ..., was ...ing", "We ..., were ...ing",\
            "You (pl) ..., were...ing", "They ..., were ...ing"),
    ("I (have) ...ed", "You (have) ...ed",\
            "He/she/it (has) ...ed", "We (have) ...ed",\
            "You (pl) (have) ...ed", "They (have) ...ed"),
    ("I had ...ed", "You had ...ed",\
            "He/she/it had ...ed", "We had ...ed",\
            "You (pl) had ...ed", "They had ...ed"),
    ("I shall ...", "You (s) will ...",\
            "He/she/it will ...", "We shall ...",\
            "You (pl) will ...", "They will ..."),
    ("I shall have ...ed", "You (s) will have ...ed",\
            "He/she/it will have ...ed", "We will have ...ed",\
            "You (pl) will have ...ed", "They will have ...ed")
)

PASS_TRANS = (
    ("I am (being) ...ed", "You (s) are (being) ...ed",\
            "He/she/it is (being) ...ed)", "We are (being) ...ed",\
            "You (pl) are (being) ...ed", "They are (being) ...ed"),
    ("I was being ...ed", "You (s) were being ...ed",\
            "He/she/it was being ...ed)", "We were being ...ed",\
            "You (pl) were being ...ed", "They were being ...ed"),
    ("I was ...ed", "You (s) were ...ed",\
            "He/she/it was ...ed)", "We were ...ed",\
            "You (pl) were ...ed", "They were ...ed"),
    ("I had been ...ed", "You (s) had been ...ed",\
            "He/she/it had been ...ed)", "We had been ...ed",\
            "You (pl) had been ...ed", "They had been ...ed"),
    ("I shall be ...ed", "You (s) will be ...ed",\
            "He/she/it will be ...ed)", "We shall be ...ed",\
            "You (pl) will be ...ed", "They will be ...ed"),
    ("I shall have been ...ed", "You (s) will be ...ed",\
            "He/she/it will be ...ed)", "We shall have been ...ed",\
            "You (pl) will be ...ed", "They will be ...ed")
)

def print_tense(latlist, englist):
    """
    :list: verb object's list of finite verb parts
    :returns: html formatted string
    """
    string = "<table>\n"
    for i, part in enumerate(latlist):
        string += '<tr>\n\t<td>' + part + '</td>\n'
        string += '\t<td>' + englist[i] + '</td>\n</tr>\n'
    string += "</table>\n"
    return string

def writehtml(verbobj):
    """
    :verbobj: verb object created with Verbs.py
    :returns: string in html format
    """
    string = "<html>\n<body>\n"
    string += print_tense(verbobj.present_active_indicative,
            ACT_TRANS[0])
    string += print_tense(verbobj.present_passive_indicative,
            PASS_TRANS[0])
    string += print_tense(verbobj.imperfect_active_indicative,
            ACT_TRANS[1])
    string += print_tense(verbobj.imperfect_passive_indicative,
            PASS_TRANS[1])
    string += print_tense(verbobj.perfect_active_indicative,
            ACT_TRANS[2])
    string += print_tense(verbobj.perfect_passive_indicative,
            PASS_TRANS[2])
    string += print_tense(verbobj.pluperfect_active_indicative,
            ACT_TRANS[3])
    string += print_tense(verbobj.pluperfect_passive_indicative,
            PASS_TRANS[3])
    string += print_tense(verbobj.future_active_indicative,
            ACT_TRANS[4])
    string += print_tense(verbobj.future_passive_indicative,
            PASS_TRANS[4])
    string += print_tense(verbobj.future_perfect_active_indicative,
            ACT_TRANS[5])
    string += print_tense(verbobj.future_perfect_passive_indicative,
            PASS_TRANS[5])
    string += "</body>\n</html>"
    return string

def write_html_to_file(htmlstring, filename=None):
    while (True):
        if filename == None:
            filename = input("Please input filename: ")
        else:
            break

    with open(filename, 'a') as fn:
        fn.write(htmlstring)
