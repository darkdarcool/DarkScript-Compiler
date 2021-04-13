import time, os, sys, re
from datetime import date
jb = 0
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
pink = '\033[95m'
read_line = 0
console = 0
today = date.today()
print("What is file path?")
file_path = input("")
if '.ds' in file_path:
  pass
else:
  raise Exception(f"{file_path} is not a DarkScript code file")
try:
  file = open(f"{file_path}","r")
except:
  raise Exception("No file in file path " + file_path + "!")
os.system("clear")
print("Darkscript 1.0.2(early release)(" + str(today) + ")")
Counter = 0
  
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
load = 0
for i in CoList: 
    if i:
        load += 1

while (True):
  sun = input()
  if "run-project" in sun:
    while (" " in sun):
      sun = sun.replace(" ", "")
    if sun == "run-project":
      break
  elif "darkscript main.ds" in sun:
    while (" " in sun):
      sun = sun.replace(" ", "")
    if sun == "darkscriptmain.ds":
      break
  elif "ds main.ds" in sun:
    while (" " in sun):
      sun = sun.replace(" ", "")
    if sun == "dsmain.ds":
      break
  if "run" in sun:
    while (" " in sun):
      sun = sun.replace(" ", "")
    if sun == "run":
      break
  if "ds install jb" in sun:
      print("Installed JB module.")
      jb = 1
  elif "clear" in sun:
    while (" " in sun):
      sun = sun.replace(" ", "")
    if sun == "clear":
      os.system("clear")
      print("Darkscript 1.0.2(early release)(" + str(today) + ")")
    else:
      os.system(str(sun))
  else:
    os.system(str(sun))
mathsa = 0
num1 = 0
num = 0
print("Compiling script")
while (num < load):
  print("Compiling... /")
  time.sleep(0.08)
  os.system("clear")
  print("Compiling... -")
  time.sleep(0.08)
  os.system("clear")
  print("Compiling... \ ")
  time.sleep(0.08)
  os.system("clear")
  num += 1

num2 = 0
getChar1 = "none"
getChar2 = "none"
getChar3 = "none"
df = 10
c = -1
red = "\033[0;91m"
w = "\033[0m"
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
pink = '\033[95m'
allvars = {}
def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)
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
            res = res.replace('{getChar1}', getChar1)
            res = res.replace('{getChar2}', getChar2)
            res = res.replace('{getChar3}', getChar3)
            res = res.replace('{blue}', blue)
            res = res.replace('{bold}', bold)
            res = res.replace('{end}', '\033[0m')

            res = res.replace('{green}', green)
            res = res.replace('{magenta}', magenta)
            res = res.replace('{cyan}', cyan)
            
            if "{{" in res:
                if "}}" in res:
                    start = "{{"
                    end = "}}"
                    check = res[res.find(start) + len(start):res.rfind(end)]
                    if check in allvars:
                        res = res.replace("{{", "")
                        res = res.replace("}}", "")
                        dffdfdfdf = allvars[check]
                        res = res.replace(check, str(dffdfdfdf))
                    else:
                        os.system("clear")
                        print(red + bold + str(lines) + "\n" + green +
                              "^~~~~~~~~~~~~" + yellow + bold +
                              "\n[Varaible error on line " + str(line) + "]:" +
                              red + bold + "\n" + sun +
                              " is not a varaible. Please create " + sun +
                              " a varaiable. To use it in inputs")
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
            # read_line = 1
    except:
        pass
read = 1
maths = 0
def logli():
    try:
        if '")' in lines:
            spl_word = '  window.out.ln("'
            res = lines.partition(spl_word)[2]
            res = res.replace('$n', '\n')
            res = res.replace('\')', '')
            res = res.replace('{red}', red)
            res = res.replace('{end}', '\033[0m')
            res = res.replace('{blue}', blue)
            res = res.replace('{bold}', bold)
            res = res.replace('{green}', green)
            res = res.replace('{magenta}', magenta)
            res = res.replace('{cyan}', cyan)
            res = res.replace('{yellow}', yellow)
            res = res.replace('{white}', w)
            res = res.replace('{black}', black)
            res = res.replace('{pink}', pink)
            if "{{" in res:
                if "}}" in res:
                    start = "{{"
                    end = "}}"
                    check = res[res.find(start) + len(start):res.rfind(end)]
                    if check in allvars:
                        res = res.replace("{{", "")
                        res = res.replace("}}", "")
                        dffdfdfdf = allvars[check]
                        res = res.replace(check, str(dffdfdfdf))
                    else:
                        os.system("clear")
                        print(red + bold + str(lines) + "\n" + green +
                              "^~~~~~~~~~~~~" + yellow + bold +
                              "\n[Varaible error on line " + str(line) + "]:" +
                              red + bold + "\n" + sun +
                              " is not a varaible. Please create " + sun +
                              " a varaiable. To use it in inputs")
            res = res.replace('{getChar1}', getChar1)
            res = res.replace('{getChar2}', getChar2)
            res = res.replace('{getChar3}', getChar3)
            res = res.replace('"', "")
            res = res.replace(")", "")
            res = res.replace("{{input1}}", input1)
            res = res.replace("{{input2}}", input2)
            res = res.replace("{{input3}}", input3)
            res = res.replace("{{var1}}", var1)
            split_string = res.split("\")", -1)
            res = split_string[0]
            print(res)
            # read_line = 1
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
        res = res.replace('$n', '\n')
        res = res.replace('\')', '')
        res = res.replace('{red}', red)
        res = res.replace('{blue}', blue)
        res = res.replace('{getChar1}', getChar1)
        res = res.replace('{getChar2}', getChar2)
        res = res.replace('{getChar3}', getChar3)
        res = res.replace('{bold}', bold)
        res = res.replace('{green}', green)
        res = res.replace('{magenta}', magenta)
        res = res.replace('{cyan}', cyan)
        res = res.replace('{yellow}', yellow)
        res = res.replace('{white}', w)
        res = res.replace('{black}', black)
        res = res.replace('{end}', '\033[0m')

        if "{{" in res:
            if "}}" in res:
                start = "{{"
                end = "}}"
                check = res[res.find(start) + len(start):res.rfind(end)]
                if check in allvars:
                    res = res.replace("{{", "")
                    res = res.replace("}}", "")
                    dffdfdfdf = allvars[check]
                    res = res.replace(check, str(dffdfdfdf))
                else:
                    os.system("clear")
                    print(red + bold + str(lines) + "\n" + green +
                          "^~~~~~~~~~~~~" + yellow + bold +
                          "\n[Varaible error on line " + str(line) + "]:" +
                          red + bold + "\n" + sun +
                          " is not a varaible. Please create " + sun +
                          " a varaiable. To use it in inputs")
        res = res.replace('{pink}', pink)
        res = res.replace('"', "")
        res = res.replace("  ", " ")
        res = res.replace(")", "")
        res = res.replace("{{input1}}", input1)
        res = res.replace("{{input2}}", input2)
        res = res.replace("{{input3}}", input3)
        res = res.replace("{{var1}}", var1)
        print(res, end="")
        # read_line = 1
    else:
        pass
def spp():
    if console == 1:
        spl_word = 'window.sp("'
        res = lines.partition(spl_word)[2]
        res = res.replace('$n', '\n')
        res = res.replace('\')', '')
        res = res.replace('{red}', red)
        res = res.replace('{blue}', blue)
        res = res.replace('{bold}', bold)
        res = res.replace('{green}', green)
        res = res.replace('{magenta}', magenta)
        res = res.replace('{getChar1}', getChar1)
        res = res.replace('{getChar2}', getChar2)
        res = res.replace('{getChar3}', getChar3)
        res = res.replace('{cyan}', cyan)
        res = res.replace('{yellow}', yellow)
        res = res.replace('{white}', w)
        res = res.replace('{black}', black)
        res = res.replace('{pink}', pink)
        res = res.replace('{end}', '\033[0m')
        res = res.replace("{{input1}}", input1)
        res = res.replace("{{input2}}", input2)
        res = res.replace("{{input3}}", input3)
        if "{{" in res:
            if "}}" in res:
                start = "{{"
                end = "}}"
                check = res[res.find(start) + len(start):res.rfind(end)]
                if check in allvars:
                    res = res.replace("{{", "")
                    res = res.replace("}}", "")
                    dffdfdfdf = allvars[check]
                    res = res.replace(check, str(dffdfdfdf))
                else:
                    os.system("clear")
                    print(red + bold + str(lines) + "\n" + green +
                          "^~~~~~~~~~~~~" + yellow + bold +
                          "\n[Varaible error on line " + str(line) + "]:" +
                          red + bold + "\n" + sun +
                          " is not a varaible. Please create " + sun +
                          " a varaiable. To use it in inputs")
        res = res.replace('"', "")
        res = res.replace(")", "")
        res = res.replace("{{var1}}", var1)
        split_string = res.split("\")", -1)
        res = split_string[0]
        sp(res)
        # read_line = 0
def sppj():
    if console == 1:
      if jb == 1:
        spl_word = 'slowwrite("'
        res = lines.partition(spl_word)[2]
        res = res.replace('$n', '\n')
        res = res.replace('\')', '')
        res = res.replace('{red}', red)
        res = res.replace('{blue}', blue)
        res = res.replace('{bold}', bold)
        res = res.replace('{green}', green)
        res = res.replace('{magenta}', magenta)
        res = res.replace('{getChar1}', getChar1)
        res = res.replace('{getChar2}', getChar2)
        res = res.replace('{getChar3}', getChar3)
        res = res.replace('{cyan}', cyan)
        res = res.replace('{yellow}', yellow)
        res = res.replace('{white}', w)
        res = res.replace('{black}', black)
        res = res.replace('{pink}', pink)
        res = res.replace('{end}', '\033[0m')
        res = res.replace("{{input1}}", input1)
        res = res.replace("{{input2}}", input2)
        res = res.replace("{{input3}}", input3)
        if "{{" in res:
            if "}}" in res:
                start = "{{"
                end = "}}"
                check = res[res.find(start) + len(start):res.rfind(end)]
                if check in allvars:
                    res = res.replace("{{", "")
                    res = res.replace("}}", "")
                    dffdfdfdf = allvars[check]
                    res = res.replace(check, str(dffdfdfdf))
                else:
                    os.system("clear")
                    print(red + bold + str(lines) + "\n" + green +
                          "^~~~~~~~~~~~~" + yellow + bold +
                          "\n[Varaible error on line " + str(line) + "]:" +
                          red + bold + "\n" + sun +
                          " is not a varaible. Please create " + sun +
                          " a varaiable. To use it in inputs")
        res = res.replace('"', "")
        res = res.replace(")", "")
        res = res.replace("{{var1}}", var1)
        split_string = res.split("\")", -1)
        res = split_string[0]
        sp(res)
        # read_line = 0
def loglj():  #add suggestion about lang or whatever, KK- dark
    try:
        if (jb == 1):
            if '")' in lines:
                spl_word = 'write("'
                res = lines.partition(spl_word)[2]
                res = res.replace('$n', '\n')
                res = res.replace('\')', '')
                res = res.replace('{red}', red)
                res = res.replace('{blue}', blue)
                res = res.replace('{getChar1}', getChar1)
                res = res.replace('{getChar2}', getChar2)
                res = res.replace('{getChar3}', getChar3)
                res = res.replace('{bold}', bold)
                res = res.replace('{green}', green)
                res = res.replace('{magenta}', magenta)
                res = res.replace('{cyan}', cyan)
                res = res.replace('{yellow}', yellow)
                res = res.replace('{white}', w)
                res = res.replace('{black}', black)
                res = res.replace('{pink}', pink)
                res = res.replace('{end}', '\033[0m')
                res = res.replace('"', "")
                res = res.replace("  ", " ")
                res = res.replace(")", "")
                res = res.replace("{{input1}}", input1)
                res = res.replace("{{input2}}", input2)
                res = res.replace("{{input3}}", input3)
                res = res.replace("{{var1}}", var1)
                if "{{" in res:
                    if "}}" in res:
                        start = "{{"
                        end = "}}"
                        check = res[res.find(start) +
                                    len(start):res.rfind(end)]
                        if check in allvars:
                            res = res.replace("{{", "")
                            res = res.replace("}}", "")
                            dffdfdfdf = allvars[check]
                            res = res.replace(check, str(dffdfdfdf))
                        else:
                            os.system("clear")
                            print(red + bold + str(lines) + "\n" + green +
                                  "^~~~~~~~~~~~~" + yellow + bold +
                                  "\n[Varaible error on line " + str(line) +
                                  "]:" + red + bold + "\n" + sun +
                                  " is not a varaible. Please create " + sun +
                                  " a varaiable. To use it in inputs")
                split_string = res.split("\")", -1)
                res = split_string[0]
                print(res, end="")
                # read_line = 0
            else:
                errors()
        else:
            errors()
    except:
        pass
def lognj():  #add suggestion about lang or whatever, KK- dark
    try:
        if (jb == 1):
            if '")' in lines:
                spl_word = 'writeN("'
                res = lines.partition(spl_word)[2]
                res = res.replace('$n', '\n')
                res = res.replace('\')', '')
                res = res.replace('{red}', red)
                res = res.replace('{blue}', blue)
                res = res.replace('{getChar1}', getChar1)
                res = res.replace('{getChar2}', getChar2)
                res = res.replace('{getChar3}', getChar3)
                res = res.replace('{bold}', bold)
                res = res.replace('{green}', green)
                res = res.replace('{magenta}', magenta)
                res = res.replace('{cyan}', cyan)
                res = res.replace('{yellow}', yellow)
                res = res.replace('{white}', w)
                res = res.replace('{end}', '\033[0m')
                res = res.replace('{black}', black)
                res = res.replace('{pink}', pink)
                res = res.replace('"', "")
                res = res.replace("  ", " ")
                res = res.replace(")", "")
                res = res.replace("{{input1}}", input1)
                res = res.replace("{{input2}}", input2)
                res = res.replace("{{input3}}", input3)
                res = res.replace("{{var1}}", var1)
                if "{{" in res:
                    if "}}" in res:
                        start = "{{"
                        end = "}}"
                        check = res[res.find(start) +
                                    len(start):res.rfind(end)]
                        if check in allvars:
                            res = res.replace("{{", "")
                            res = res.replace("}}", "")
                            dffdfdfdf = allvars[check]
                            res = res.replace(check, str(dffdfdfdf))
                        else:
                            os.system("clear")
                            print(red + bold + str(lines) + "\n" + green +
                                  "^~~~~~~~~~~~~" + yellow + bold +
                                  "\n[Varaible error on line " + str(line) +
                                  "]:" + red + bold + "\n" + sun +
                                  " is not a varaible. Please create " + sun +
                                  " a varaiable. To use it in inputs")
                split_string = res.split("\")", -1)
                res = split_string[0]
                print(res)
                # read_line = 0
            else:
                errors()
        else:
            errors()
    except:
        pass
def logl():
    try:
        if '")' in lines:
            spl_word = 'window.out.ln("'
            res = lines.partition(spl_word)[2]
            res = res.replace('$n', '\n')
            res = res.replace('\')', '')
            res = res.replace('{red}', red)
            res = res.replace('{blue}', blue)
            res = res.replace('{getChar1}', getChar1)
            res = res.replace('{getChar2}', getChar2)
            res = res.replace('{getChar3}', getChar3)
            res = res.replace('{bold}', bold)
            res = res.replace('{green}', green)
            res = res.replace('{magenta}', magenta)
            res = res.replace('{cyan}', cyan)
            res = res.replace('{end}', '\033[0m')
            res = res.replace('{yellow}', yellow)
            res = res.replace('{white}', w)
            res = res.replace('{black}', black)
            res = res.replace('{pink}', pink)
            res = res.replace('{end}', '\033[0m')
            res = res.replace('"', "")
            res = res.replace("  ", " ")
            res = res.replace(")", "")
            res = res.replace("{{input1}}", input1)
            res = res.replace("{{input2}}", input2)
            res = res.replace("{{input3}}", input3)
            res = res.replace("{{var1}}", var1)
            if "{{" in res:
                if "}}" in res:
                    start = "{{"
                    end = "}}"
                    check = res[res.find(start) + len(start):res.rfind(end)]
                    if check in allvars:
                        res = res.replace("{{", "")
                        res = res.replace("}}", "")
                        dffdfdfdf = allvars[check]
                        res = res.replace(check, str(dffdfdfdf))
                    else:
                        os.system("clear")
                        print(red + bold + str(lines) + "\n" + green +
                              "^~~~~~~~~~~~~" + yellow + bold +
                              "\n[Varaible error on line " + str(line) + "]:" +
                              red + bold + "\n" + sun +
                              " is not a varaible. Please create " + sun +
                              " a varaiable. To use it in inputs")
            split_string = res.split("\")", -1)
            res = split_string[0]
            print(res)
            # read_line = 0
        else:
            errors()
    except:
        pass
def log():
    try:
        if '")' in lines:
            spl_word = 'window.out("'
            res = lines.partition(spl_word)[2]
            res = res.replace('$n', '\n')
            res = res.replace('\')', '')
            split_string = res.split("\")", -1)
            res = split_string[0]
            res = res.replace('$n', '\n')
            res = res.replace('\')', '')
            res = res.replace('{red}', red)
            res = res.replace('{blue}', blue)
            res = res.replace('{getChar1}', getChar1)
            res = res.replace('{getChar2}', getChar2)
            res = res.replace('{getChar3}', getChar3)
            res = res.replace('{bold}', bold)
            res = res.replace('{green}', green)
            res = res.replace('{end}', '\033[0m')
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
            if "{{" in res:
                if "}}" in res:
                    start = "{{"
                    end = "}}"
                    check = res[res.find(start) + len(start):res.rfind(end)]
                    if check in allvars:
                        res = res.replace("{{", "")
                        res = res.replace("}}", "")
                        dffdfdfdf = allvars[check]
                        res = res.replace(check, str(dffdfdfdf))
                    else:
                        os.system("clear")
                        print(red + bold + str(lines) + "\n" + green +
                              "^~~~~~~~~~~~~" + yellow + bold +
                              "\n[Varaible error on line " + str(line) + "]:" +
                              red + bold + "\n" + sun +
                              " is not a varaible. Please create " + sun +
                              " a varaiable. To use it in inputs")
            print(res, end="")
            # read_line = 0
        else:
            errors()
    except:
        pass
red = "\033[0;31m"
bold = '\033[1m'
newvar = 0
f = open(f'{file_path}')
readline2 = 0
for lines in f.readlines():
    if "?*" in lines:
      readline2 = 1
    if readline2 == 1:
      continue
    if "*?" in lines:
      readline2 = 0
      continue
    if "//" in lines:
      if jb == 1:
        continue
    def errors():
        if "??" in lines:
            return
        if "?/" in lines:
            return
        if "/?" in lines:
            return
        elif "?" in lines:
            os.system("clear")
            print(
                red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~" +
                yellow + bold + "\n[comment error on line " + str(line) +
                "]:" + red + bold +
                "\nPlease use a ?? instead of a ?. The computer connot read a question mark. It will expect a custom read."
            )
            time.sleep(3000)
        elif "windowout" in lines:
            os.system("clear")
            print(
                red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~" +
                yellow + bold + "\n[syntax error in line " + str(line) + "]:" +
                red + bold + red + bold +
                "\nwindowout is not defined. Did you mean: 'window.out' or 'window.out.ln'"
            )
            time.sleep(3000)
        elif "import" in lines:
            os.system("clear")
            print(
                red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~~~" +
                yellow + bold + "\n[import error in line " + str(line) + "]:" +
                red + bold +
                "\nThe input provided was was not valid or no import was provided. Please put in a valid import"
            )
            time.sleep(3000)
        elif "window.out" in lines:
            os.system("clear")
            print(
                red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~" +
                yellow + bold + "\n[print error on line " + str(line) + "]:" +
                red + bold + red + bold +
                "\nwindow.out is a function but no text was found. Please insert text like this: `window.out(\"Hello World\")` next time"
            )
            time.sleep(3000)
        elif (jb == 0 and "write" in lines):
            print(red + bold + str(lines) + "\n" + green + "^~~~~~~~~~~" +
                  yellow + bold + "\n[syntax error on line " + str(line) +
                  "]:" + red + bold + red + bold +
                  "\nPlease use the jb import module to use jb commands")
            time.sleep(3000)

    line += 1
    lines = lines.replace('\n', '')
    lines = lines.replace('\t', '')
    if lines == "":
        pass
    elif "??" in lines:
        pass
    lines = lines.rstrip()
    
    if 'import jb.lang.*' in lines:
        jb = 1
        continue
    if "writeN(\"" in lines:
      lognj()
    if 'string ' in lines:
        spl_word = "string "
        newvar = lines.partition(spl_word)[2]
        split_string = newvar.split("\")", -1)
        newvar.replace(')', '')
        newvar.replace('\"', '')
        newvar = split_string[0]
        allvars[newvar] = None
    if "force.exit" in lines:
      if jb == 1:
        break
      else:
        pass
    if 'var ' in lines:
      if jb == 1:
        spl_word = "var "
        newvar = lines.partition(spl_word)[2]
        split_string = newvar.split("\")", -1)
        newvar.replace(')', '')
        newvar.replace('\"', '')
        newvar = split_string[0]
        allvars[newvar] = 0
    if '??' in lines:
        pass
        read_line = 0
    elif "question(" in lines:
        spl_word = "question("
        sun = lines.partition(spl_word)[2]
        split_string = sun.split(")", -1)
        sun.replace(')', '')
        sun.replace('\"', '')
        sun = split_string[0]
        sun.strip(")")
        if sun in allvars:
            sun = input()
            allvars[newvar] = sun
        else:
            if sun not in allvars:
                os.system("clear")
                print(red + bold + str(lines) + "\n" + green +
                      "^~~~~~~~~~~~~" + yellow + bold +
                      "\n[Varaible error on line " + str(line) + "]:" + red +
                      bold + "\n" + sun +
                      " is not a varaible. Please create " + sun +
                      " a varaiable. To use it in inputs")
                break
            else:
                errors()
    elif "window.in(" in lines:
        spl_word = "window.in("
        sun = lines.partition(spl_word)[2]
        split_string = sun.split(")", -1)
        sun.replace(')', '')
        sun.replace('\"', '')
        sun = split_string[0]
        sun.strip(")")
        if sun in allvars:
            sun = input()
            allvars[newvar] = sun
        else:
            if sun not in allvars:
                os.system("clear")
                print(red + bold + str(lines) + "\n" + green +
                      "^~~~~~~~~~~~~" + yellow + bold +
                      "\n[Varaible error on line " + str(line) + "]:" + red +
                      bold + "\n" + sun +
                      " is not a varaible. Please create " + sun +
                      " a varaiable. To use it in inputs")
                break
            else:
                errors()
    elif "window.add(" in lines:
        spl_word = "window.add("
        sun = lines.partition(spl_word)[2]
        split_string = sun.split(")", -1)
        sun.replace(')', '')
        sun.replace('\"', '')
        sun = split_string[0]
        sun.strip(")")
        int
    if 'window.sleep(' in lines:
        spl_word = 'window.sleep('
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res = split_string[0]
        time.sleep(float(res))
    if 'usleep(' in lines:
      if jb == 1:
        spl_word = 'usleep('
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res = split_string[0]
        time.sleep(float(res))
    if "?/" in lines:
        read = 0
    if "/?" in lines:
        read = 1
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
    elif lines == "import console.commands.*":
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
    elif '  ' in lines:
        if read_line == 1:
            if '  ' in lines:
                sppi()
                logli()
                logi()
        else:
            continue
    elif '};' in lines:
        read_line = 0
    elif "window.sp(\"" in lines:
        spp()
    #passsssss#umm wat is this so i can use cntl-f to find it later ah,ok
    elif "slowwrite(\"" in lines:
      sppj()
    elif 'window.out.ln("' in lines:
        if 'window.out.ln("' in lines:
            logl()
    elif 'window.out' in lines:
        log()
    elif 'write("' in lines:
        loglj()
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
    elif "window.kill" in lines:
        break
    elif "window.getChar1(" in lines:
        spl_word = "window.getChar("
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res.replace('"', '')
        sun = split_string[0]
        getChar1 = input()[0]

    elif "window.getChar2(" in lines:
        spl_word = "window.getChar2("
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res.replace('"', '')
        sun = split_string[0]
        getChar2 = input()[0]

    elif "window.getChar3(" in lines:
        spl_word = "window.getChar3("
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res.replace('"', '')
        sun = split_string[0]
        getChar3 = input()[0]

    elif 'system(' in lines:
        if ')' in lines:
            spl_word = 'system('
            res = lines.partition(spl_word)[2]
            split_string = res.split(")", -1)
            res.replace(')', '')
            res = split_string[0]
            os.system(res)
    elif "window.clear()" in lines:
        os.system('clear;echo 0')
    elif "window.clear(clear:all)" in lines:
        os.system('clear')
    elif "clear(console)" in lines:
      if jb == 1:
        os.system('clear; echo 0')
      else:
        pass
    elif "clear(console.all)" in lines:
      if jb == 1:
        os.system('clear')
      else:
        pass
    elif "window.rand(rand1)::(" in lines:
        spl_word = 'window.rand(rand1)::('
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res = split_string[0]
        try:
            rand1 = int(res)
        except ValueError:
            pass

    elif 'is "' in lines:
        if newvar in lines:
            spl_word = "is \""
            sun = lines.partition(spl_word)[2]
            split_string = sun.split('"', -1)
            sun.replace(')', '')
            sun.replace('\"', '')
            sun = split_string[0]
            sun.strip(")")
            allvars[newvar] = sun
    elif "window.rand(rand2)::(" in lines:
        spl_word = 'window.rand(rand2)::('
        res = lines.partition(spl_word)[2]
        split_string = res.split(")", -1)
        res.replace(')', '')
        res = split_string[0]
        try:
            rand2 = int(res)
        except ValueError:
            pass
    elif "window.rand.out(rand1, rand2)" in lines:
        import random
        randomNumber = random.randint(float(rand1), float(rand2))
    elif "if (randomNumber is \" " in lines:
        pass
    else:
        errors()
#print(w)
print(red + bold + "\nCode file exacuted with no errors")
while True:
  sun = input(blue + bold + "~/DarkScript-Compiler" + end + w + "$ ")
  os.system(str(sun))