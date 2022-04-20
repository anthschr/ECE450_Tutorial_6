from sklearn import metrics
import csv

with open("DB_1_clu_cascade_numbers.txt") as file:
	cascade_tsv = csv.reader(file,delimiter="\t")
	print(cascade_tsv)
	labels_true_cascade=[]
	for line in cascade_tsv:
		labels_true_cascade.append(line[0])
	del labels_true_cascade[0]

with open("DB_1_clu_single_step_numbers.txt") as file:
	single_step_tsv = csv.reader(file,delimiter="\t")
	print(single_step_tsv)
	labels_predicted_single_step=[]
	for line in single_step_tsv:
		labels_predicted_single_step.append(line[0])
	del labels_predicted_single_step[0]

for i in range(len(labels_true_cascade)):
	labels_true_cascade[i] = int(labels_true_cascade[i])
	labels_predicted_single_step[i] = int(labels_predicted_single_step[i])

print(labels_true_cascade)

adjusted_rand_score = metrics.adjusted_rand_score(labels_true_cascade,labels_predicted_single_step)
adjusted_mutual_info_score = metrics.adjusted_mutual_info_score(labels_true_cascade,labels_predicted_single_step)
homogeneity = metrics.homogeneity_score(labels_true_cascade,labels_predicted_single_step)
completeness = metrics.completeness_score(labels_true_cascade,labels_predicted_single_step)

print("Adjusted Rand Score:\t\t%s" % adjusted_rand_score)
print("Adjusted Mutual Info Score:\t%s" % adjusted_mutual_info_score)
print("Homogeneity:\t\t\t\t%s" % homogeneity)
print("Completeness:\t\t\t\t%s" % completeness)