"""
Example usage and demonstrations of TrinityCore Stream.

This script shows various ways to use the streaming architecture
with different extensions.
"""

from trinity_core import TrinityCoreStream
from extensions import (
    EquationTransformer,
    IntegralExpander,
    SymbolicLogger,
    StateInjector
)


def example_basic():
    """Basic example from README - equation transformation."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Equation Transformation")
    print("="*60)
    
    core = TrinityCoreStream()
    core.add_extension(EquationTransformer())
    out = core.stream("∫ L dt")
    print(out)


def example_multiple_extensions():
    """Example with multiple extensions chained together."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Multiple Extensions")
    print("="*60)
    
    core = TrinityCoreStream()
    core.add_extension(IntegralExpander())
    core.add_extension(EquationTransformer())
    out = core.stream("∫ L dt")
    print(out)


def example_with_logging():
    """Example with logging extension to track transformations."""
    print("\n" + "="*60)
    print("EXAMPLE 3: With Logging")
    print("="*60)
    
    core = TrinityCoreStream()
    core.add_extension(SymbolicLogger(log_prefix="[TRANSFORM]"))
    core.add_extension(EquationTransformer())
    out = core.stream("∫ L dt")
    print(out)


def example_with_state():
    """Example demonstrating state injection."""
    print("\n" + "="*60)
    print("EXAMPLE 4: State Injection")
    print("="*60)
    
    core = TrinityCoreStream()
    core.add_extension(StateInjector("universe", "mathematical"))
    core.add_extension(StateInjector("dimension", 42))
    core.add_extension(EquationTransformer())
    
    print(f"Stream state: {core.state}")
    out = core.stream("∫ L dt")
    print(out)


def example_complex_pipeline():
    """Complex example with full pipeline."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Complex Pipeline")
    print("="*60)
    
    core = TrinityCoreStream()
    
    # Add multiple extensions
    core.add_extension(StateInjector("framework", "TrinityOne"))
    core.add_extension(SymbolicLogger(log_prefix="[STEP]"))
    core.add_extension(IntegralExpander())
    core.add_extension(EquationTransformer())
    
    # Process multiple inputs
    inputs = ["∫ L dt", "∂Ψ/∂t", "δS = 0"]
    
    for input_signal in inputs:
        print(f"\nProcessing: {input_signal}")
        result = core.stream(input_signal)
        print(f"Result: {result}")
    
    print(f"\nFinal state: {core.state}")


if __name__ == "__main__":
    print("\n" + "█"*60)
    print("  TRINITYONE STREAMING ARCHITECTURE DEMONSTRATIONS")
    print("█"*60)
    
    # Run all examples
    example_basic()
    example_multiple_extensions()
    example_with_logging()
    example_with_state()
    example_complex_pipeline()
    
    print("\n" + "="*60)
    print("All examples completed successfully!")
    print("="*60 + "\n")
