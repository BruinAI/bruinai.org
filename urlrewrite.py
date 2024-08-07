import sys

def process_html(file_path):
  content = ''
  print(f'Processing {file_path}')
  
  with open(file_path, 'r') as f:
    content = f.read()

    # use javascript window to perform a URL rewrite
    # essentially if user requests /about.html, it will show /about in the URL bar
    new_path = file_path.replace("./", "")
    if 'index.html' in file_path:
      content = content.replace('</head>', "<script>if (window.location.pathname === '/index.html') {window.history.pushState({}, '', '/')};</script></head>")
    else:
      content = content.replace('</head>', f"<script>if (window.location.pathname === '/{new_path}') {{window.history.pushState({{}}, '', '/{new_path[:-5]}')}};</script></head>")

  with open(file_path, 'w') as f:
    f.write(content)
          

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python process_html.py <file_path>")
    sys.exit(1)
  process_html(sys.argv[1])
