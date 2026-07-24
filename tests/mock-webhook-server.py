#!/usr/bin/env python3
"""Simple HTTP server that accepts POST requests and returns 200 OK.
Used as a mock Slack webhook endpoint for testing."""
import http.server
import sys

class MockWebhookHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        self.rfile.read(length)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'ok')

    def log_message(self, format, *args):
        pass  # suppress output

port = int(sys.argv[1]) if len(sys.argv) > 1 else 18765
server = http.server.HTTPServer(('127.0.0.1', port), MockWebhookHandler)
server.serve_forever()
