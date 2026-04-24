import ast

def analyze_code(code: str):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return {"error": "Invalid code"}

    functions = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
    loops = len([n for n in ast.walk(tree) if isinstance(n, ast.For)])

    return {
        "functions": functions,
        "loops": loops,
        "complexity_score": functions + loops
    }