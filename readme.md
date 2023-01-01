# AI for Medicine Specialization
taught by Pranav Rajpurkar, Instructor Harvard University

## About this Course
AI is transforming the practice of medicine. It’s helping doctors diagnose patients more accurately, make predictions about patients’ future health, and recommend better treatments. As an AI practitioner, you have the opportunity to join in this transformation of modern medicine. If you're already familiar with some of the math and coding behind AI algorithms, and are eager to develop your skills further to tackle challenges in the healthcare industry, then this specialization is for you. No prior medical expertise is required! 

This program will give you practical experience in applying cutting-edge machine learning techniques to concrete problems in modern medicine:

- In Course 1, you will create convolutional neural network image classification and segmentation models to make diagnoses of lung and brain disorders. 
- In Course 2, you will build risk models and survival estimators for heart disease using statistical methods and a random forest predictor to determine patient prognosis. 
- In Course 3, you will build a treatment effect predictor, apply model interpretation techniques and use natural language processing to extract information from radiology reports.

## Citations

Chest X Ray 8 Dataset
https://arxiv.org/abs/1705.02315

CheXNeXt
https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1002686

Dermatology
https://www.nature.com/articles/nature21056

Ophthalmology
https://www.ncbi.nlm.nih.gov/pubmed/27898976

Pathology
https://jamanetwork.com/journals/jama/fullarticle/2665774

Data - decathlon 10 challenge
https://decathlon-10.grand-challenge.org/

Decathlon 10 paper (contains brief background on CT — see task_01 (brain tumour)) 
https://arxiv.org/pdf/1902.09063.pdf

3D U-Net
https://arxiv.org/abs/1606.06650

U-Net
https://arxiv.org/abs/1505.04597

--------------
Chads-vasc risk score
https://journal.chestnet.org/article/S0012-3692(10)60067-0/fulltext

MELD score
https://aasldpubs.onlinelibrary.wiley.com/doi/full/10.1002/hep.21563

ASCVD+
https://www.ahajournals.org/doi/full/10.1161/01.cir.0000437738.63853.7a

Data: NHANES I 
links https://wwwn.cdc.gov/nchs/nhanes/nhanes1/
references  https://wwwn.cdc.gov/nchs/nhanes/nhefs/

Data in SHAP library
https://github.com/slundberg/shap

Also used this notebook by the creator SHAP, Scott Lundberg, as a loose reference when developing the assignment.
https://slundberg.github.io/shap/notebooks/NHANES%20I%20Survival%20Model.html

Lifelines library
https://lifelines.readthedocs.io/en/latest/
Lifelines is also the source of the dataset. It in turn sources its data from StatsDirect https://www.statsdirect.com/help/content/survival_analysis/logrank.htm, which takes it from Arbitrage and Berry http://www.medicine.mcgill.ca/epidemiology/hanley/c634/lifetables/abm_17.PDF

Cox Model
https://www.jstor.org/stable/2985181?seq=1

Random survival forest 
https://arxiv.org/pdf/0811.1645.pdf

Harrell C-Index 
https://www.ncbi.nlm.nih.gov/pubmed/7069920

---------
Levamisole and Fluorouracil background
https://www.nejm.org/doi/full/10.1056/NEJM199002083220602

Data sourced from here
https://www.rdocumentation.org/packages/survival/versions/3.1-8/topics/colon

C-statistic for benefit
https://www.ncbi.nlm.nih.gov/pubmed/29132832

T-learner
https://arxiv.org/pdf/1706.03461.pdf
Labeling methods and dataset

https://arxiv.org/abs/1901.07031

Huggingface transformers library
https://github.com/huggingface/transformers

BERT paper
https://arxiv.org/abs/1810.04805

Question answering data set (used for example)
https://rajpurkar.github.io/SQuAD-explorer/

Grad cam
https://arxiv.org/pdf/1610.02391.pdf

Random forests + permutation importance: https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf (R45f14345c000-1 Breiman, “Random Forests”, Machine Learning, 45(1), 5-32, 2001.)

Shapley importance
https://www.nature.com/articles/s42256-019-0138-9

Clinical note example for question answering
https://www.mtsamples.com/
