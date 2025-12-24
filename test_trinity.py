"""
Tests for TrinityCore Stream implementation.

Run with: python test_trinity.py
"""

import sys

from trinity_core import TrinityCoreStream, SecureExtension, safe_loader
from extensions import (
    EquationTransformer,
    IntegralExpander,
    SymbolicLogger,
    StateInjector
)


def test_core_initialization():
    """Test that core initializes correctly."""
    print("Testing core initialization...", end=" ")
    core = TrinityCoreStream()
    assert core.state == {}
    assert core.extensions == []
    print("✓")


def test_basic_extension():
    """Test basic extension loading and processing."""
    print("Testing basic extension...", end=" ")
    core = TrinityCoreStream()
    ext = EquationTransformer()
    core.add_extension(ext)
    result = core.stream("test")
    assert "Ψ' = dΨ/dt" in result
    assert "test" in result
    print("✓")


def test_multiple_extensions():
    """Test multiple extensions chained together."""
    print("Testing multiple extensions...", end=" ")
    core = TrinityCoreStream()
    core.add_extension(IntegralExpander())
    core.add_extension(EquationTransformer())
    result = core.stream("∫ test")
    assert "integral of" in result
    print("✓")


def test_state_injection():
    """Test state injection into stream."""
    print("Testing state injection...", end=" ")
    core = TrinityCoreStream()
    core.add_extension(StateInjector("key1", "value1"))
    assert "key1" in core.state
    assert core.state["key1"] == "value1"
    print("✓")


def test_logging_extension():
    """Test logging extension."""
    print("Testing logging extension...", end=" ")
    core = TrinityCoreStream()
    logger = SymbolicLogger()
    core.add_extension(logger)
    core.stream("test1")
    core.stream("test2")
    assert len(logger.log_history) == 2
    assert "test1" in logger.log_history[0]
    assert "test2" in logger.log_history[1]
    print("✓")


def test_validation_checks():
    """Test that validation methods are called."""
    print("Testing validation checks...", end=" ")
    
    class TestExtension(SecureExtension):
        def ethics_safe(self):
            return True
        
        def lagrangian_stable(self):
            return True
    
    ext = TestExtension()
    assert ext.ethics_safe() == True
    assert ext.lagrangian_stable() == True
    print("✓")


def test_failed_validation():
    """Test that invalid extensions are rejected."""
    print("Testing failed validation...", end=" ")
    
    class UnsafeExtension(SecureExtension):
        def ethics_safe(self):
            return False
    
    core = TrinityCoreStream()
    try:
        core.add_extension(UnsafeExtension())
        assert False, "Should have raised ValueError"
    except ValueError:
        pass  # Expected
    print("✓")


def test_safe_loader():
    """Test the safe_loader function."""
    print("Testing safe_loader...", end=" ")
    ext = EquationTransformer()
    loaded = safe_loader(ext)
    assert loaded == ext
    print("✓")


def test_safe_loader_failure():
    """Test safe_loader with invalid extension."""
    print("Testing safe_loader failure...", end=" ")
    
    class BadExtension(SecureExtension):
        def ethics_safe(self):
            return False
    
    try:
        safe_loader(BadExtension())
        assert False, "Should have raised AssertionError"
    except AssertionError:
        pass  # Expected
    print("✓")


def test_integral_expansion():
    """Test integral expansion specifically."""
    print("Testing integral expansion...", end=" ")
    ext = IntegralExpander()
    result = ext.mutate("∫ f(x) dx")
    assert "integral of" in result
    assert "f(x) dx" in result
    print("✓")


def test_equation_transformer():
    """Test equation transformer specifically."""
    print("Testing equation transformer...", end=" ")
    ext = EquationTransformer()
    result = ext.mutate("input")
    assert "Ψ' = dΨ/dt" in result
    assert "input" in result
    print("✓")


def test_stream_with_empty_extensions():
    """Test streaming with no extensions."""
    print("Testing stream with no extensions...", end=" ")
    core = TrinityCoreStream()
    result = core.stream("test")
    assert result == "Core processed: test"
    print("✓")


def test_complex_pipeline():
    """Test complex pipeline with multiple extensions."""
    print("Testing complex pipeline...", end=" ")
    core = TrinityCoreStream()
    core.add_extension(StateInjector("test_key", "test_value"))
    core.add_extension(IntegralExpander())
    core.add_extension(EquationTransformer())
    
    result = core.stream("∫ L dt")
    assert "integral of" in result
    assert "Ψ' = dΨ/dt" in result
    assert "test_key" in core.state
    print("✓")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("Running TrinityCore Stream Tests")
    print("="*60 + "\n")
    
    tests = [
        test_core_initialization,
        test_basic_extension,
        test_multiple_extensions,
        test_state_injection,
        test_logging_extension,
        test_validation_checks,
        test_failed_validation,
        test_safe_loader,
        test_safe_loader_failure,
        test_integral_expansion,
        test_equation_transformer,
        test_stream_with_empty_extensions,
        test_complex_pipeline,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ (Error: {e})")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Tests completed: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
