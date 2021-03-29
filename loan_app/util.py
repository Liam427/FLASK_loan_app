import requests
import pandas as pd
from loan_app.models import Loan, Evaluation, db


def get_loan_api():
    serviceKey='4e19b3c39dc13e07c53cb5561795c308'

    endpoint1 = 'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={serviceKey}&topFinGrpNo=050000&pageNo=1'.format(serviceKey=serviceKey)
    resp1 = requests.get(endpoint1)

    a1 = pd.DataFrame(resp1.json()['result']['optionList'])
    b1 = pd.DataFrame(resp1.json()['result']['baseList'])[['fin_co_no', 'kor_co_nm', 'fin_prdt_nm']]
    bank1_df = pd.merge(a1, b1, on='fin_co_no')
    bank1_df = bank1_df.drop_duplicates()

    endpoint2 = 'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={serviceKey}&topFinGrpNo=020000&pageNo=1'.format(serviceKey=serviceKey)
    resp2 = requests.get(endpoint2)

    a2 = pd.DataFrame(resp2.json()['result']['optionList'])
    b2 = pd.DataFrame(resp2.json()['result']['baseList'])[['fin_co_no', 'kor_co_nm', 'fin_prdt_nm']]
    bank2_df = pd.merge(a2, b2, on='fin_co_no')
    bank2_df = bank2_df.drop_duplicates()

    endpoint3 = 'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={serviceKey}&topFinGrpNo=030300&pageNo=1'.format(serviceKey=serviceKey)
    resp3 = requests.get(endpoint3)

    a3 = pd.DataFrame(resp3.json()['result']['optionList'])
    b3 = pd.DataFrame(resp3.json()['result']['baseList'])[['fin_co_no','kor_co_nm', 'fin_prdt_nm']]
    bank3_df = pd.merge(a3, b3, on='fin_co_no')
    bank3_df = bank3_df.drop_duplicates()

    loan_df = pd.concat([bank1_df, bank2_df, bank3_df])
    loan_df.drop(['dcls_month', 'fin_co_no', 'fin_prdt_cd', 'rpay_type', 'lend_rate_type'], axis=1, inplace=True)
    loan_df = loan_df[['kor_co_nm', 'fin_prdt_nm', 'rpay_type_nm', 'lend_rate_type_nm', 'lend_rate_min', 'lend_rate_max', 'lend_rate_avg']]
    loan_df.columns = ['금융회사', '대출 상품명', '상환방식', '대출 금리유형', '최저 대출금리(%)', '최고 대출금리(%)', '평균 대출금리(%)']

    # print(loan_df)

    # print(loan_df.iloc[0])

    # print(loan_df.iloc[0].to_dict())

    

    for i in range(215):
        bank_name=loan_df.iloc[i].to_dict()['금융회사']
        loan_name=loan_df.iloc[i].to_dict()['대출 상품명']
        rpay = loan_df.iloc[i].to_dict()['상환방식']
        rate_type = loan_df.iloc[i].to_dict()['대출 금리유형']
        rate_min = loan_df.iloc[i].to_dict()['최저 대출금리(%)']
        rate_max = loan_df.iloc[i].to_dict()['최고 대출금리(%)']
        rate_avg = loan_df.iloc[i].to_dict()['평균 대출금리(%)']

        loan_up = Loan(bank_name=bank_name, loan_name=loan_name, rpay=rpay, rate_type=rate_type, 
        rate_min=rate_min, rate_max=rate_max, rate_avg=rate_avg)
        
        print(i, '----------------------------------------------------------')
        db.session.add(loan_up)
        db.session.commit()

    return print("에휴!!!")