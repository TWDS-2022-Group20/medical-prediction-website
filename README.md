# Mental Health Helper 心理健康小幫手

The Mental Health Helper is a web service to predict the risk of getting depression. We extract some questoinnaries from CDC of The United States and build a model with LightGBM to estimate the probability of having depression. Because the respondents in our training data are mostly American, this application may have some drifts when being applied to those people who are not living in the United States. However, in our opinion, it is worthy to conduct such experiment, because the selected questionnaires are very general compared to traditional mental health related questionnaries like: PHQ-9. It is more likely to find out the potential and help them in the early stage of depression.


## How to launch our service?

[Local Service]

After installed the pre-requisite python packages, all you need to do is run the following command:
```
$ streamlit run depression_predictor.py
```

It will open a website with your default browser.

## Quick Installation

- Windows
1. creata a virtual environement with pyenv or venv
2. activate the virtual environment, and then install the python packages through:
```
pip install -r requirements/requirements.txt
```

- macOS (M1 chips)
1. create a virual environment with conda
2. activate the conda environment and then install python packages throguh:
```
pip install -r requirements/requirement-macOS.txt
bash requirements/conda_package_install.sh
```

## Main Contributors
- Sam      沈昱辰
- Eli Chen 陳杰翰 (ita3051 at gmail.com)

## How to contribute to this repository?
This project still has a lot rooms to improve. for example, the integration CI/CD development tool and doing some depth research on modeling the flow of questionnaires.

Any contributions are welcome, and please follow GitHub flow when issuing a pull request.

Thanks,
Team of Mental Health Helper

## License
The MIT License
