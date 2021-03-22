convertlist = [
  ["STOCK", "STONK"],
  ["ARMY", "ARMMEY"],
  ["RUIN", "ROUN"],
  ["SCRATCH", "SCRTACH"],
  ["SINCE", "SINSE"],
  ["2020", "2069"],
  ["2021", "2069"],
  ["LET'S", "LESS"],
  ["FOLLOW", "FOLO"],
  # suffixes go at the bottom of the list
  ["ING", "IN"]
]

while True:
  texttostonk = input("type some text to become stonked: ")
  stonkedtext = texttostonk.upper()
  for stonkedword in convertlist:
    stonkedtext = stonkedtext.replace(stonkedword[0], stonkedword[1])
  print(stonkedtext)