def main():
    yell ( "This is CS50" )

def yell ( *words ) :
    Uppercased = []
    for word in words:
        Uppercased.append(word.upper())
    print(*Uppercased, sep=" ")

    
if __name__ == "__main__":
    main()