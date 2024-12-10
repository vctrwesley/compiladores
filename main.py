#.\venv\Scripts\python.exe -m pip install matplotlib
#.\venv\Scripts\python.exe -m pip install networkx
from Repl import *

def prompt():
  Repl().cmdloop()

def test(w):
  Repl().analisador(w)

if __name__ == "__main__":
  prompt()