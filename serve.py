import http.server, socketserver, os
os.chdir('/Users/pulasthiranawaka/Desktop/Claude/RK')
with socketserver.TCPServer(("", 3000), http.server.SimpleHTTPRequestHandler) as s:
    print("Serving on http://localhost:3000")
    s.serve_forever()
