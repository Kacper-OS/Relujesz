import sys, tkinter

class interpreter:
    def __init__(self, file_path: str):
        self.program_lines:dict = []
        self.functions:dict = []
        self.classes:dict = []
        self.python_code:str = ""

        with open(file_path, "r") as file:
            if ".rel" in file_path or ".🪑" in file_path or ".🗿" in file_path:
                for line in file.readlines():
                    # print(line)
                    self.program_lines.append(line.replace(";", ""))
            else:
                print("\npreferowane rozszerzenia plików to / The preferred file extensions are .rel / .🪑 / .🗿\n")
                

        for line in self.program_lines:
            if "#" in line or "//" in line:
                pass
            else:
                if "sigma" in line:
                    self.functions.append(f"{line.replace("sigma ", "").replace("sigma", "").replace(":", "").strip().split("(")[0]}()")
                    self.python_code += line.replace("sigma", "def")
                elif "delulu(" in line:
                    self.python_code += line.replace("delulu(", "print(")
                elif "fr" in line:
                    if "Prawda" in line:
                        self.python_code += line.replace("fr ", "").removeprefix("fr ").replace("Prawda", "True")
                    elif "Fałsz" in line or "Falsz" in line:
                        self.python_code += line.replace("fr ", "").removeprefix("fr ").replace("Fałsz", "False").replace("Falsz", "False")
                    else:
                        self.python_code += line.replace("fr ", "").removeprefix("fr ")
                elif "imo" in line:
                    self.python_code += line.replace("imo", "if")
                elif "naura" in line:
                    self.python_code += line.replace("naura", "return")
                elif "rizz" in line:
                    if "Prawda" in line:
                        self.python_code += line.replace("rizz", "while").replace("Prawda", "True") 
                    elif "Fałsz" in line or "Falsz" in line:
                        self.python_code += line.replace("rizz", "while").replace("Fałsz", "False").replace("Falsz", "False")
                    else: 
                        self.python_code += line.replace("rizz", "while")
                elif "py(" in line:
                    self.python_code += line.replace('py("', '').replace('")', '')
                elif line in self.functions:
                    self.python_code += line.replace(";", "")
                elif "uzywaj" in line:
                    if "jako" in line:
                        self.python_code += line.replace("uzywaj", "import").replace("jako", "as")
                    else:
                        self.python_code += line.replace("uzywaj", "import")
                elif "baza" in line:
                    self.classes.append(line.replace("baza ", "").replace("baza", "").replace(":", "").strip())
                    self.python_code += line.replace("baza", "class")
                elif line.split(".")[0] in self.classes:
                    if line.split(".")[1] in self.functions:
                        self.python_code += line
                elif "przez" in line:
                    if "w" in line:
                        self.python_code += line.replace("przez", "for").replace("w", "in")
                    else:
                        self.python_code += line.replace("przez", "for")
                elif "$SIGMA" in line: self.python_code +=  line.replace("$SIGMA", 'print("Kacper jest Sigmą / Kacper is Sigma")\n')
                else:
                    self.python_code += line

        # print(self.functions)
        # print(self.classes)
        # print(self.python_code)

        try:
            exec(self.python_code)
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    try:
        interpreter(sys.argv[1])
    except IndexError:
        print("\npodaj ścieżkę do pliku / Specify the path to the file\n")