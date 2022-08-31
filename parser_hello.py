from yargy import Parser
from yargy.pipelines import morph_pipeline


RULE = morph_pipeline([
    'здравствуйте',
    'добрый день',
    'добрый вечер',
    'доброе утро',
    'приветствую',
    ])

parser_hello = Parser(RULE)


def search_hello(text, row):
    for match in parser_hello.findall(text):
        if row['role'] == 'manager' and  row['line_n'] <= 5:
        
            return {'hi': ' '.join([_.value for _ in match.tokens])}