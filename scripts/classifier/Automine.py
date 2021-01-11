import os
import random
import yaml
import subprocess
import reproduce.reproduce as r
from reproduce.filereader import FileReader
import pickle
import nltk
from git import rmtree

NO_COMMITS = 39

fr = FileReader()
folders = ['data', 'metadata', 'reproduce']
relevantNo = 0


checked = []

if os.path.exists(os.getcwd() +'/sc.pickle') and os.path.exists(os.getcwd() +'/classifier.pickle'):
    scFile = open('sc.pickle', 'rb')
    classifierFile = open('classifier.pickle', 'rb')
    classifier = pickle.load(classifierFile)
    sc = pickle.load(scFile)
else:
    scFile = open('sc.pickle', 'wb')
    classifierFile = open('classifier.pickle', 'wb')
    classifier, sc = r.run()
    pickle.dump(sc, scFile)
    pickle.dump(classifier, classifierFile)

pre_fn=sc.lemmatize_new_text
feature_fn=sc.bag_of_words



for f in os.scandir(os.getcwd()):
        if f.is_dir() and not f.name in folders:
            repoDir = f.path
            rmtree(repoDir)


total = 0
while relevantNo < NO_COMMITS:
    relevantComs = open("relevant.txt", 'a', encoding='utf-8')
    logFile = open('log.txt', 'w', encoding='utf-8')
    repoMeta = random.choice([x for x in os.listdir(os.getcwd() + "/metadata/") if os.path.isfile(os.path.join("metadata/", x))])
    repoMeta = os.path.join('metadata/', repoMeta)
    if repoMeta in checked:
        continue
    checked.append(repoMeta)
    repoFile = open(repoMeta, 'r', encoding='utf-8')
    repoYaml  = yaml.load(repoFile)
    gitAddr = repoYaml.get('Repo', 'NA')
    if 'github' not in gitAddr:
        continue
    cmd = "git clone " + gitAddr
    try:
        cloned = subprocess.check_output(cmd.split(' ')).decode()
    except subprocess.CalledProcessError as e:
        continue
    for f in os.scandir(os.getcwd()):
        if f.is_dir() and not f.name in folders:
            repoDir = f.path

    cmd = "git log"
    try:
        log = subprocess.check_output(cmd.split(' '), cwd=repoDir).decode()
    except UnicodeDecodeError as e:
        rmtree(repoDir)
        continue
    
    logFile.write(log)
    logFile.close()
    commits = fr.parse('log.txt')

    relevant_features = [" ".join(pre_fn(x.text)) for x in sc.relevant_commits]
    irrelevant_features = [" ".join(pre_fn(x.text)) for x in sc.irrelevant_commits]
    unknown_features = [" ".join(pre_fn(x.text)) for x in sc.unknown_commits]
    to_predict = [" ".join(pre_fn(x.text)) for x in commits]
    features = []
    features.extend(relevant_features)
    features.extend(irrelevant_features)
    features.extend(unknown_features)
    features.extend(to_predict)
    x = feature_fn(features)
    x_unknown = x[len(relevant_features) + len(irrelevant_features) + len(unknown_features):]
    prediction = classifier.predict(x_unknown)



    relevantComs.write(gitAddr)
    relevantComs.write('\n')
    relevantComs.write('num commits: ' + str(len(commits)))
    relevantComs.write('\n\n')
    total += len(commits)
    i = 0
    while i < len(prediction):
            if prediction[i] != "irrelevant":
                commit = commits[i]
                relevantComs.write("commit " + commit.cmt_hash + "\n")
                relevantComs.write("Author: " + commit.author + "\n")
                relevantComs.write("Date: " + commit.date + "\n")
                relevantComs.write("\n" + commit.text + "\n\n")
                relevantNo += 1
            i += 1

    rmtree(repoDir)
    relevantComs.close
    print(str(relevantNo) + " commits found so far")

relevantComs.write('Total commits: ' + str(total))