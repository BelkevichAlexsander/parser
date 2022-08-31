from yargy import Parser, rule, or_
from yargy.predicates import gram
from yargy.pipelines import morph_pipeline
from yargy.interpretation import fact

Person = fact(
    'Person',
    ['position', 'name']
)

Name = fact(
    'Name',
    ['first']
)


POSITION = morph_pipeline(['зовут', 'это'])

NAME = rule(
    gram('Name').interpretation(
        Name.first.inflected()
    )
).interpretation(
    Name
)

POSIT = POSITION.interpretation(Person.position.inflected())
NAME = NAME.interpretation(Person.name)

PERSON = or_(
    rule(
        POSIT,
        NAME
    ),
    rule(
        NAME,
        POSIT
    )
    
).interpretation(
    Person
)


parser_name = Parser(PERSON)


def search_name(text, row):
    for match in parser_name.findall(text):
        
        if row['role'] == 'manager' and row['line_n'] <= 5:
            
            lst = [_.value for _ in match.tokens]

            if 'зовут' in lst:
                lst.remove('зовут')
            else:
                lst.remove('это')

            return {'name': lst[0]}