from .wurds import convertlist

while True:
  texttostonk = input("type some text to become stonked: ")
  stonkedtext = texttostonk.upper()
  for stonkedword in convertlist:
    stonkedtext = stonkedtext.replace(stonkedword[0], stonkedword[1])
  print(stonkedtext)