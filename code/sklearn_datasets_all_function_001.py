from sklearn import datasets#to get iris dataset
from sklearn import svm
'''
#dump_svmlight_file() not run 
iris=datasets.dump_svmlight_file()
print("After using dump_svlight_file in datasets of Sklearn, the Data is :: ",iris)
#fetch_20newsgroups not run
iris=datasets.fetch_20newsgroups()
print("After using fetch_20newsgrups in datasets of Sklearn, the Data is :: ",iris)
'''
#get_data_home() executed
iris=datasets.get_data_home()# output is  'C:\\Users\\Nutan Gupta\\scikit_learn_data'
print("the output of get_data_home() :: ",iris)

#load_boston() excuted
iris=datasets.load_boston()
print("the output of load_boston() :: ",iris)

#load_brest_cancer() excuted
iris=datasets.load_breast_cancer()
print("the output of load_breast_cancer() :: ",iris)

#load_diabetes() excuted
iris=datasets.load_diabetes()
print("the output of load_diabetes() :: ",iris)

#load_digits() excuted
iris=datasets.load_digits()
print("the output of load_digits() :: ",iris)

#load_iris() excuted
print("the output of load_iris() :: ",datasets.load_iris())

#load_linnerud() excuted
print("the output of load_linnerud() :: ",datasets.load_linnerud())

#load_wine() excuted
print("the output of load_wine() :: ",datasets.load_wine())

#make_blobs() excuted
print("the output of make_blobs() :: ",datasets.make_blobs())

#make_circles() executed
print("the output of make_circles() :: ",datasets.make_circles())

#make_classification() executed
print("the output of make_classification() :: ",datasets.make_classification())
#make_friedman1() executed
print("the output of make_friedman1() :: ",datasets.make_friedman1())

#make_friedman2() executed
print("the output of make_friedman2() :: ",datasets.make_friedman2())

#make_friedman3() executed
print("the output of make_friedman3() :: ",datasets.make_friedman3())


#make_gaussian_quantiles() executed
print("the output of make_gaussian_quantiles() :: ",datasets.make_gaussian_quantiles())

#make_hastie_10_2() executed
print("the output of make_hastie_10_2() :: ",datasets.make_hastie_10_2())


#make_moons() executed
print("the output of make_moons() :: ",datasets.make_moons())


#make_multilabel_classification() executed
print("the output of make_multilabel_classification() :: ",datasets.make_multilabel_classification())

#make_regression() executed
print("the output of make_regression() :: ",datasets.make_regression())

#make_sparse_spd_matrix() executed
print("the output of make_sparse_spd_matrix() :: ",datasets.make_sparse_spd_matrix())

#make_sparse_uncorrelated() executed
print("the output of make_sparse_uncorrelated() :: ",datasets.make_sparse_uncorrelated())

#make_sparse_uncorrelated() executed
print("the output of make_sparse_uncorrelated() :: ",datasets.make_sparse_uncorrelated())

#make_swiss_roll() executed
print("the output of make_swiss_roll() :: ",datasets.make_swiss_roll())

#mldata_filename() executed
print("the output of mldata_filename() :: ",datasets.mldata_filename('iris.txt'))
