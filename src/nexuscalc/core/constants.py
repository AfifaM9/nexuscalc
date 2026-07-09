"""Mathematical constants."""

import math

class Constants:
    """Collection of mathematical constants."""
    
    PI = math.pi
    E = math.e
    TAU = math.tau
    INF = float('inf')
    NAN = float('nan')
    
    @classmethod
    def get_constant(cls, name):
        """Get a constant by name."""
        constants = {
            'pi': cls.PI,
            'e': cls.E,
            'tau': cls.TAU,
            'inf': cls.INF,
            'infinity': cls.INF,
            'nan': cls.NAN
        }
        return constants.get(name.lower())
    
    @classmethod
    def list_constants(cls):
        """List all available constants."""
        return ['pi', 'e', 'tau', 'inf', 'nan']
