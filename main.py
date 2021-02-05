import time, os, sys, re
red = "\033[0;91m"
w = "\033[0;37m"
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'
pink='\033[95m'
read_line = 0
console = 0
mathsa = 0
num1 = 0
num2 = 0
def sp(text):
  words = text
  for char in words:
    time.sleep(0.04)
    sys.stdout.write(char)
    sys.stdout.flush()
var1 = "Undefined variable"
input1 = "Undefined input"
input2 = "Undefined input"
input3 = "Undefined input"
line = 0
read_line = 0
def sppi():
  try:
    if console == 1:
      spl_word = '  sp("'
      res = lines.partition(spl_word)[2]
      res = res.replace('$n', '\n')
      res = res.replace('\')', '')
      res = res.replace('{red}', red)
      res = res.replace('{end}', end)
      res = res.replace('{blue}', blue)
      res = res.replace('{bold}', bold)
      res = res.replace('{green}', green)
      res = res.replace('{magenta}', magenta)
      res = res.replace('{cyan}', cyan)
      res = res.replace('{yellow}', yellow)
      res = res.replace('{white}', w)
      res = res.replace('{black}', black)
      res = res.replace('{pink}', pink)
      res = res.replace("{{input1}}", input1)
      res = res.replace("{{input2}}", input2)
      res = res.replace("{{input3}}", input3)
      res = res.replace('"', "")
      res = res.replace(")", "")
      res = res.replace("{{var1}}", var1)
      split_string = res.split("\")", -1)
      res = split_string[0]
      sp(res)
      read_line = 1
  except:
    pass
maths = 0
def logli():
  try:
    if '")' in lines:
      spl_word = '  window.out.ln("'
      res = lines.partition(spl_word)[2]
      res = res.replace('$n', '\n')
      res = res.replace('\')', '')
      res = res.replace('{red}', red)
      res = res.replace('{end}', end)
      res = res.replace('{blue}', blue)
      res = res.replace('{bold}', bold)
      res = res.replace('{green}', green)
      res = res.replace('{magenta}', magenta)
      res = res.replace('{cyan}', cyan)
      res = res.replace('{yellow}', yellow)
      res = res.replace('{white}', w)
      res = res.replace('{black}', black)
      res = res.replace('{pink}', pink)
      res = res.replace('"', "")
      res = res.replace(")", "")
      res = res.replace("{{input1}}", input1)
      res = res.replace("{{input2}}", input2)
      res = res.replace("{{input3}}", input3)
      res = res.replace("{{var1}}", var1)
      split_string = res.split("\")", -1)
      res = split_string[0]
      print(res)
      read_line = 1
    else:
      pass
  except:
    pass 
def logi():
  if '")' in lines:
    spl_word = '  window.out("'
    res = lines.partition(spl_word)[2]
    res = res.replace('$n', '\n')
    res = res.replace('\')', '')
    split_string = res.split("\")", -1)
    res = split_string[0]
    print(res, end ="")
    read_line = 1
  else:
    pass
def spp():
            if console == 1:
              spl_word = 'window.sp("'
              res = lines.partition(spl_word)[2]
              res = res.replace('$n', '\n')
              res = res.replace('\')', '')
              res = res.replace('{red}', red)
              res = res.replace('{end}', end)
              res = res.replace('{blue}', blue)
              res = res.replace('{bold}', bold)
              res = res.replace('{green}', green)
              res = res.replace('{magenta}', magenta)
              res = res.replace('{cyan}', cyan)
              res = res.replace('{yellow}', yellow)
              res = res.replace('{white}', w)
              res = res.replace('{black}', black)
              res = res.replace('{pink}', pink)
              res = res.replace("{{input1}}", input1)
              res = res.replace("{{input2}}", input2)
              res = res.replace("{{input3}}", input3)
              res = res.replace('"', "")
              res = res.replace(")", "")
              res = res.replace("{{var1}}", var1)
              split_string = res.split("\")", -1)
              res = split_string[0]
              sp(res)
              read_line = 0




def logl():
    try:
      if '")' in lines:
        spl_word = 'window.out.ln("'
        res = lines.partition(spl_word)[2]
        res = res.replace('$n', '\n')
        res = res.replace('\')', '')
        res = res.replace('{red}', red)
        res = res.replace('{end}', end)
        res = res.replace('{blue}', blue)
        res = res.replace('{bold}', bold)
        res = res.replace('{green}', green)
        res = res.replace('{magenta}', magenta)
        res = res.replace('{cyan}', cyan)
        res = res.replace('{yellow}', yellow)
        res = res.replace('{white}', w)
        res = res.replace('{black}', black)
        res = res.replace('{pink}', pink)
        res = res.replace('"', "")
        res = res.replace("  ", " ")
        res = res.replace(")", "")
        res = res.replace("{{input1}}", input1)
        res = res.replace("{{input2}}", input2)
        res = res.replace("{{input3}}", input3)
        res = res.replace("{{var1}}", var1)
        split_string = res.split("\")", -1)
        res = split_string[0]
        print(res)
        read_line = 0
      else:
        errors()
    except:
      pass 
def log():
    if '")' in lines:
      spl_word = 'window.out("'
      res = lines.partition(spl_word)[2]
      res = res.replace('$n', '\n')
      res = res.replace('\')', '')
      split_string = res.split("\")", -1)
      res = split_string[0]
      print(res, end ="")
      read_line = 0
    else:
      errors()
red = "\033[0;31m"
bold = '\033[1m'

f =  open('main.ds') 

for lines in f.readlines():
        def errors():
          if "windowout" in lines:
            os.system("clear")
            print(red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~" + yellow + bold + "\n[syntax error in line " + str(line) + "]:" + red + bold + red + bold + "\nwindowout is not defined. Did you mean: 'window.out' or 'window.out.ln'")
          elif "window.out" in lines:
            os.system("clear")
            print(red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~" + yellow + bold + "\n[print error on line " + str(line) + "]:" + red + bold + red + bold + "\nwindow.out is a function but no text was found. Please insert text line this: `window.out(\"Hello World\")` next time")
        line += 1
        lines = lines.replace('\n','')
        lines = lines.replace('\t','')
        if lines == "":
          pass  
        elif "??" in lines:
          pass 
        if '??' in lines:
          pass
          read_line = 0
        elif 'window.sleep(' in lines:
                  spl_word = 'window.sleep('
                  res = lines.partition(spl_word)[2]
                  split_string = res.split(")", -1)
                  res.replace(')', '')
                  res = split_string[0]
                  time.sleep(float(res))
        elif 'do + >num1{' in lines:
          if '}' in lines:
            spl_word = 'do + >num1{'
            res = lines.partition(spl_word)[2]
            split_string = res.split(")", -1)
            res.replace(')', '')
            res = split_string[0]
            res = res.replace("}", "")
            num1 = res
            num1 = float(num1)
        elif 'do + >num2{' in lines:
          if '}' in lines:
            spl_word = 'do + >num2{'
            res = lines.partition(spl_word)[2]
            split_string = res.split(")", -1)
            res.replace(')', '')
            res = split_string[0]
            res = res.replace("}", "")
            num2 = res
            num2 = float(num2)
        elif 'do {num1+num2}' in lines:
          print(float(num1) + float(num2))
          nums = float(num1) + float(num2)
        if lines == "};":
          pass
        elif lines == "import console.commands.*" :
          console = 1
        elif 'if (input1 is "' in lines:
          spl_word = "if (input1 is \""
          sun = lines.partition(spl_word)[2]
          split_string = sun.split("\")", -1)
          sun.replace(')', '')
          sun.replace('\"', '')
          sun.replace(')', '')
          sun = split_string[0]
          if input1 == sun:
            if '{;' in lines:
              read_line = 1
          else:
            pass
        elif '   ' in lines:
          if read_line == 1:
            if '   ' in lines:
              sppi()
              logli()
              logi()
          else:
            continue
        
        elif '};' in lines:
            read_line = 0
        elif 'window.in(input1) => ("' in lines:
          spl_word = "window.in(input1) => (\""
          sun = lines.partition(spl_word)[2]
          split_string = sun.split("\")", -1)
          sun.replace(')', '')
          sun.replace('\"', '')
          sun = split_string[0]
          input1 = input(sun)
        elif 'window.in(input2) => (' in lines:
          spl_word = "window.in(input2) => ("
          sun = lines.partition(spl_word)[2]
          split_string = sun.split(")", -1)
          sun.replace(')', '')
          sun.replace('"', '')
          sun = split_string[0]
          input2 = input(sun)
        elif 'window.in(input3) => (' in lines:
          spl_word = "window.in(input3) => ("
          sun = lines.partition(spl_word)[2]
          split_string = sun.split(")", -1)
          sun.replace(')', '')
          sun.replace('"', '')
          sun = split_string[0]
          input3 = input(sun)
        elif 'window.in(input1)' in lines:
          input1 = input()
        elif 'window.in(input2)' in lines:
          input2 = input(sun)
        elif 'window.in(input3)' in lines:
          input3 = input(sun)
        elif "window.sp(\"" in lines:
          spp()
        elif 'window.out.ln("' in lines:
          if 'window.out.ln("' in lines:
            logl() 
        elif 'window.out' in lines:
          log()
        elif 'var1 = ' in lines:
          spl_word = "var1 = "
          res = lines.partition(spl_word)[2]
          split_string = res.split(")", -1)
          res = split_string[0]
          var1 = res
          try:
            var1 = float(var1)
          except:
            var1 = str(var1)
        elif 'system(' in lines:
          if ')' in lines:
              spl_word = 'system('
              res = lines.partition(spl_word) [2]
              split_string = res.split(")", -1)
              res.replace(')', '')
              res = split_string[0]
              os.system(res)
        elif "window.erase()" in lines:
          os.system('clear;echo 0')
        else:

            errors()