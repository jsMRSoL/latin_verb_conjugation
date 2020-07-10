from collections import namedtuple

PrincipalParts = namedtuple('VerbString', ('present', 'infinitive', 'perfect', 'ppp'))

def verb_to_string(verb):
    splitVerb = verb.split(', ')
    present = splitVerb[0]
    infinitive = splitVerb[1]
    perfect = splitVerb[2]
    if len(splitVerb) == 4: 
        ppp = splitVerb[3]
    else:
        ppp = 'none' 
    return PrincipalParts(present, infinitive, perfect, ppp)

def conjugation(verb):
    principalparts = verb_to_string(verb)
    print(principalparts)
    if principalparts.infinitive[-3:] == 'are' \
        or principalparts.infinitive[-3:] == 'ari':
            return 1
    if principalparts.infinitive[-3:] == 'ire' \
        or principalparts.infinitive[-3:] == 'iri':
            return 4
    if principalparts.infinitive[-3:] == 'ere' \
        and principalparts.present[-2:] == 'eo':
            return 2
    if principalparts.infinitive[-3:] == 'eri': 
            return 2
    if principalparts.infinitive[-3:] == 'ere' \
        and principalparts.present[-2:] == 'io':
            return 5
    if principalparts.infinitive[-1:] == 'i' \
        and principalparts.present[-3:] == 'ior':
            return 5
    if principalparts.infinitive[-3:] == 'ere':
            return 3
    if principalparts.infinitive[-1:] == 'i' \
        and principalparts.present[-1:] == 'r':
            return 3
    raise ValueError('This is not a regular verb.')

def present_stem(verb, conjugation):
    """ verb is string, conjugation is integer """
    if conjugation == 1:
        return verb.split(', ')[0][:-1]
    if conjugation == 2:
        return verb.split(', ')[0][:-2]
    if conjugation == 3:
        return verb.split(', ')[0][:-1]
    if conjugation == 4:
        return verb.split(', ')[0][:-2]
    if conjugation == 5:
        return verb.split(', ')[0][:-2]

def make_present_active(verb, person):
    """This function returns the required form of the present active

    :verb: e.g. 'porto, portare, portavi, portatus'
    :person: a number between 1 and 6
    :returns: string

    """
    Endings = (
        ('o', 'as', 'at', 'amus', 'atis', 'ant'),
        ('eo', 'es', 'et', 'emus', 'etis', 'ent'),
        ('o', 'is', 'it', 'imus', 'itis', 'unt'),
        ('io', 'is', 'it', 'imus', 'itis', 'iunt'),
        ('io', 'is', 'it', 'imus', 'itis', 'iunt')
    )
    conj = conjugation(verb)
    return present_stem(verb, conj) + Endings[conj - 1][person - 1] 

print(make_present_active('porto, portare, portavi, portatus', 2))
