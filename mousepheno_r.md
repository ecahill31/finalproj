I oversee a project that makes knockout mice and phenotypes them.
Specifically, a gene is deleted (e.g., Fbxo7), mice are bred up (7M + 7F KOs)
and then examined using clinical assays to detect “phenodeviants.”
The grantees on the project have developed an R package to analyze the
phenotype data. The package has a variety of models, tests, and graphical
outputs.
For the class project I analyzed the red blood cell counts of Fbxo7
knockouts. I installed Phenstat from Bioconductor, downloaded a dataset, made
some minor alterations (change “Weight” from factor to numeric, changed
factor level name for Genotype), ran the testDataset function, output the
summary, and ran the boxplotSexGenotype function to generate a boxplot.

1) Install and load Phenstat
2) Read in a dataset
3) Manipulate a dataset

library(PhenStat)
PhenFbxo7RBC <-
data.frame(read.csv("http://www.mousephenotype.org/data/exportraw?phenotyping_center=
WTSI&parameter_stable_id=IMPC_HEM_002_001&allele_accession_id=MGI:4842259&strain=MGI:
2159965&pipeline_stable_id=MGP_001&&zygosity=homozygote&"))
#change Weight from factor to numeric
PhenFbxo7RBC[, "Weight"] <- as.numeric(as.character(PhenFbxo7RBC[,"Weight"]))
## Warning: NAs introduced by coercion
#convert "MEBV"" to "KO/KO" in Genotype column
levels(PhenFbxo7RBC$Genotype)[levels(PhenFbxo7RBC$Genotype)=="MEBV"] <- "KO/KO"
# PhenList cleans the dataframe
pl <- PhenList(PhenFbxo7RBC, testGenotype ="KO/KO" )
## Warning:
## Dataset's column 'Assay.Date' has been renamed to 'Batch' and will be used for the
batch effect modelling.
## Information:
## Dataset's 'Genotype' column has following values: '+/+', 'KO/KO'
## Information:
## Dataset's 'Sex' column has following value(s): 'Female', 'Male'

4) Do statistical test on a dataset

TestFb7RBC <- testDataset(pl, depVariable = "Value")
## Information:
## Dependent variable: 'Value'.
## Information:
## Perform all MM framework stages: startModel and finalModel.
## Information:
## Method: Mixed Model framework.
## Information:
## Equation: 'withWeight'.
## Information:
## Calculated values for model effects are: keepBatch=TRUE, keepEqualVariance=TRUE, keepWeight=TRUE,
keepSex=FALSE, keepInteraction=TRUE.
summaryOutput(TestFb7RBC)
##
## Test for dependent variable:
## *** Value ***
##
## Method:
## *** Mixed Model framework ***
## ----------------------------------------------------------------------------
## Model Output
## ----------------------------------------------------------------------------
## Final fitted model: Value ~ Sex + Genotype:Sex + Weight
## Was batch significant? TRUE
## Was variance equal? TRUE
## Genotype p-value: 2.461476e-21
## Genotype by male effect: -2.170103e+00 +/- 2.416023e-01
## Genotype by female effect: -1.245927e+00 +/- 2.374242e-01
## Was there evidence of sexual dimorphism? yes (p-value 3.966791e-03)
## Genotype percentage change Female: -11.41%
## Genotype percentage change Male: -19.87%
##
## ----------------------------------------------------------------------------
## Classification Tag
## ----------------------------------------------------------------------------
## With phenotype threshold value 0.01 - different size as males greater
##
## ----------------------------------------------------------------------------
## Model Output Summary
## ----------------------------------------------------------------------------
## Value Std.Error DF t-value
## (Intercept) 10.43321240 0.097604540 2687 106.8926958
## SexMale -0.02773634 0.030301085 2687 -0.9153579
## Weight 0.01795439 0.003676673 2687 4.8833237
## SexFemale:GenotypeKO/KO -1.24592701 0.237424181 2687 -5.2476837
## SexMale:GenotypeKO/KO -2.17010343 0.241602280 2687 -8.9821314
## p-value
## (Intercept) 0.000000e+00
## SexMale 3.600859e-01
## Weight 1.104251e-06
## SexFemale:GenotypeKO/KO 1.660369e-07
## SexMale:GenotypeKO/KO 4.880124e-19

5) Make a graph from the data
boxplotSexGenotype(pl, depVariable = "Value")