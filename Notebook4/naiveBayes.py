def prob_of_feature_with_given_class(featureName, featureAttr, className):
    classOccurence = 0
    feature_occurence_in_given_class = 0
    for i in range(len(featuresAndClassesDic['class'])):
        if featuresAndClassesDic['class'][i] == className:
            classOccurence += 1
            if featuresAndClassesDic[featureName][i] == featureAttr:
                feature_occurence_in_given_class += 1
    return feature_occurence_in_given_class / classOccurence

def prob_class(className):
    classOccurence = 0
    entireEntries = len(featuresAndClassesDic['class'])
    for i in range(len(featuresAndClassesDic['class'])):
        if featuresAndClassesDic['class'][i] == className:
            classOccurence += 1
    return classOccurence / entireEntries

#f.e. name: day, attr: monday
def prod_of_feature(featureName, featureAttr):
    attr_occurence = 0
    entire_attr = len(featuresAndClassesDic[featureName])
    for i in range(len(featuresAndClassesDic[featureName])):
        if featuresAndClassesDic[featureName][i] == featureAttr:
            attr_occurence += 1
    return attr_occurence / entire_attr


def prob_of_class_with_given_features(feature_names, feature_attrs, class_name):
    #basically: d is our feature, c is our class

    #percentage its a feature_attr with given class_name
    p_d_under_cond_c = []

    p_d = []

    for i in range(len(feature_names)):
        p_d_under_cond_c.append(prob_of_feature_with_given_class(featureName=feature_names[i], featureAttr=feature_attrs[i], className=class_name))
        p_d.append(prod_of_feature(feature_names[i], feature_attrs[i]))

    p_c = prob_class(class_name)

    result = 1
    for i in range(len(p_d)):
        result *= (p_d_under_cond_c[i])
    return result * p_c


with open('weather.txt', 'r') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
values = []
for line in content:
    values.append(line.split(", "))

headLine = values[0]

probabilitiesUnderConditions = []

#Contains a a feature key and attribute values, f.e. "season":["winter", "spring" ...]
featuresAndClassesDic = {}
for i in range(len(headLine)):
    #add each feature name
    featuresAndClassesDic[headLine[i]] = []
    for j in range(len(values)):
        if values[j][i] != headLine[i]:
            #Add the feature attributes
            featuresAndClassesDic[headLine[i]].append(values[j][i])


feature_names = ['day', 'season', 'wind', 'rain']
feature_attrs = ['weekday', 'winter', 'high', 'heavy']

classes = ['on time', 'late', 'very late', 'cancelled']


probs = []
for class_name in classes:
    probs.append([class_name, prob_of_class_with_given_features(feature_names, feature_attrs, class_name)])

print(probs)






