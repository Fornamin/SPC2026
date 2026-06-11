# pip install mcp

from mcp.server.fastmcp import FastMCP
from mcp import ClientSession
from importlib.metadata import version
import inspect

print(f"MCP Version: {version('mcp')}")

print('\nMCP Document\n')
print(inspect.getdoc(FastMCP))
print(inspect.getdoc(FastMCP.sse_app))

print('\nMCP Session Management')
print(inspect.getdoc(ClientSession))
print(inspect.getdoc(ClientSession.initialize))