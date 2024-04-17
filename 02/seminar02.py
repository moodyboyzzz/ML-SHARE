class MyFirstClassifier(object):
    def __init__(self):
        pass
    def fit(self, x_train, y_train):
        self.class_means = {}
        for digit in np.unique(y_train):
            digit_pixels = x_train[y_train == digit]
            mean_pixel = np.mean(digit_pixels, axis=0)
            self.class_means[digit] = mean_pixel
    def predict(self, x_test):
        predictions = []
        for image in x_test:
            min_distance = float('inf')
            predicted_digit = None
            for digit, mean_pixel in self.class_means.items():
                distance = np.sum(np.abs(image - mean_pixel))
                if distance < min_distance:
                    min_distance = distance
                    predicted_digit = digit
            predictions.append(predicted_digit)
        return predictions