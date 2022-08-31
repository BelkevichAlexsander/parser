from yargy import Parser
from yargy.pipelines import morph_pipeline


RULE = morph_pipeline([
    'диджитал бизнес',
    'китобизнес'
    ])

parser_company = Parser(RULE)


def search_company(text, row):
    for match in parser_company.findall(text):
        if row['role'] == 'manager' and  row['line_n'] <= 5:
        
            return {'company': ' '.join([_.value for _ in match.tokens])}