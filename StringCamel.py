from re import sub

def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  s=s.replace("*","")
  return ''.join([s[0].upper(), s[1:]])
  
print(camel_case("Cats AND*Dogs-are Awesome"))
