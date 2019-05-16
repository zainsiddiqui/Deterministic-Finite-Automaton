##################################
# Deterministic Finite Automaton #
# Author: Zain Siddiqui		 #
##################################

flag = 0
DFA = {}
start = ""
final = []

def runFSM(input):
  cS = start
  ip = input
  for letter in input:
    try:
      cS = DFA[cS][letter]
    except KeyError:
      print("rejected")
      return

  
  for f in final:
    if (cS in f):
      print("accepted")
      return
  
  print("rejected")

def createAutomaton(input):
  global flag
  global DFA
  global start
  global final
  if ( 'states:' in  input):
    input = input.replace('states: ',"")

    states = input.split()

    for i,val in enumerate(states):
      DFA[states[i]] = {}

  if ( 'symbols:' in  input):
    input = input.replace('symbols: ',"")
    #SYMBOLS LIST
    symbols = input.split()

  if ( '->' in  input):

    rules = input.split()
    DFA[rules[0]][rules[4]] = rules[2]
    

  if ( 'start:' in  input):
    start = input.replace('start: ',"")
  if ( 'final:' in  input):
    input = input.replace('final: ',"")
    final = input.split()
    flag =1
    return
  if (flag == 1):
    runFSM(input)
    

def main():
  while True:     
    try:       
      inp = input()
      createAutomaton(inp)
    except EOFError:
      break


if __name__ == '__main__':
    main()
