from aksharamukha import transliterate
import json

print(transliterate.process('HK', 'Siddham', 'buddhaH'))

print(transliterate.process('autodetect', 'IAST', 'ꯃꯤꯇꯩ_ꯃꯌꯦꯛ'))

print(transliterate.process('HK', 'Tamil', 'maMgaLa', False))

print(transliterate.process('HK', 'Tamil', 'bRhaspati gaMgA', False, post_options = ['TamilSubScript','TamilRemoveApostrophe']))

print(transliterate.process('Thai', 'Devanagari', 'พุทธัง สะระณัง คัจฉามิ', pre_options=['ThaiOrthography']))

print(transliterate.process('autodetect', 'IAST', 'พุทธัง สะระณัง คัจฉามิ'))

print(transliterate.auto_detect('ꯃꯤꯇꯩ_ꯃꯌꯦꯛ'))

print(transliterate.process('Devanagari', 'IAST', 'धर्म भारत की श्रमण परम्परा से निकला धर्म और दर्शन है', pre_options=['RemoveSchwaHindi']))


    

f = open('./data.json',)

    # returns JSON object as
    # a dictionary
data = json.load(f)

transliterate.convert_docx(data["source"], data["target"], data["fileDocx"], nativize=data["nativize"], post_options=data["preOptions"], pre_options=data["postOptions"])

