# Does poor educational infrastructure influence school dropout and child labor in Brazil?

> This project (Write a Data Science Blog Post) is part of Udacity Data Scientist Nanodegree Program. Detailed analysis results can be found in [the full article (medium)]([/assets/images/tux.png](https://danilocardia.medium.com/does-poor-educational-infrastructure-influence-school-dropout-and-child-labor-in-brazil-c36c68150344)).

## Libraries
- numpy
- pandas
- matplotlib
- seaborn
- sci-kit learn
## Motivation
The current school dropout in Brazil is 20%, while there are more than 1.8 million children in child labor situation. It’s common sense to relate high quality school infrastructure with low rate of school dropout, but is this actually true in the Brazilian reality?

## Questions

1. Is school dropout rate higher in schools with less infrastructure?
2. Is child labor rate higher in regions where the schools have less infrastructure?
3. Is child labor rate higher in regions with high school dropout rate?

## Files

The Brazilian dataset files can be found [in this portal](https://dados.gov.br/dataset). I needed to pre-process that data before pushing to this repository because the main dataset has more than 5GB, so I cleaned it up by using the following scripts:
- [enem-cleaning.py](enem-cleaning.py)
- [enem-state-split.py](enem-state-split.py)

Besides, I also applied the same cleaning to the schools infrastructure dataset:
- [schools-infrastructure-cleaning.py](schools-infrastructure-cleaning.py)

The processed files are used afterwards in the analysis. These files are found in [data-prepared](data-prepared/) folder.

Following CRISP-DM process, I have two notebooks for the steps 2 and 3, given I've done the first step (business understanding) by researching about the subjet:
- [2-data-understanding.ipynb](2-data-understanding.ipynb)
- [3-data-exploration-and-preparation.ipynb](3-data-exploration-and-preparation.ipynb)

## Results
The findings of the analysis done with this code are found at the [post available here](https://danilocardia.medium.com/does-poor-educational-infrastructure-influence-school-dropout-and-child-labor-in-brazil-c36c68150344)

## Licensing, Authors, Acknowledgements

I'd like to thank the Brazilian Federal Government for maintaining such a datasets publicly available. An special mention for professor Joaquim Soares Neto of Universidade de Brasília, who conducted a research that helped me to weight infrastrucutre features in schools.