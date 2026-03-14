# test_cryptowalletkit.py
"""
Tests for CryptoWalletKit module.
"""

import unittest
from cryptowalletkit import CryptoWalletKit

class TestCryptoWalletKit(unittest.TestCase):
    """Test cases for CryptoWalletKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoWalletKit()
        self.assertIsInstance(instance, CryptoWalletKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoWalletKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
