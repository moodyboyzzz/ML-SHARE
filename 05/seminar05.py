import csv

with open('y_true.txt', 'r') as true_file, open('y_pred.txt', 'r') as pred_file:
    y_true = [int(x) for x in true_file]
    y_pred = [int(x) for x in pred_file]

TP = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == 1)
TN = sum(1 for i in range(len(y_true)) if y_true[i] == -1 and y_pred[i] == -1)
FP = sum(1 for i in range(len(y_true)) if y_true[i] == -1 and y_pred[i] == 1)
FN = sum(1 for i in range(len(y_true)) if y_true[i] == 1 and y_pred[i] == -1)

acc = (TP + TN) / (TP + TN + FP + FN)
prec = TP / (TP + FP)
rec = TP / (TP + FN)
tpr = rec
fpr = FP / (FP + TN)
tnr = TN / (FP + TN)
fnr = FN / (TP + FN)
f1 = 2 * (prec * rec) / (prec + rec)

metrics = [acc, tpr, fpr, tnr, fnr, prec, rec, f1]

with open('seminar05_metrics.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["acc", "tpr", "fpr", "tnr", "fnr", "prec", "rec", "f1"])
    writer.writerow(metrics)