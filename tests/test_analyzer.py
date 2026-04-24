from app.core.analyzer import CodeAnalyzer

def test_analysis():
    code = "def test(): return 1"

    analyzer = CodeAnalyzer()
    result = analyzer.analyze(code)

    assert result["functions"] >= 1