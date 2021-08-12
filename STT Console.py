import StaticToornament

def inputLoop():
 theInput = str(input())
 if theInput == "": inputLoop()
 else: print(StaticToornament.getMatchAndCustomFormatted(theInput))
 inputLoop()

inputLoop()