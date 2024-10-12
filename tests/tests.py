# Generated tests on 2024-10-12 12:50:06

import ast
import json
import astjson
import unittest
from pprint import pprint

class Tests(unittest.TestCase):
    
	def test_x1(self):
		print("Testing x = 1")
		parsed_ast = ast.parse("x = 1")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Assign', 'targets': [{'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Store'}}], 'value': {'_type': 'Constant', 'value': 1, 'kind': None}, 'type_comment': None}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_x1y2(self):
		print("Testing x = 1; y = 2")
		parsed_ast = ast.parse("x = 1; y = 2")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Assign', 'targets': [{'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Store'}}], 'value': {'_type': 'Constant', 'value': 1, 'kind': None}, 'type_comment': None}, {'_type': 'Assign', 'targets': [{'_type': 'Name', 'id': 'y', 'ctx': {'_type': 'Store'}}], 'value': {'_type': 'Constant', 'value': 2, 'kind': None}, 'type_comment': None}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_123(self):
		print("Testing [1, 2, 3]")
		parsed_ast = ast.parse("[1, 2, 3]")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'List', 'elts': [{'_type': 'Constant', 'value': 1, 'kind': None}, {'_type': 'Constant', 'value': 2, 'kind': None}, {'_type': 'Constant', 'value': 3, 'kind': None}], 'ctx': {'_type': 'Load'}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_123(self):
		print("Testing {1, 2, 3}")
		parsed_ast = ast.parse("{1, 2, 3}")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'Set', 'elts': [{'_type': 'Constant', 'value': 1, 'kind': None}, {'_type': 'Constant', 'value': 2, 'kind': None}, {'_type': 'Constant', 'value': 3, 'kind': None}]}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_a(self):
		print("Testing a")
		parsed_ast = ast.parse("a")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'Name', 'id': 'a', 'ctx': {'_type': 'Load'}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_a1(self):
		print("Testing a = 1")
		parsed_ast = ast.parse("a = 1")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Assign', 'targets': [{'_type': 'Name', 'id': 'a', 'ctx': {'_type': 'Store'}}], 'value': {'_type': 'Constant', 'value': 1, 'kind': None}, 'type_comment': None}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_dela(self):
		print("Testing del a")
		parsed_ast = ast.parse("del a")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Delete', 'targets': [{'_type': 'Name', 'id': 'a', 'ctx': {'_type': 'Del'}}]}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_a(self):
		print("Testing - a")
		parsed_ast = ast.parse("- a")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'UnaryOp', 'op': {'_type': 'USub'}, 'operand': {'_type': 'Name', 'id': 'a', 'ctx': {'_type': 'Load'}}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_notx(self):
		print("Testing not x")
		parsed_ast = ast.parse("not x")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'UnaryOp', 'op': {'_type': 'Not'}, 'operand': {'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Load'}}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_xy(self):
		print("Testing x + y")
		parsed_ast = ast.parse("x + y")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'BinOp', 'left': {'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Load'}}, 'op': {'_type': 'Add'}, 'right': {'_type': 'Name', 'id': 'y', 'ctx': {'_type': 'Load'}}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_foo12(self):
		print("Testing foo(1, 2, ...)")
		parsed_ast = ast.parse("foo(1, 2, ...)")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'Call', 'func': {'_type': 'Name', 'id': 'foo', 'ctx': {'_type': 'Load'}}, 'args': [{'_type': 'Constant', 'value': 1, 'kind': None}, {'_type': 'Constant', 'value': 2, 'kind': None}, {'_type': 'Constant', 'value': {'_type': 'Ellipsis', 'value': 'Ellipsis'}, 'kind': None}], 'keywords': []}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_aifbelsec(self):
		print("Testing a if b else c")
		parsed_ast = ast.parse("a if b else c")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'IfExp', 'test': {'_type': 'Name', 'id': 'b', 'ctx': {'_type': 'Load'}}, 'body': {'_type': 'Name', 'id': 'a', 'ctx': {'_type': 'Load'}}, 'orelse': {'_type': 'Name', 'id': 'c', 'ctx': {'_type': 'Load'}}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_l123(self):
		print("Testing l[1:2, 3]")
		parsed_ast = ast.parse("l[1:2, 3]")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'Subscript', 'value': {'_type': 'Name', 'id': 'l', 'ctx': {'_type': 'Load'}}, 'slice': {'_type': 'Tuple', 'elts': [{'_type': 'Slice', 'lower': {'_type': 'Constant', 'value': 1, 'kind': None}, 'upper': {'_type': 'Constant', 'value': 2, 'kind': None}, 'step': None}, {'_type': 'Constant', 'value': 3, 'kind': None}], 'ctx': {'_type': 'Load'}}, 'ctx': {'_type': 'Load'}}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_xforxinnumbers(self):
		print("Testing [x for x in numbers]")
		parsed_ast = ast.parse("[x for x in numbers]")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Expr', 'value': {'_type': 'ListComp', 'elt': {'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Load'}}, 'generators': [{'_type': 'comprehension', 'target': {'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Store'}}, 'iter': {'_type': 'Name', 'id': 'numbers', 'ctx': {'_type': 'Load'}}, 'ifs': [], 'is_async': 0}]}}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_importxyz(self):
		print("Testing import x,y,z")
		parsed_ast = ast.parse("import x,y,z")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'Import', 'names': [{'_type': 'alias', 'name': 'x', 'asname': None}, {'_type': 'alias', 'name': 'y', 'asname': None}, {'_type': 'alias', 'name': 'z', 'asname': None}]}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
	def test_xint(self):
		print("Testing x:int")
		parsed_ast = ast.parse("x:int")
		print(ast.dump(parsed_ast, indent=2))
		expected = {'_type': 'Module', 'body': [{'_type': 'AnnAssign', 'target': {'_type': 'Name', 'id': 'x', 'ctx': {'_type': 'Store'}}, 'annotation': {'_type': 'Name', 'id': 'int', 'ctx': {'_type': 'Load'}}, 'value': None, 'simple': 1}], 'type_ignores': []}
		pprint(expected)
		result = astjson.ast_to_json(parsed_ast)
		self.assertEqual(expected, result)
		assert json.dumps(result)
		print("--------")
