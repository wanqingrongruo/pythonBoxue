from sklearn import tree

features = [[550, 160], [520, 200], [80, 420], [110, 360]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[400, 110]]))

