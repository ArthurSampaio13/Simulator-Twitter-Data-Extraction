import sys
sys.path.append("")

from airflow.models import DAG
from datetime import datetime, timedelta
from operators.twitter_operator import TwitterOperator
from os.path import join
from airflow.utils.dates import days_ago



with DAG(dag_id= "TwitterDAG", start_date=days_ago(1), schedule_interval='@daily') as dag:
    
    query = "datascience"
    
    to = TwitterOperator(file_path=join("datalake/twitter_datascience",
                                           "extract_date={{ ds }}",
                                           "datascience {{ ds_nodash }}.json"), 
                         query=query, 
                         start_time="{{ data_interval_start.strftime('%Y-%m-%dT%H:%M:%S.00Z') }}", 
                         end_time="{{ data_interval_end.strftime('%Y-%m-%dT%H:%M:%S.00Z')}}", 
                         task_id="twitter_datascience")
        