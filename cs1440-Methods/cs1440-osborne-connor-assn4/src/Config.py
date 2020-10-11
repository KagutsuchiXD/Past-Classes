def createDictionary(config):
    dictionary = {}
    with open(config, "r") as configFile:
        for line in configFile:
            keys = line.strip().split(": ")
            dictionary[(keys[0].lower())] = keys[1]

    return dictionary
