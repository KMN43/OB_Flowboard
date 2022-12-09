import urllib3
import pandas as pd
from requests_kerberos import OPTIONAL, HTTPKerberosAuth
from retryer import requests_retry_session
import io

def pull_igraph_csv(url):
    resp = requests_retry_session().get(url,
                                    auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),
                                    verify=False,
                                    allow_redirects=True,
                                    timeout=30)

    if resp.status_code == 200:

        csv_data = resp.content

        if csv_data is not None:
            
            rawData = pd.read_csv(io.StringIO(csv_data.decode('utf-8')))
            df = rawData
            

        else:
            print("No Data")
    
    else:
        print(resp.raise_for_status())

    return df

if __name__ == "__main__":
    pull_igraph_csv()