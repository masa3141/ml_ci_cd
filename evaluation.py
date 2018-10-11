import yaml

with open("model.yml", "r+") as f:
    data = yaml.load(f)
print(data)

def evaluate(test_data, predict_data):
    return sum([(t-p)**2 for (t, p) in zip(test_data, predict_data)])


train_data = [1, 2, 3]
test_data = [3, 4, 5]
module = __import__(data['model'])
class_ = getattr(module, data['class'])
instance = class_(train_data, test_data)
instance.fit()
predict_data = instance.predict()
score = evaluate(test_data, predict_data)
print(score)


