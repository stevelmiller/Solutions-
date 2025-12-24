"""
Example extensions for TrinityCore Stream.

This module contains example extensions that demonstrate how to create
secure, validated extensions for the streaming architecture.
"""

from trinity_core import SecureExtension


class EquationTransformer(SecureExtension):
    """
    Mathematical thought transformer that processes symbolic equations.
    
    Transforms input into a differential representation: Ψ' = dΨ/dt
    """
    
    def mutate(self, data):
        """
        Transform data into differential equation format.
        
        Args:
            data: Input expression (e.g., "∫ L dt")
            
        Returns:
            Transformed expression in Ψ' format
        """
        return f"Ψ' = dΨ/dt (received: {data})"


class IntegralExpander(SecureExtension):
    """
    Expands integral expressions into their component parts.
    """
    
    def mutate(self, data):
        """
        Expand integral notation.
        
        Args:
            data: Input with potential integral notation
            
        Returns:
            Expanded form
        """
        if "∫" in data:
            return data.replace("∫", "integral of ")
        return data


class SymbolicLogger(SecureExtension):
    """
    Logs symbolic transformations for debugging and analysis.
    """
    
    def __init__(self, log_prefix="[LOG]"):
        """
        Initialize logger with optional prefix.
        
        Args:
            log_prefix: Prefix for log messages
        """
        self.log_prefix = log_prefix
        self.log_history = []
    
    def inject(self, host_state):
        """Inject log history into host state."""
        host_state['log_history'] = self.log_history
    
    def mutate(self, data):
        """
        Log the data as it passes through the stream.
        
        Args:
            data: Data to log
            
        Returns:
            Unmodified data (logging doesn't transform)
        """
        log_entry = f"{self.log_prefix} {data}"
        self.log_history.append(log_entry)
        print(log_entry)
        return data


class StateInjector(SecureExtension):
    """
    Injects custom state into the host stream.
    """
    
    def __init__(self, key, value):
        """
        Initialize with key-value pair to inject.
        
        Args:
            key: State key
            value: State value
        """
        self.key = key
        self.value = value
    
    def inject(self, host_state):
        """Inject the configured state into host."""
        host_state[self.key] = self.value
        print(f"Injected state: {self.key} = {self.value}")
