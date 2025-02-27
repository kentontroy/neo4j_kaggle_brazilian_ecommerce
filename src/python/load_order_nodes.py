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

def load_order_nodes(tx, row)->None:
    cypher = """
        MERGE (o:Order {
            order_id: $order_id,
            customer_id: $customer_id,
            order_status: $order_status,
            order_purchase_timestamp: $order_purchase_timestamp
        })
        """
    result = tx.run(cypher, 
        order_id = row["order_id"],
        customer_id = row["customer_id"],
        order_status = row["order_status"],
        order_purchase_timestamp = row["order_purchase_timestamp"]
        #   order_approved_at = row["order_approved_at"],
        #   order_delivered_carrier_date = row["order_delivered_carrier_date"],
        #   order_delivered_customer_date = row["order_delivered_customer_date"],
        #   order_estimated_delivery_date = row["order_estimated_delivery_date"]
    )
    return result

if __name__ == '__main__':
    with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
        with driver.session() as session:
            df = pd.read_csv(ORDER_FILE) 
            for index, row in df.iterrows():
                result = session.execute_write(load_order_nodes, row)
                logging.info(result)