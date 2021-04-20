from dummy_dataset import *
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

model = LinearRegression()
model.fit(x, y)
y_predicted = model.predict(x)

# evaluasi model
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)

print('Slope:', model.coef_)
print('Intercept:', model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)

# merencanakan hasil
plt.scatter(x, y, s=5)
plt.xlabel('x')
plt.ylabel('y')

# hasil dari prediksi
plt.plot(x, y_predicted, color='r')
plt.show()
