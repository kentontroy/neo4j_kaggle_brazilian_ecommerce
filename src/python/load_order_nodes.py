import logging
import os
import pandas as pd
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()
ORDER_FILE = os.getenv("ORDER_FILE_FILTERED")
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

order_id: $order_id,
customer_id
order_status
order_purchase_timestamp
order_approved_at,
order_delivered_carrier_date
order_delivered_customer_date
order_estimated_delivery_date

def load_customer_nodes(tx, row)->None:
    cypher = """
        MERGE (o:Order
        { customer_id: $customer_id, 
          customer_unique_id: $customer_unique_id, 
          customer_zip_code_prefix: $customer_zip_code_prefix,
          customer_city: $customer_city,
          customer_state: $customer_state })
        """
    result = tx.run(cypher, 
        customer_id = row["customer_id"], 
        customer_unique_id = row["customer_unique_id"], 
        customer_zip_code_prefix = row["customer_zip_code_prefix"],
        customer_city = row["customer_city"],
        customer_state = row["customer_state"]
    )
    return result

if __name__ == '__main__':
    with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
        with driver.session() as session:
            df = pd.read_csv(CUSTOMER_FILE) 
            for index, row in df.iterrows():
                result = session.execute_write(load_customer_nodes, row)
                logging.info(result)