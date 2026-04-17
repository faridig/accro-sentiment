"""
Tests for the ACCRO Sentiment Analyzer walking skeleton.
Sprint 0: Basic test structure.
"""

import asyncio
import sys
import os
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_project_structure():
    """Test that the project has the expected structure."""
    project_root = Path(__file__).parent.parent
    
    # Check essential directories exist
    assert (project_root / "src").exists(), "src/ directory missing"
    assert (project_root / "tests").exists(), "tests/ directory missing"
    assert (project_root / "docs").exists(), "docs/ directory missing"
    assert (project_root / "config").exists(), "config/ directory missing"
    
    # Check essential files exist
    assert (project_root / "pyproject.toml").exists(), "pyproject.toml missing"
    assert (project_root / ".env.example").exists(), ".env.example missing"
    assert (project_root / ".gitignore").exists(), ".gitignore missing"
    assert (project_root / "README.md").exists(), "README.md missing"
    
    # Check source files
    assert (project_root / "src" / "main.py").exists(), "src/main.py missing"
    assert (project_root / "src" / "__init__.py").exists(), "src/__init__.py missing"
    
    print("✅ Project structure test passed")


def test_main_module_import():
    """Test that the main module can be imported."""
    try:
        import src.main
        print("✅ Main module import test passed")
    except ImportError as e:
        raise AssertionError(f"Failed to import main module: {e}")


async def test_main_execution():
    """Test that the main function executes without errors."""
    from src.main import main
    
    try:
        await main()
        print("✅ Main execution test passed")
    except Exception as e:
        raise AssertionError(f"Main execution failed: {e}")


def test_python_version():
    """Test that Python version is 3.11 or higher."""
    version = sys.version_info
    assert version.major == 3 and version.minor >= 11, \
        f"Python 3.11+ required, found {version.major}.{version.minor}"
    print(f"✅ Python version test passed: {version.major}.{version.minor}")


def run_all_tests():
    """Run all tests for Sprint 0."""
    print("\n" + "="*50)
    print("RUNNING SPRINT 0 TESTS")
    print("="*50)
    
    tests = [
        test_project_structure,
        test_main_module_import,
        lambda: asyncio.run(test_main_execution()),
        test_python_version,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            failed += 1
    
    print("\n" + "="*50)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("="*50)
    
    if failed == 0:
        print("🎉 All tests passed! Sprint 0 infrastructure is ready.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the project setup.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)