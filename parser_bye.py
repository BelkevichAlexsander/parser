from yargy import Parser
from yargy.pipelines import morph_pipeline


RULE = morph_pipeline([
    'до свидания',
    'хорошего дня',
    'хорошего вечера',
    'всего хорошего',
    'всего наилучшего',
    'всего доброго',
    ]).repeatable()

parser_bye = Parser(RULE)


def search_bye(text, row):
    for match in parser_bye.findall(text):
        if row['role'] == 'manager':
        
            return {'bye': ' '.join([_.value for _ in match.tokens])}