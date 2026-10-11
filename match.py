name = input("enter your name: ")

match name:
    case "harry" | "potter" | "heriome":
        print("correct")
    case "ddd" | "eee" | "fff":
        print("also correct")
    case _:
        print("invalid")        