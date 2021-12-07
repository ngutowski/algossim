from util.FilesLoader import FilesLoader


def data_store(name_dataset):
    classes = "./data/%s/classes.txt" % name_dataset
    descriptions = "./data/%s/descriptions.txt" % name_dataset
    predictions = "./data/%s/predictions.txt" % name_dataset

    f_arms = FilesLoader(classes)
    store_arms = f_arms.loadFile()
    res_arms = f_arms.processFileArms(store_arms)
    arms = res_arms[2]
    nb_arms = res_arms[1]
    d_arms = res_arms[0]

    # print(arms[0].getArmId())
    # print(arms[0].getArmName())
    # print(arms[0].getArmFeat())

    f_contexts = FilesLoader(descriptions)
    store_contexts = f_contexts.loadFile()
    res_contexts = f_contexts.processFileContexts(store_contexts)
    contexts = res_contexts[2]
    nb_contexts = res_contexts[1]
    d_contexts = res_contexts[0]

    # print(contexts[0].getContextId())
    # print(contexts[0].getContextFeat())

    f_ratings = FilesLoader(predictions)
    store_ratings = f_ratings.loadFile()

    res_ratings = f_ratings.processFileRatings(store_ratings, nb_contexts, nb_arms)

    ratings = res_ratings[0]
    nb_pred = res_ratings[1]

    # print(ratings)

    f_arms.close(store_arms)
    f_ratings.close(store_ratings)
    f_contexts.close(store_contexts)

    return d_contexts, nb_arms, arms, contexts, ratings, nb_arms, nb_contexts, nb_pred, d_arms
