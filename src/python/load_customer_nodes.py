import logging
import os
import pandas as pd
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()
CUSTOMER_FILE = os.getenv("CUSTOMER_FILE_FILTERED")
URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

def load_customer_nodes(tx, row)->None:
    cypher = """
        MERGE (c:Customer 
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