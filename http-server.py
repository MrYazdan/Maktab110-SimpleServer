from http.server import BaseHTTPRequestHandler, HTTPServer

home_html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>⭐ Maktab110 ⭐</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div class="bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-emerald-500 to-90% fixed inset-0 flex justify-center items-center">
        <h1 class="font-bold text-6xl text-white">Maktab 110</h1>
    </div>
</body>
</html>
"""


class Server(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(home_html, "utf-8"))


if __name__ == '__main__':
    host = "maktab110.ir"
    port = 80

    server = HTTPServer((host, port), Server)
    print(f"Server run in http://{host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
