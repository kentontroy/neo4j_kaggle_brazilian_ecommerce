import logging
import query_strings as q_strings
import os
import random

from dotenv import load_dotenv
from neo4j import GraphDatabase
from typing import Dict, List

# Load environment variables from .env file
load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s \n %(message)s" 
)
logger = logging.getLogger(__name__)

# Access environment variables
URI=os.getenv("NEO4J_URI")
USERNAME=os.getenv("NEO4J_USERNAME")
PASSWORD=os.getenv("NEO4J_PASSWORD")

def getSampleCustomerIds()->List[str]:
    customer_ids = []
    try:
        with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
            driver.verify_connectivity()
            drs = driver.session()
            res = drs.run(q_strings.GET_DEMO_CUSTOMER_IDS)
            for rec in res:
                customer_ids.append(rec["id"])
            drs.close()

    except Exception as e:
        raise Exception(f"An error occurred in getSampleCustomerIds: {e}")
    
    return customer_ids

def getTierForCustomerId(customer_id: str)->str:
    tier = ""
    try:
        with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
            driver.verify_connectivity()
            drs = driver.session()
            res = drs.run(q_strings.GET_TIER, customer_id=customer_id)
            for rec in res:
                tier = rec["tier"]            
                break
            drs.close()

    except Exception as e:
        raise Exception(f"An error occurred in getTierForCustomerId: {e}")

    return tier

def getTiersForAllSampleCustomers()->Dict[str, str]:
    tiers = {}
    try:
        with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
            driver.verify_connectivity()
            drs = driver.session()
            res = drs.run(q_strings.GET_TIERS_FOR_ALL_SAMPLE)
            for rec in res:
                tiers[rec["customer_id"]] = rec["tier"]
            drs.close()

    except Exception as e:
        raise Exception(f"An error occurred in getTiersForAllSampleCustomers: {e}")

    return tiers

def getPromotionsForAllTiers()->Dict[str, str]:
    promotions = {}
    try:
        with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
            driver.verify_connectivity()
            drs = driver.session()
            res = drs.run(q_strings.GET_PROMOTIONS_FOR_ALL_TIERS)
            for rec in res:
                promotions["diamond"] = rec["diamond"]
                promotions["gold"] = rec["gold"]
                promotions["silver"] = rec["silver"]
                promotions["member"] = rec["member"]
                break
            drs.close()

    except Exception as e:
        raise Exception(f"An error occurred in getPromotionsForAllTiers: {e}")

    return promotions

def getPromotionsForCustomerId(customer_id: str)->str:
    try:
        tier = getTierForCustomerId(customer_id)
        all_promotions: {} = getPromotionsForAllTiers()
        promotions = all_promotions[tier.lower()]
        return promotions

    except Exception as e:
        raise Exception(f"An error occurred in getPromotionsForCustomerId: {e}")

if __name__ == "__main__":
# Execute all APIs to test
    customer_ids = getSampleCustomerIds()
    logger.info(customer_ids)

    tier = getTierForCustomerId(random.choice(customer_ids))
    logger.info(tier)

    tiers = getTiersForAllSampleCustomers()
    logger.info(tiers)

#    promotions = getPromotionsForAllTiers()
#    logger.info(promotions)

#    promotions = getPromotionsForCustomerId(random.choice(customer_ids))
#    logger.info(promotions)

