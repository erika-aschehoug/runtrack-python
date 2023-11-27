def my_long_word(longueur, phrase):
    """
    Retourne les mots d'une phrase qui sont plus longs qu'une longueur donnée.
    """
    words = phrase.split()  # Sépare la phrase en mots
    long_words = []  # Liste pour stocker les mots plus longs que la longueur donnée

    for word in words:
        if count_characters(word) > longueur:  # Utilise une fonction personnalisée pour compter les caractères
            long_words.append(word)

    return ' '.join(long_words)  # Retourne les mots séparés par des espaces

def count_characters(word):
    """
    Compte le nombre de caractères dans un mot sans utiliser la fonction len().
    """
    count = 0
    for caractere in word:
        count += 1
    return count

test_sentence = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(f"{my_long_word(3, test_sentence)}")
