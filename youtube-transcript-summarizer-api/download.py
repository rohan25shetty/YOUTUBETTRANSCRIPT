def makeTextFile(name, content):
    directory = f"{name}.txt"
    file = open(directory, "w", encoding="utf-8")
    file.write(f"{name} Transcript:\n")
    file.write(content)
    file.close()

    
