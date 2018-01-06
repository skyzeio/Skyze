''' Printing helpers'''


def style(message, style):
  return style + message + '\033[0m'


def green(message):
  return style(message, '\033[92m')


def blue(message):
  return style(message, '\033[94m')


def yellow(message):
  return style(message, '\033[93m')


def red(message):
  return style(message, '\033[91m')


def pink(message):
  return style(message, '\033[95m')


def bold(message):
  return style(message, '\033[1m')


def underline(message):
  return style(message, '\033[4m')


def prt(*args):
  print(' '.join([str(arg) for arg in args]))


def openingTitles():
  title = "\n\n\n\n"
  title += "\n     ssss       kkkk     kkkk  yyyy          yyyy   zzzzzzzzzzzz  eeeeeeeeeeeee"
  title += "\n  ssss  ssss    kkkk    kkkk     yyyy      yyyy    zzzzzzzzzzzz   eeeeeeeeeeeee"
  title += "\n   ssss         kkkk  kkkk         yyyy  yyyy            zzzz     eeee "
  title += "\n     ssss       kkkkkkkk            yyyyyyyy            zzzz      eeeeeeeeeeeee "
  title += "\n      ssss      kkkkkkkk              yyyy            zzzz        eeeeeeeeeeeee "
  title += "\n       ssss     kkkk  kkkk            yyyy          zzzz          eeee"
  title += "\n  ssss  ssss    kkkk    kkkk          yyyy        zzzzzzzzzzzzz   eeeeeeeeeeeee"
  title += "\n     ssss       kkkk      kkkk        yyyy         zzzzzzzzzzzzz  eeeeeeeeeeeee"
  title += "\n\n\n\n"
