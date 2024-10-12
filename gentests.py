from datetime import datetime
import re
import uuid
import ast
import astjson


expressions = [
    'x = 1',
    'x = 1; y = 2',
    #'f"sin({a}) is {sin(a):.3}"',
    '[1, 2, 3]',
    '{1, 2, 3}',
    #'{"a":1, **d}',
    'a',
    'a = 1',
    'del a',
    '- a',
    'not x',
    'x + y',
    'foo(1, 2, ...)',
    'a if b else c',
    'l[1:2, 3]',
    '[x for x in numbers]',
    'import x,y,z',
    'x:int',
]
def generate_testname(expr: str) -> str:
    cleaned_expr = re.sub(r'[^a-zA-Z1-9]', '', expr)
    if not cleaned_expr:
        return "test_" + str(uuid.uuid4()).replace('-', '')
    return "test_" + cleaned_expr

def generate_testcase(expr: str) -> str:
    test_name = generate_testname(expr)
    result_strs = [f"\tdef {test_name}(self):", 
                  f"\t\tprint(\"Testing {expr}\")",
                  f"\t\tparsed_ast = ast.parse(\"{expr}\")"]
    parsed_ast = ast.parse(expr)
    result_strs.append("\t\tprint(ast.dump(parsed_ast, indent=2))")
    expected = astjson.ast_to_json(parsed_ast)
    result_strs.append(f"\t\texpected = {expected}")
    result_strs.append(f"\t\tpprint(expected)")
    result_strs.append("\t\tresult = astjson.ast_to_json(parsed_ast)")
    result_strs.append(f"\t\tself.assertEqual(expected, result)")
    result_strs.append("\t\tassert json.dumps(result)")
    result_strs.append('\t\tprint("--------")')
    return '\n'.join(result_strs)

def main():
    formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"# Generated tests on {formatted_date}")
    preamble = """
import ast
import json
import astjson
import unittest
from pprint import pprint

class Tests(unittest.TestCase):
    """
    print(preamble)
    for expr in expressions:
        print(generate_testcase(expr))
if __name__ == '__main__':
    main()