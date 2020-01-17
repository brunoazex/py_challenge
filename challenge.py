import pandas as pd
from database import Database

class Challenge():    
    def one():
        """
        The number of transactions and the total value purchased of each credit card grouped by card number and card family.
        """
        (fields, rows) = Database.query("""
            SELECT
                c.card_family,
                c.card_number,
                t.id AS transaction_id,
                t.value,
                f.fraud_flag
            FROM
                cards c
            LEFT JOIN
                transactions t on c.card_number = t.card_number
            LEFT JOIN
                frauds f on t.id = f.transaction_id""")
    
        data_frame = pd.DataFrame(rows, columns=fields)
        pivot = data_frame.pivot_table(index=['card_family', 'card_number'],
                                values=['transaction_id', 'fraud_flag', 'value'],
                                aggfunc={
                                    'transaction_id': 'count',
                                    'fraud_flag': 'sum',
                                    'value': 'sum'
                                })
        subtotals = [
                d.append(d.sum().rename((k, 'Subtotal')))
                for k, d in pivot.groupby(level=0)
            ]        
        grand_total = pivot \
            .sum() \
            .rename(('Grand', 'Total'))
            
        pivot = pd \
            .concat(subtotals) \
            .append(grand_total) \
            .rename(columns={
                'transaction_id': 'transactions',
                'fraud_flag': 'frauds',
                'value': 'amount'
            })
        return pivot
    
    def two():
        """
        All the customer ids that have "Diamond" segment and made at least 40 transactions.
        """
        (fields, rows) = Database.query("""
                SELECT
                    cust.id AS customer_id,
                    count(*) AS transactions_count
                FROM
                    transactions t
                INNER JOIN
                    cards crd ON t.card_number = crd.card_number
                INNER JOIN
                    customers cust ON crd.customer_id = cust.id
                WHERE
                    cust.segment = 'Diamond'
                GROUP BY
                    cust.segment, cust.id
                HAVING
                    COUNT(*) >= 40
                ORDER BY
                    COUNT(*) DESC
            """)
        data_frame = pd.DataFrame(rows, columns=fields)
        return data_frame            
   