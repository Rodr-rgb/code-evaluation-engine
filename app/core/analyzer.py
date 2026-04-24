import ast

class CodeAnalyzer:
    def analyze(self, code: str):
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return {"error": "invalid code"}

        functions = len([
            n for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef)
        ])

        loops = len([
            n for n in ast.walk(tree)
            if isinstance(n, (ast.For, ast.While))
        ])

        complexity = functions + loops

        return {
            "functions": functions,
            "loops": loops,
            "complexity_score": complexity,
            "grade": self._grade(complexity)
        }

    def _grade(self, complexity: int):
        if complexity >= 5:
            return "A"
        elif complexity >= 3:
            return "B"
        return "C"