from fastmcp import FastMCP
from duckduckgo_search import DDGS

# Create an MCP server
mcp = FastMCP("Online Search Tool")


@mcp.tool()
def duck_search(query: str, max_results: int = 5, region: str = 'wt-wt', safesearch: str = None) -> dict:
    """
    This tool can search the web using DuckDuckGo.
    Args:
        query: Search query string
        max_results: Number of results to return (default: 5)
        region: Region code for search (default: 'wt-wt' for worldwide)
        safesearch: Safe search level ('off', 'moderate', 'strict' or None)
    """
    try:
        with DDGS() as ddgs:
            results = ddgs.text(
                query,
                region=region,
                safesearch=safesearch,
                max_results=max_results
            )
            results_list = list(results)
            
            return {
                "success": True,
                "query": query,
                "results": results_list
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": f"Error occurred: {str(e)}"
        }