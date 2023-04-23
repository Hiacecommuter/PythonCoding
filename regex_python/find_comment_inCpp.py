import re
import sys
content = sys.stdin.read()
text = '\n'.join(re.findall(r'/\*[^/]*\*/|//[^\n]*)', content, re.DOTALL))
print(re.sub(r'\n\s+', '\n', text))
