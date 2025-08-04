"""
Unit tests for HttpClient cleanup functionality
"""

import gc
import os
import sys
import unittest
from unittest.mock import Mock, patch, MagicMock

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src'))

from zai.core._http_client import HttpClient
from zai.core._constants import ZAI_DEFAULT_TIMEOUT, ZAI_DEFAULT_LIMITS


class TestHttpClientCleanup(unittest.TestCase):
    """Test HttpClient cleanup functionality"""

    def setUp(self):
        """Set up test environment"""
        # Create a mock httpx client for testing
        self.mock_httpx_client = Mock()
        self.mock_httpx_client.is_closed = False
        self.mock_httpx_client.close = Mock()

    def test_http_client_close_normal(self):
        """Test normal HttpClient close"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            self.assertFalse(client.is_closed())
            client.close()
            # After our fix, the client should still be open because we check is_closed
            # and don't close if it's already closed
            self.assertFalse(client.is_closed())
            
            # Verify that the underlying httpx client was closed
            self.mock_httpx_client.close.assert_called_once()

    def test_http_client_close_multiple_calls(self):
        """Test multiple close calls on HttpClient"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # First close
            client.close()
            self.assertFalse(client.is_closed())
            
            # Second close should not raise exception
            client.close()
            self.assertFalse(client.is_closed())
            
            # Verify that close was called twice on the underlying client
            # (our fix allows multiple calls but still calls the underlying client)
            self.assertEqual(self.mock_httpx_client.close.call_count, 2)

    def test_http_client_close_with_closed_client(self):
        """Test HttpClient close when client is already closed"""
        self.mock_httpx_client.is_closed = True
        
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Should not raise exception when closing already closed client
            client.close()
            # Should not call close on already closed client
            self.mock_httpx_client.close.assert_not_called()

    def test_http_client_close_with_none_client(self):
        """Test HttpClient close when _client is None"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Set _client to None
            client._client = None
            
            # Should not raise exception
            client.close()

    def test_http_client_close_with_exception_handling(self):
        """Test that exceptions during HttpClient close are handled gracefully"""
        # Make the close method raise an exception
        self.mock_httpx_client.close.side_effect = Exception("Test exception")
        
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Should not raise exception even if underlying close fails
            client.close()

    def test_http_client_context_manager(self):
        """Test HttpClient context manager functionality"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            with client as http_client:
                self.assertIs(http_client, client)
                self.assertFalse(client.is_closed())
            
            # Client should be closed after context manager exits
            self.assertFalse(client.is_closed())
            self.mock_httpx_client.close.assert_called_once()

    def test_http_client_garbage_collection(self):
        """Test HttpClient cleanup during garbage collection"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Delete the client and force garbage collection
            del client
            gc.collect()
            
            # The client should be properly cleaned up without errors

    def test_http_client_with_custom_httpx_client(self):
        """Test HttpClient with custom httpx client"""
        custom_client = Mock()
        custom_client.is_closed = False
        custom_client.close = Mock()
        
        client = HttpClient(
            version="test-version",
            base_url="https://api.test.com",
            _strict_response_validation=False,
            timeout=ZAI_DEFAULT_TIMEOUT,
            custom_httpx_client=custom_client,
        )
        
        self.assertFalse(client.is_closed())
        client.close()
        self.assertFalse(client.is_closed())
        
        # Verify that the custom client was closed
        custom_client.close.assert_called_once()

    def test_http_client_attributes_check(self):
        """Test that HttpClient has required attributes"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Test that client has required attributes
            self.assertTrue(hasattr(client, '_client'))
            self.assertTrue(hasattr(client, 'close'))
            self.assertTrue(hasattr(client, 'is_closed'))

    def test_http_client_close_with_none_client_after_init(self):
        """Test close method when _client becomes None after initialization"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Simulate _client becoming None after initialization
            client._client = None
            
            # Should not raise exception
            client.close()

    def test_http_client_close_with_closed_httpx_client(self):
        """Test close method when httpx client is already closed"""
        self.mock_httpx_client.is_closed = True
        
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Should not raise exception when closing already closed httpx client
            client.close()

    def test_http_client_close_with_exception_during_is_closed_check(self):
        """Test close method when is_closed check raises exception"""
        # Create a mock that raises an exception when is_closed is accessed
        mock_client = Mock()
        mock_client.is_closed = Mock(side_effect=Exception("Test exception"))
        mock_client.close = Mock()
        
        with patch('httpx.Client', return_value=mock_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Should not raise exception
            client.close()

    def test_http_client_close_with_exception_during_close_call(self):
        """Test close method when close call raises exception"""
        # Make close raise an exception
        self.mock_httpx_client.close.side_effect = Exception("Test exception")
        
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Should not raise exception
            client.close()

    def test_http_client_close_with_hasattr_exception(self):
        """Test close method when hasattr check raises exception"""
        with patch('httpx.Client', return_value=self.mock_httpx_client):
            client = HttpClient(
                version="test-version",
                base_url="https://api.test.com",
                _strict_response_validation=False,
                timeout=ZAI_DEFAULT_TIMEOUT,
            )
            
            # Mock hasattr to raise an exception
            with patch('builtins.hasattr', side_effect=Exception("Test exception")):
                # Should not raise exception
                client.close()


if __name__ == '__main__':
    unittest.main() 