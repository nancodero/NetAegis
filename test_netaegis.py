# test_netaegis.py
"""
Tests for NetAegis module.
"""

import unittest
from netaegis import NetAegis

class TestNetAegis(unittest.TestCase):
    """Test cases for NetAegis class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NetAegis()
        self.assertIsInstance(instance, NetAegis)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NetAegis()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
