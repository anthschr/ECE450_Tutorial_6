from sklearn import metrics
import csv

with open("cluster_ids.txt") as file:
	tsv_file = csv.reader(file,delimiter="\t")
	labels_true_cascade=[]
	labels_predicted_single_step=[]
	for line in tsv_file:
		labels_true_cascade.append(line[1])
		labels_predicted_single_step.append(line[2])
	print(labels_true_cascade)
	print(labels_predicted_single_step)
	del labels_true_cascade[0]
	del labels_predicted_single_step[0]
	print(labels_true_cascade)
	print(labels_predicted_single_step)

for i in range(len(labels_true_cascade)):
	labels_true_cascade[i] = int(labels_true_cascade[i])
	labels_predicted_single_step[i] = int(labels_predicted_single_step[i])

for i in range(len(labels_true_cascade)):
	print("{0}\t{1}".format(labels_true_cascade[i],labels_predicted_single_step[i]))

adjusted_rand_score = metrics.adjusted_rand_score(labels_true_cascade,labels_predicted_single_step)
adjusted_mutual_info_score = metrics.adjusted_mutual_info_score(labels_true_cascade,labels_predicted_single_step)
normalized_mutual_info_score = metrics.normalized_mutual_info_score(labels_true_cascade,labels_predicted_single_step)
homogeneity = metrics.homogeneity_score(labels_true_cascade,labels_predicted_single_step)
completeness = metrics.completeness_score(labels_true_cascade,labels_predicted_single_step)

print("Adjusted Rand Score:\t\t%s" % adjusted_rand_score)
print("Adjusted Mutual Info Score:\t%s" % adjusted_mutual_info_score)
print("Normalized Mutual Info Score:\t%s" % normalized_mutual_info_score)
print("Homogeneity:\t\t\t%s" % homogeneity)
print("Completeness:\t\t\t%s" % completeness)