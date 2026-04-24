from app.core.analyzer import CodeAnalyzer

analyzer = CodeAnalyzer()

def evaluate_code(code: str):
    result = analyzer.analyze(code)

    return {
        **result,
        "status": "VALID" if "error" not in result else "INVALID"
    }