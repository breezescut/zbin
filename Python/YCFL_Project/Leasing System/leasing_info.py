#! /usr/bin/env python

import cx_Oracle
import pandas as pd
import pandas.io.sql as psql

import os 
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# Leasing System
# 模拟用友租赁业务系统, 首先完成信息查询
class leasing_system():
    def __init__(self, db_user, db_passwd, db_ip, db_sid):
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_ip = db_ip
        self.db_sid = db_sid
        self.db_conn = None
        self.cur = None
        
        self.__dbConn__()
    
    def __dbConn__(self):
        # self.db_conn = cx_Oracle.connect(self.db_user, self.db_passwd, self.db_name)
        self.db_conn = cx_Oracle.connect("%s/%s@%s/%s" % (self.db_user, self.db_passwd, self.db_ip, self.db_sid))
        self.cur = self.db_conn.cursor()

    # 读取合同信息台账
    def get_contact_all_info(self):
        querySQL = '''
                    SELECT CT.PK_CONTRACT,
                                              CT.PK_CUSTOMER_LESSEE  PK_CUSTOMER,
                                              CT.PK_LEASE_CALCULATOR   PK_LEASE_BALANCE,
                                              CT.PK_LEASE_CALCULATOR,
                                              OVR.OVERDUE_DAYS         AS OVERDUE_DAYS,
                                              OVR.OVERDUE_CASH         AS OVERDUE_CASH,
                                              OVR.OVERDUE_CORPUS       AS OVERDUE_CORPUS,
                                              OVR.OVERDUE_INTEREST     AS OVERDUE_INTEREST,
                                              OVR.ACCRUED_PENALTY_CASH AS ACCRUED_PENALTY_CASH,
                                              OVR.FACT_PENALTY_CASH    AS FACT_PENALTY_CASH,
                                              OVR.ALREADY_REDUCE_CASH  AS ALREADY_REDUCE_CASH,
                                              OVR.ACTUAL_REDUCE_CASH   AS ACTUAL_REDUCE_CASH,
                                              OVR.OVERDUE_TIMES        AS OVERDUE_TIMES,
                                              CT.LEASE_IRR             AS FACT_CONT_IRR,
                                              CT.YEAR_INTEREST_IRR     AS YEAR_IRR,
                                              CT.PLAN_CON_NOTAX_IRR,
                                              CT.LEASE_IRR             AS CONT_IRR,
                                              CT.AUDIT_IRR,
                                              CT.LESSEE_IRR,
                                              CT.PROJECT_IRR,
                                              CT.FINANCE_IRR,
                                              CT.PROJECT_NOTAX_IRR,
                                              CT.FINANCE_NOTAX_IRR,
                                              CT.PLAN_CON_IRR,
                                              CT.RENT_IRR,
                                              CT.FEE_DISTR_IRR,
                                              CT.TS,
                                              CT.PK_CONTRACT           AS PK_CONTRACT_TEMP,
                                              CT.PLAN_LOAN_FACT,
                                              CT.LEASE_DATE_FACT,
                                              CT.CONT_END_DATE,
                                              CT.BAD_FLAG,  /*是否坏账核销标识*/
                                              PRJ.PROJECT_TYPE,
                                              LC.LEASE_METHOD,
                                              LC.contract_xirr,
                                              LC.project_irr  as  irr,/*合同收益IRR*/
                                              UOIT.USE_OFFSET_INTEREST_T ADVANCE_RENT_INTEREST,
                                              assets_classify.param_name as ASSETS_CLASSIFY,
                                               LC.RENT_TERM_IRR,
                                               pc.rp deserve_cash,
                                             /*v_contract_amout 视图取值*/
                                               ca.contract_cash, ca.corpus_plan, ca.corpus_fact,ca.not_corpus_plan,
                                               ca.rent_plan, ca.rent_fact,ca.rent_plan_balance,
                                               ca.corpus_cash_plan, ca.corpus_fact_back,ca.capital_balance,
                                               ca.interest_plan, ca.interest_fact,ca.interest_balance,
                                               ca.fee_plan, ca.fee_fact,ca.not_poundage,
                                               ca.risk_plan, ca.risk_fact,ca.not_risk,ca.risk_balance,
                                               ca.risk_interest_plan, ca.risk_fact_ex,ca.risk_interest_balance,
                                               ca.verdor_margin_plan, ca.verdor_margin_fact, ca.vendor_margin_offset, ca.back_vendor_margin,
                                               ca.not_vendor_margin,ca.vendor_margin_balance,
                                               ca.margin_plan, ca.margin_fact, ca.not_margin,ca.margin_balance_fi,
                                               ca.advance_rent_plan, ca.advance_rent_fact,ca.not_advance_rent,ca.advance_rent_balance_fi,
                                               ca.nominal_price_plan, ca.nominal_price_fact,ca.not_nominal_price,
                                               ca.servfee_plan, ca.servfee_fact ,ca.not_servfee,
                                               ca.advances_received_balance,ca.fact_cust_amt,ca.cust_cont_balance,
                                               ca.other_balance,ca.other_plan,ca.other_fact
                                          FROM YLS_CONTRACT_C CT
                                          left join v_contract_amout ca on ct.pk_contract = ca.pk_contract
                                          LEFT JOIN YLS_PROJECT_INFO PRJ
                                            ON PRJ.PK_PROJECT_INFO = CT.PK_PROJECT
                                          LEFT JOIN YLS_LEASE_CALCULATOR_C LC
                                            ON LC.PK_LEASE_CALCULATOR = CT.PK_LEASE_CALCULATOR
                                          LEFT JOIN ( select IPC.pk_Contract,
                                               NVL(IPC.OVERDUE_TIMES,0) OVERDUE_TIMES,
                                               NVL(IPC.ACCRUED_PENALTY_CASH,0.00) ACCRUED_PENALTY_CASH,
                                               NVL(IPC.FACT_PENALTY_CASH,0.00) FACT_PENALTY_CASH,
                                               NVL(IPC3.ALREADY_REDUCE_CASH,0.00) ALREADY_REDUCE_CASH,
                                               NVL(IPC.ACTUAL_REDUCE_CASH,0.00) ACTUAL_REDUCE_CASH,
                                               NVL(IPC2.OVERDUE_DAYS,0)  OVERDUE_DAYS,
                                               NVL(IPC2.Lease_Balance,0.00)  AS overdue_cash,
                                               NVL(IPC2.OVERDUE_CORPUS,0.00)   AS OVERDUE_CORPUS,
                                               NVL(IPC2.OVERDUE_INTEREST,0.00)    AS OVERDUE_INTEREST
                                          from (select Ipc.Pk_Contract,
                                                       NVL(COUNT(*),0) OVERDUE_TIMES,
                                                       SUM(NVL(IPC.LEASE_CASH, 0.00)) accrued_penalty_cash,  /*应记逾期租金*/
                                                       SUM(NVL(IPC.fact_cash, 0.00)) fact_penalty_cash,  /*实收逾期*/
                                                       SUM(NVL(IPC.lease_balance, 0.00)) actual_reduce_cash
                                                  from YLS_INOUT_PLAN_C IPC
                                                  left join YLS_EVENT_TYPE ET
                                                    ON IPC.TRANS_TYPE = ET.PK_EVENT_TYPE
                                                 where et.event_code in ('10213')
                                                 group by IPC.Pk_Contract) IPC
                                                  left join
                                                  (select Ipc.Pk_Contract,
                                                 SUM(NVL(IPC.Lease_Balance, 0.00)) Lease_Balance, /* 逾期租金*/
                                                  (SUM(NVL(IPC.LEASE_CORPUS,0.00))-  sum(NVL(IPC.FACT_CORPUS,0))) OVERDUE_CORPUS,
                                                  (SUM(NVL(IPC.LEASE_INTEREST,0.00))-  sum(NVL(IPC.Fact_Interest,0))) OVERDUE_INTEREST,
                                                 NVL(MAX(OV.OVERDUE_DATE),0) OVERDUE_DAYS /* 逾期最大天数*/
                                            from YLS_OVERDUE_RECORD OV
                                            LEFT JOIN YLS_INOUT_PLAN_C IPC
                                              ON IPC.PK_INOUT_PLAN = OV.PK_INOUT_PLAN
                                            left join YLS_EVENT_TYPE ET
                                              ON IPC.TRANS_TYPE = ET.PK_EVENT_TYPE
                                           where OV.PK_OVERDUE_RECORD is not null
                                             and et.event_code in ('10203', '10201')
                                             and IPC.CHARGE_OFF_STATUS != 2
                                           group by IPC.Pk_Contract) IPC2
                                            on IPC2.pk_contract = ipc.pk_contract
                                            left join 
                                            (select RC.Pk_Contract,suM(NVl(RC.REDUCE_INTEREST_T,0.00)) ALREADY_REDUCE_CASH from   
                                            yls_reduce_check RC group by RC.Pk_Contract 
                                             ) IPC3 on IPC3.Pk_Contract = IPC.Pk_Contract ) OVR
                                            ON CT.PK_CONTRACT = OVR.PK_CONTRACT
                                          LEFT JOIN (SELECT SUM(NVL(ADVANCES_RECEIVED, 0.00)) ADVANCES_RECEIVED,
                                                            PK_CONTRACT
                                                       FROM YLS_ADVANCES_RECEIVED
                                                      GROUP BY PK_CONTRACT) AR
                                            ON AR.PK_CONTRACT = CT.PK_CONTRACT
                                          LEFT JOIN (SELECT SUM(NVL(USE_OFFSET_INTEREST_T, 0.00)) USE_OFFSET_INTEREST_T,
                                                            PK_CONTRACT
                                                       FROM YLS_REDUCE_CHECK RC
                                                      WHERE RC.BILLSTATUS = 9
                                                      GROUP BY PK_CONTRACT) UOIT
                                            ON UOIT.PK_CONTRACT = CT.PK_CONTRACT
                                          LEFT Join (select p1.pk_parameter, p1.param_name, p1.param_code, p1.param_value
                                                      from yls_param_type p
                                                      left join yls_parameter p1
                                                        on p.pk_param_type = p1.pk_param_type
                                                     where p.param_code = '1000340'
                                                      ) assets_classify on CT.assets_classify=assets_classify.param_value
                                          left join (select sum(nvl(c.lease_cash_fin,0.00)) rp,source_bill from yls_inout_plan_c c 
                                                     inner join yls_event_type t on c.trans_type=t.pk_event_type 
                                                     and t.event_code in ('10201','10203')
                                                     group by c.source_bill 
                                                    )pc on ct.pk_lease_calculator=pc.source_bill
                    '''

        rows = psql.read_sql(querySQL, self.db_conn)
        rows.to_csv('xx.csv')
        print(rows)

if __name__ == '__main__':
    lsc = leasing_system('ycjrzl_readonly', 'ycjrzl_readonly', '100.100.0.112', 'ORCL')
    lsc.get_contact_all_info()

