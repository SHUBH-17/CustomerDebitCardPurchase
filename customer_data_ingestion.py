import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node S3_Customer_Data_Source
S3_Customer_Data_Source_node1711172128294 = glueContext.create_dynamic_frame.from_catalog(database="sales-metadata-db", table_name="input_raw_data", transformation_ctx="S3_Customer_Data_Source_node1711172128294")

# Script generated for node Change Schema
ChangeSchema_node1711172260541 = ApplyMapping.apply(frame=S3_Customer_Data_Source_node1711172128294, mappings=[("debit_card_number", "long", "debit_card_number", "string"), ("amount_spend", "long", "total_amount_spend", "int"), ("bank_name", "string", "bank_name", "string"), ("customer_id", "long", "customer_id", "int")], transformation_ctx="ChangeSchema_node1711172260541")

# Script generated for node customer_transaction_target_table
customer_transaction_target_table_node1711172374858 = glueContext.write_dynamic_frame.from_catalog(frame=ChangeSchema_node1711172260541, database="sales-metadata-db", table_name="sales_customer_transaction", transformation_ctx="customer_transaction_target_table_node1711172374858")

job.commit()