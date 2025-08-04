"""
Unit tests for client cleanup functionality
"""

import gc
import os
import sys
import unittest
from unittest.mock import Mock, patch

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from zai import ZaiClient, ZhipuAiClient
from zai.core._errors import ZaiError


class TestClientCleanup(unittest.TestCase):
    """Test client cleanup functionality"""

    def setUp(self):
        """Set up test environment"""
        # Set a dummy API key for testing
        os.environ['ZAI_API_KEY'] = 'test-api-key'
        self.original_api_key = os.environ.get('ZAI_API_KEY')

    def tearDown(self):
        """Clean up test environment"""
        if self.original_api_key:
            os.environ['ZAI_API_KEY'] = self.original_api_key
        elif 'ZAI_API_KEY' in os.environ:
            del os.environ['ZAI_API_KEY']

    def test_context_manager_cleanup(self):
        """Test that context manager properly cleans up the client"""
        with ZaiClient() as client:
            self.assertIsNotNone(client)
            self.assertFalse(client.is_closed())
        
        # Client should be closed after context manager exits
        self.assertTrue(client.is_closed())

    def test_explicit_close(self):
        """Test explicit client close"""
        client = ZaiClient()
        self.assertFalse(client.is_closed())
        
        client.close()
        self.assertTrue(client.is_closed())

    def test_multiple_close_calls(self):
        """Test that multiple close calls don't cause errors"""
        client = ZaiClient()
        client.close()
        self.assertTrue(client.is_closed())
        
        # Second close should not raise an exception
        client.close()
        self.assertTrue(client.is_closed())

    def test_garbage_collection_cleanup(self):
        """Test that garbage collection properly cleans up the client"""
        client = ZaiClient()
        client_ref = client
        
        # Delete the reference and force garbage collection
        del client
        gc.collect()
        
        # The client should be properly cleaned up without errors

    def test_multiple_clients_cleanup(self):
        """Test cleanup of multiple clients"""
        clients = []
        for i in range(5):
            client = ZaiClient()
            clients.append(client)
        
        # Close all clients
        for client in clients:
            client.close()
            self.assertTrue(client.is_closed())
        
        # Delete all clients and force garbage collection
        del clients
        gc.collect()

    def test_client_with_custom_http_client(self):
        """Test cleanup when using custom HTTP client"""
        import httpx
        
        custom_client = httpx.Client()
        client = ZaiClient(http_client=custom_client)
        
        # Should close custom HTTP client when we call close()
        client.close()
        self.assertTrue(custom_client.is_closed)
        
        # Clean up custom client (it's already closed)
        # custom_client.close()  # No need to close again

    def test_client_initialization_failure(self):
        """Test cleanup when client initialization fails"""
        # Remove API key to cause initialization failure
        if 'ZAI_API_KEY' in os.environ:
            del os.environ['ZAI_API_KEY']
        
        with self.assertRaises(ZaiError):
            ZaiClient()
        
        # Should not cause cleanup errors during garbage collection
        gc.collect()

    def test_client_with_none_client(self):
        """Test cleanup when _client is None"""
        client = ZaiClient()
        
        # Manually set _client to None to simulate edge case
        client._client = None
        
        # Should not raise exception
        client.close()

    def test_client_with_closed_client(self):
        """Test cleanup when client is already closed"""
        client = ZaiClient()
        client.close()
        
        # Should not raise exception when closing already closed client
        client.close()

    @patch('httpx.Client.close')
    def test_client_close_exception_handling(self, mock_close):
        """Test that exceptions during close are handled gracefully"""
        # Make the close method raise an exception
        mock_close.side_effect = Exception("Test exception")
        
        client = ZaiClient()
        
        # Should not raise exception even if underlying close fails
        client.close()

    def test_zhipu_client_cleanup(self):
        """Test cleanup for ZhipuAiClient"""
        with ZhipuAiClient() as client:
            self.assertIsNotNone(client)
            self.assertFalse(client.is_closed())
        
        # Client should be closed after context manager exits
        self.assertTrue(client.is_closed())

    def test_client_attributes_check(self):
        """Test that client checks for required attributes before cleanup"""
        client = ZaiClient()
        
        # Test that client has required attributes
        self.assertTrue(hasattr(client, '_has_custom_http_client'))
        self.assertTrue(hasattr(client, 'close'))
        self.assertTrue(hasattr(client, '_client'))

    def test_client_del_without_initialization(self):
        """Test __del__ method when client is not properly initialized"""
        # Create a client but manually remove attributes to simulate partial initialization
        client = ZaiClient()
        
        # Remove required attributes
        if hasattr(client, '_has_custom_http_client'):
            delattr(client, '_has_custom_http_client')
        
        # Should not raise exception during garbage collection
        del client
        gc.collect()

    def test_client_del_with_custom_http_client(self):
        """Test __del__ method when using custom HTTP client"""
        import httpx
        
        custom_client = httpx.Client()
        client = ZaiClient(http_client=custom_client)
        
        # Should not close custom HTTP client during garbage collection
        # because _has_custom_http_client is True
        del client
        gc.collect()
        
        # Custom client should still be open because __del__ doesn't close it
        self.assertFalse(custom_client.is_closed)
        custom_client.close()

    def test_client_close_with_none_client_after_init(self):
        """Test close method when _client becomes None after initialization"""
        client = ZaiClient()
        
        # Simulate _client becoming None after initialization
        client._client = None
        
        # Should not raise exception
        client.close()

    def test_client_close_with_closed_httpx_client(self):
        """Test close method when httpx client is already closed"""
        client = ZaiClient()
        
        # Close the underlying httpx client
        client._client.close()
        
        # Should not raise exception when closing already closed httpx client
        client.close()


if __name__ == '__main__':
    unittest.main() 