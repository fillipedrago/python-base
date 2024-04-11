def repete_vogal(word):
    """Retorna a palavra com as vogais repetidas."""
    final_word = ""
    for index, letter in enumerate(word):
        # usamos enumerate para ajudar a sabermos as voltas do loop
        print(f"{index=} {letter=}")
        if letter.lower() in "aeiouãõôêéáíó":
            final_word = letter * 2
        else:
            final_word = letter
        print(f"final_word")
    return final_word
    
print(repete_vogal("banana"))