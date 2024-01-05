from mitmproxy import ctx, http

def request(flow: http.HTTPFlow) -> None:
    
    ctx.log.info(f"Intercepted request to {flow.request.url}")
    
    # MODIFY REQUEST HEADERS
    flow.request.headers["User-Agent"] = "Custom User Agent"
    
def response(flow: http.HTTPFlow) -> None:
    #Handle response before sent back to android
    
    ctx.log.info(f"Intercepted response from {flow.request.url}")
    
    # Example modif response
    flow.response.content.replace(b"Hello", b"Hacked")
    
if __name__ == "__main__":
    
    #use -p to specify the listening pot e.gg (8080)
    #use --ssl-insecure to igonre SSL certificate errors
    mitmproxy_cmd = "mitmproxy -s android_mitm_tool.py"
    print(f"Run the following command in your terminal:\n\n{mitmproxy_cmd}")