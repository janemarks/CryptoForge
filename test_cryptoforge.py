# test_cryptoforge.py
"""
Tests for CryptoForge module.
"""

import unittest
from cryptoforge import CryptoForge

class TestCryptoForge(unittest.TestCase):
    """Test cases for CryptoForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoForge()
        self.assertIsInstance(instance, CryptoForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
