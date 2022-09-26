# Bare Bones Markov Text Generator

# import modules
import random
import nltk

# define function
def finish_sentence(sentence, n, corpus, deterministic=False):
    count = buildCount(sentence, n, corpus)
    if count == {}:
        x = n
    while (count == {}) and (x > -2):
        count = buildCount(sentence, x - 1, corpus)
        x -= 1
        pass
    if deterministic:
        sentence.append(max(count, key=count.get))
        pass
    else:
        sentence.append(
            random.choices(
                list(count.keys()),
                weights=[
                    eachCount / sum(count.values()) for eachCount in count.values()
                ],
                k=1,
            )[0]
        )
        pass
    pass


# define loop function to allow for back-off recursion
def buildCount(sentence, n, corpus):
    count = {}
    for eachToken in range(len(corpus)):
        if corpus[eachToken - n + 1 : eachToken] == sentence[-n + 1 :]:
            if corpus[eachToken] not in count:
                count[corpus[eachToken]] = 1
                pass
            else:
                count[corpus[eachToken]] += 1
                pass
            pass
        pass
    return count


# define main function
if __name__ == "__main__":
    sentence = ["how", "many", "cataclysmic"]
    n = 3
    corpus = nltk.word_tokenize(nltk.corpus.gutenberg.raw("austen-sense.txt").lower())
    deterministic = False
    while (sentence[-1] not in [".", "!", "?"]) and (len(sentence) < 10):
        finish_sentence(sentence, n, corpus, deterministic)
        pass
    print(sentence)
