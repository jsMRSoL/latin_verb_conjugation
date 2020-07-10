class Verb(object):

    """Creates a verb object"""

    def __init__(self, verb_parts_string):
        """Form all parts """
        # assume some defaults
        self.irregular = False
        self.deponent = False
        self.semideponent = False
        # populate principal parts and meaning
        if "-" in verb_parts_string:
            principal_parts, self.meanings \
                = [x.strip() for x in verb_parts_string.split("-")]
        elif ":" in verb_parts_string:
            principal_parts, self.meanings \
                = [x.strip() for x in verb_parts_string.split(":")]
        elif "=" in verb_parts_string:
            principal_parts, self.meanings \
                = [x.strip() for x in verb_parts_string.split("=")]
        parts_list = principal_parts.strip().split(',')
        if len(parts_list) > 3:
            self.first_principal_part, self.second_principal_part, \
                self.third_principal_part, self.fourth_principal_part \
                = [x.strip() for x in parts_list]
            self.perfect_passive_infinitive = self.fourth_principal_part + ' esse'
            self.future_active_infinitive = self.fourth_principal_part[:-2] + 'urus esse'
            self.future_passive_infinitive = self.fourth_principal_part[:-1] + 'm iri'
            self.perfect_participle = self.fourth_principal_part
            self.future_participle = self.fourth_principal_part[:-2] + 'urus'
        else:
            self.first_principal_part, self.second_principal_part, \
                self.third_principal_part \
                = [x.strip() for x in parts_list]
        # decide conjugation
        self.conjugation = self.make_conjugation(
            self.first_principal_part, self.second_principal_part)
        # Is deponent or not?
        if self.first_principal_part[-1:] == 'r':
            self.deponent = True
        if self.deponent:
            self.present_stem = self.make_present_stem(
                self.first_principal_part, self.conjugation, True)
            self.fourth_principal_part = self.third_principal_part.split(' ')[
                0]
            self.present_active_indicative = \
                self.make_present_passive_indicative(
                    self.present_stem, self.conjugation)
            self.present_active_subjunctive = \
                self.make_present_passive_subjunctive(
                    self.present_stem, self.conjugation)
            self.imperfect_active_indicative = \
                self.make_imperfect_passive_indicative(
                    self.present_stem, self.conjugation)
            self.imperfect_active_subjunctive = \
                self.make_imperfect_passive_subjunctive(
                    self.present_stem, self.conjugation)
            self.future_active_indicative = \
                self.make_future_passive_indicative(
                    self.present_stem, self.conjugation)
            self.perfect_active_indicative = [self.fourth_principal_part[:-2] + end for end in (
                'us sum', 'us es', 'us est', 'i sumus', 'i estis', 'i sunt')]
            self.perfect_active_subjunctive = [self.fourth_principal_part[:-2] + end for end in (
                'us sim', 'us sis', 'us sit', 'i simus', 'i sitis', 'i sint')]
            self.pluperfect_active_indicative = [self.fourth_principal_part[:-2] + end for end in (
                'us eram', 'us eras', 'us erat', 'i eramus', 'i eratis', 'i erant')]
            self.pluperfect_active_subjunctive = [self.fourth_principal_part[:-2] + end for end in (
                'us essem', 'us esses', 'us esset', 'i essemus', 'i essetis', 'i essent')]
            self.future_perfect_active_indicative = [self.fourth_principal_part[:-2] + end for end in (
                'us ero', 'us eris', 'us erit', 'i erimus', 'i eritis', 'i erunt')]
            self.present_active_imperative = self.make_present_passive_imperative(
                self.present_stem, self.conjugation)
        else:
            # set stems ready for conjugating
            self.present_stem = self.make_present_stem(
                self.first_principal_part, self.conjugation)
            self.perfect_stem = self.third_principal_part[:-1]
            # set remaining infinitives and participles
            self.perfect_active_infinitive = self.perfect_stem + 'isse'
            self.present_participle = self.make_present_participle(
                self.present_stem, self.conjugation)
            # conjugate active forms
            self.present_active_indicative = \
                self.make_present_active_indicative(
                    self.present_stem, self.conjugation)
            self.present_active_subjunctive = \
                self.make_present_active_subjunctive(
                    self.present_stem, self.conjugation)
            self.imperfect_active_indicative = \
                self.make_imperfect_active_indicative(
                    self.present_stem, self.conjugation)
            self.imperfect_active_subjunctive = [self.second_principal_part +
                                                 end for end in ('m', 's', 't', 'mus', 'tis', 'nt')]
            self.future_active_indicative = \
                self.make_future_active_indicative(
                    self.present_stem, self.conjugation)
            self.perfect_active_indicative = [self.perfect_stem +
                                              end for end in ('i', 'isti', 'it', 'imus', 'itis', 'erunt')]
            self.perfect_active_subjunctive = [self.perfect_stem +
                                               end for end in ('erim', 'eris', 'erit', 'erimus', 'eritis', 'erint')]
            self.pluperfect_active_indicative = [self.perfect_stem +
                                                 end for end in ('eram', 'eras', 'erat', 'eramus', 'eratis', 'erant')]
            self.pluperfect_active_subjunctive = [self.perfect_stem +
                                                  end for end in ('issem', 'isses', 'isset', 'issemus', 'issetis', 'issent')]
            self.future_perfect_active_indicative = [self.perfect_stem +
                                                     end for end in ('ero', 'eris', 'erit', 'erimus', 'eritis', 'erint')]
            # conjugative passive forms
            self.present_passive_indicative = \
                self.make_present_passive_indicative(
                    self.present_stem, self.conjugation)
            self.present_passive_subjunctive = \
                self.make_present_passive_subjunctive(
                    self.present_stem, self.conjugation)
            self.imperfect_passive_indicative = \
                self.make_imperfect_passive_indicative(
                    self.present_stem, self.conjugation)
            self.imperfect_passive_subjunctive = \
                self.make_imperfect_passive_subjunctive(
                    self.present_stem, self.conjugation)
            self.future_passive_indicative = \
                self.make_future_passive_indicative(
                    self.present_stem, self.conjugation)
            self.perfect_passive_indicative = [self.fourth_principal_part[:-2]
                                               + end for end in ('us sum', 'us es', 'us est', 'i sumus', 'i estis', 'i sunt')]
            self.perfect_passive_subjunctive = [self.fourth_principal_part[:-2]
                                                + end for end in ('us sim', 'us sis', 'us sit', 'i simus', 'i sitis', 'i sint')]
            self.pluperfect_passive_indicative = [self.fourth_principal_part[:-2] +
                                                  end for end in ('us eram', 'us eras', 'us erat', 'i eramus', 'i eratis', 'i erant')]
            self.pluperfect_passive_subjunctive = [self.fourth_principal_part[:-2] +
                                                   end for end in ('us essem', 'us esses', 'us esset', 'i essemus', 'i essetis', 'i essent')]
            self.future_perfect_passive_indicative = [self.fourth_principal_part[:-2] +
                                                      end for end in ('us ero', 'us eris', 'us erit', 'i erimus', 'i eritis', 'i erunt')]
            self.present_active_imperative = self.make_present_active_imperative(
                self.present_stem, self.conjugation)
            self.present_passive_imperative = self.make_present_passive_imperative(
                self.present_stem, self.conjugation)
        self.gerundive = self.make_gerundive(
            self.present_stem, self.conjugation)
        self.gerund = self.make_gerund(self.present_stem, self.conjugation)

    def make_imperfect_passive_subjunctive(self, present_stem, conjugation):
        Endings = ('r', 'ris', 'tur', 'mur', 'mini', 'ntur')
        if conjugation == 1:
            return [present_stem + 'are' + end for end in Endings]
        if conjugation == 2:
            return [present_stem + 'ere' + end for end in Endings]
        if conjugation == 3:
            return [present_stem + 'ere' + end for end in Endings]
        if conjugation == 4:
            return [present_stem + 'ire' + end for end in Endings]
        if conjugation == 5:
            return [present_stem + 'ere' + end for end in Endings]

    def make_conjugation(self, first_principal_part, second_principal_part):
        # get conjugation (3.5 is 5)
        if second_principal_part[-3:] == 'are' \
                or second_principal_part[-3:] == 'ari':
            return 1
        elif second_principal_part[-3:] == 'ire' \
                or second_principal_part[-3:] == 'iri':
            return 4
        elif second_principal_part[-3:] == 'ere' \
                and first_principal_part[-2:] == 'eo':
            return 2
        elif second_principal_part[-3:] == 'eri':
            return 2
        elif second_principal_part[-3:] == 'ere' \
                and first_principal_part[-2:] == 'io':
            return 5
        elif second_principal_part[-1:] == 'i' \
                and first_principal_part[-3:] == 'ior':
            return 5
        elif second_principal_part[-3:] == 'ere':
            return 3
        elif second_principal_part[-1:] == 'i' \
                and first_principal_part[-1:] == 'r':
            return 3
        else:
            raise ValueError('This is not a regular verb.')

    def make_present_stem(self, present, conjugation, deponent=False):
        if deponent:
            if conjugation == 1:
                return present[:-2]
            if conjugation == 2:
                return present[:-3]
            if conjugation == 3:
                return present[:-2]
            if conjugation == 4:
                return present[:-3]
            if conjugation == 5:
                return present[:-3]
        else:
            if conjugation == 1:
                return present[:-1]
            if conjugation == 2:
                return present[:-2]
            if conjugation == 3:
                return present[:-1]
            if conjugation == 4:
                return present[:-2]
            if conjugation == 5:
                return present[:-2]

    def make_present_participle(self, present_stem, conjugation):
        Endings = ('ans', 'ens', 'ens', 'iens', 'iens')
        return present_stem + Endings[conjugation - 1]

    def make_gerundive(self, present_stem, conjugation):
        Endings = ('andus', 'endus', 'endus', 'iendus', 'iendus')
        return present_stem + Endings[conjugation - 1]

    def make_gerund(self, present_stem, conjugation):
        Endings = ('andum', 'endum', 'endum', 'iendum', 'iendum')
        return present_stem + Endings[conjugation - 1]

    def make_present_active_imperative(self, present_stem, conjugation):
        Endings = (
            ('a', 'ato', 'ate', 'anto'),
            ('e', 'eto', 'ete', 'ento'),
            ('e', 'ito', 'ite', 'unto'),
            ('i', 'ito', 'ite', 'iunto'),
            ('e', 'ito', 'ite', 'iunto')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_present_passive_imperative(self, present_stem, conjugation):
        Endings = (
            ('are', 'ator', 'amini', 'antor'),
            ('ere', 'etor', 'emini', 'entor'),
            ('ere', 'itor', 'imini', 'untor'),
            ('ire', 'itor', 'imini', 'iuntor'),
            ('ere', 'itor', 'imini', 'iuntor')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_present_active_indicative(self, present_stem, conjugation):
        Endings = (
            ('o', 'as', 'at', 'amus', 'atis', 'ant'),
            ('eo', 'es', 'et', 'emus', 'etis', 'ent'),
            ('o', 'is', 'it', 'imus', 'itis', 'unt'),
            ('io', 'is', 'it', 'imus', 'itis', 'iunt'),
            ('io', 'is', 'it', 'imus', 'itis', 'iunt')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_present_active_subjunctive(self, present_stem, conjugation):
        Endings = (
            ('em', 'es', 'et', 'emus', 'etis', 'ent'),
            ('eam', 'eas', 'eat', 'eamus', 'eatis', 'eant'),
            ('am', 'as', 'at', 'amus', 'atis', 'ant'),
            ('iam', 'ias', 'iat', 'iamus', 'iatis', 'iant'),
            ('iam', 'ias', 'iat', 'iamus', 'iatis', 'iant')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_imperfect_active_indicative(self, present_stem, conjugation):
        Endings = (
            ('abam', 'abas', 'abat', 'abamus', 'abatis', 'abant'),
            ('ebam', 'ebas', 'ebat', 'ebamus', 'ebatis', 'ebant'),
            ('ebam', 'ebas', 'ebat', 'ebamus', 'ebatis', 'ebant'),
            ('iebam', 'iebas', 'iebat', 'iebamus', 'iebatis', 'iebant'),
            ('iebam', 'iebas', 'iebat', 'iebamus', 'iebatis', 'iebant')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_future_active_indicative(self, present_stem, conjugation):
        Endings = (
            ('abo', 'abis', 'abit', 'abimus', 'abitis', 'abunt'),
            ('ebo', 'ebis', 'ebit', 'ebimus', 'ebitis', 'ebunt'),
            ('am', 'es', 'et', 'emus', 'etis', 'ent'),
            ('iam', 'ies', 'iet', 'iemus', 'ietis', 'ient'),
            ('iam', 'ies', 'iet', 'iemus', 'ietis', 'ient')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_present_passive_indicative(self, present_stem, conjugation):
        Endings = (
            ('or', 'aris', 'atur', 'amur', 'amini', 'antur'),
            ('eor', 'eris', 'etur', 'emur', 'emini', 'entur'),
            ('or', 'eris', 'itur', 'imur', 'imini', 'untur'),
            ('ior', 'iris', 'itur', 'imur', 'imini', 'iuntur'),
            ('ior', 'eris', 'itur', 'imur', 'imini', 'iuntur')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_present_passive_subjunctive(self, present_stem, conjugation):
        Endings = (
            ('er', 'eris', 'etur', 'emur', 'emini', 'entur'),
            ('ear', 'earis', 'eatur', 'eamur', 'eamini', 'eantur'),
            ('ar', 'aris', 'atur', 'amur', 'amini', 'antur'),
            ('iar', 'iaris', 'iatur', 'iamur', 'iamini', 'iantur'),
            ('iar', 'iaris', 'iatur', 'iamur', 'iamini', 'iantur')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_imperfect_passive_indicative(self, present_stem, conjugation):
        Endings = (
            ('abar', 'abaris', 'abatur', 'abamur', 'abamini', 'abantur'),
            ('ebar', 'ebaris', 'ebatur', 'ebamur', 'ebamini', 'ebantur'),
            ('ebar', 'ebaris', 'ebatur', 'ebamur', 'ebamini', 'ebantur'),
            ('iebar', 'iebaris', 'iebatur', 'iebamur', 'iebamini', 'iebantur'),
            ('iebar', 'iebaris', 'iebatur', 'iebamur', 'iebamini', 'iebantur')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def make_future_passive_indicative(self, present_stem, conjugation):
        Endings = (
            ('abor', 'aberis', 'abitur', 'abimur', 'abitis', 'abuntur'),
            ('ebor', 'eberis', 'ebitur', 'ebimur', 'ebitis', 'ebuntur'),
            ('ar', 'eris', 'etur', 'emur', 'emini', 'entur'),
            ('iar', 'ieris', 'ietur', 'iemur', 'iemini', 'ientur'),
            ('iar', 'ieris', 'ietur', 'iemur', 'iemini', 'ientur')
        )
        return [present_stem + end for end in Endings[conjugation - 1]]

    def to_string(self):
        print(self.first_principal_part)
        print(self.third_principal_part)
        print(self.meanings)
        print(self.conjugation)
        print(self.present_stem)
        print(self.perfect_stem)
        print(self.present_participle)
        print(self.perfect_participle)
        print(self.future_participle)
        print(self.gerundive)
        print(self.gerund)

        print(self.present_active_indicative)
        print(self.present_active_subjunctive)
        print(self.imperfect_active_indicative)
        print(self.imperfect_active_subjunctive)
        print(self.future_active_indicative)
        print(self.perfect_active_indicative)
        print(self.perfect_active_subjunctive)
        print(self.pluperfect_active_indicative)
        print(self.pluperfect_active_subjunctive)
        print(self.future_perfect_active_indicative)
        print(self.present_active_imperative)

        print(self.present_passive_indicative)
        print(self.present_passive_subjunctive)
        print(self.imperfect_passive_indicative)
        print(self.imperfect_passive_subjunctive)
        print(self.future_passive_indicative)
        print(self.perfect_passive_indicative)
        print(self.perfect_passive_subjunctive)
        print(self.pluperfect_passive_indicative)
        print(self.pluperfect_passive_subjunctive)
        print(self.future_perfect_passive_indicative)
        print(self.present_passive_imperative)

# myNewVerb = Verb('porto, portare, portavi, portatus - carry ')
# myNewVerb.to_string()
