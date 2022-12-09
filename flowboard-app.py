import urllib3
import pandas as pd
import datetime as dt
from requests_kerberos import OPTIONAL, HTTPKerberosAuth
from openpyxl import load_workbook
import io
import streamlit as st
from PIL import Image
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

pd.options.display.float_format = "{:,.0f}".format
urllib3.disable_warnings()

fc = "MAD4"
logo = Image.open("FLOW_01.png")


url = f"https://rodeo-dub.amazon.com/{fc}/CSV/ExSD?isEulerUpgraded=ALL&processPath=PPHOV&processPath=PPSingleMedium&processPath=PPNonCon&processPath=PPMultiWrap&processPath=PPMultiMedium&processPath=PPNonConTeamLift&processPath=PPMultiTBYB&processPath=&fnSku=&fulfillmentServiceClass=ALL&exSDRange.quickRange=ALL&isEulerPromiseMiss=ALL&zAxis=PROCESS_PATH&sortCode=&isEulerExSDMiss=ALL&exSDRange.dailyEnd=00%3A00&exSDRange.dailyStart=00%3A00&yAxis=WORK_POOL&isReactiveTransfer=ALL&minPickPriority=MIN_PRIORITY&fracs=ALL&shipMethod=&shipmentTypes=CUSTOMER_SHIPMENTS&_workPool=on&_workPool=on&_workPool=on&_workPool=on&workPool=PredictedCharge&workPool=PlannedShipment&workPool=ReadyToPick&workPool=ReadyToPickHardCapped&workPool=ReadyToPickUnconstrained&workPool=PickingNotYetPicked&workPool=PickingNotYetPickedPrioritized&workPool=PickingNotYetPickedNotPrioritized&workPool=PickingNotYetPickedHardCapped&workPool=CrossdockNotYetPicked&workPool=PickingPicked&workPool=PickingPickedInProgress&workPool=PickingPickedInTransit&workPool=PickingPickedRouting&workPool=PickingPickedAtDestination&workPool=Inducted&workPool=RebinBuffered&workPool=Sorted&workPool=GiftWrap&workPool=Packing&workPool=Scanned&workPool=ProblemSolving&workPool=ProcessPartial&workPool=SoftwareException&workPool=Crossdock&workPool=PreSort&workPool=TransshipSorted&workPool=Palletized&giftOption=ALL&shipOption="
url2 = "https://monitorportal.amazon.com/mws?Action=GetGraph&Version=2007-07-07&SchemaName1=Service&DataSet1=Prod&Marketplace1=MAD4&HostGroup1=ALL&Host1=ALL&ServiceName1=LagrangeModelService&MethodName1=LagrangeModelTask&Client1=ALL&MetricClass1=NONE&Instance1=NONE&Metric1=OUTBOUND.CurrentMultisOverrideCapacity&Period1=FiveMinute&Stat1=avg&LiveData1=true&Label1=Service%20OUTBOUND.CurrentMultisOverrideCapacity&SchemaName2=Search&Pattern2=dataset%3D%24Prod%24%20marketplace%3D%24MAD4%24%20hostgroup%3D%24ALL%24%20host%3D%24ALL%24%20servicename%3D%24PythiaCLI%24%20methodname%3D%24RawDataAggregator%24%20client%3D%24PythiaCLI%24%20metricclass%3D%24NONE%24%20instance%3D%24NONE%24%20PACK.EACH.Count%20NOT%20Fracs%20NOT%20metric%3D%28%24PPHOV.PACK.EACH.Count%24%20OR%20%24PPSingleNoSLAM.PACK.EACH.Count%24%20OR%20%24PPSingleMedium.PACK.EACH.Count%24%20OR%20%24PPSmartPac.PACK.EACH.Count%24%20OR%20%24PPMulti80.PACK.EACH.Count%24%20OR%20%24PPMulti20.PACK.EACH.Count%24%20OR%20%24PPMulti20Zone.PACK.EACH.Count%24%29%20Multi%20schemaname%3DService&Stat2=sum&SchemaName3=Service&Metric3=OUTBOUND.CurrentOSPMultisCapacity&Stat3=avg&Label3=Service%20OUTBOUND.CurrentOSPMultisCapacity&HeightInPixels=350&WidthInPixels=700&GraphTitle=LAGRANGE%20MULTIS&DecoratePoints=true&Palette=cloudwatch&TZ=Europe%2FMadrid@TZ%3A%20Madrid&StartTime1=-PT3H&EndTime1=-PT0H&FunctionExpression1=M1&FunctionLabel1=Multis%20Override%20%5Blast%3A%20%7Blast%7D%5D&FunctionYAxisPreference1=left&FunctionExpression2=SUM%28S2%29*12&FunctionLabel2=Multis%20OB%20Pack%20%5Blast%3A%20%7Blast%7D%5D&FunctionYAxisPreference2=left&FunctionExpression3=M3&FunctionLabel3=ALPS%20Multis%5Blast%3A%20%7Blast%7D%5D&FunctionYAxisPreference3=left&OutputFormat=CSV_TRANSPOSE"
url3 = "https://monitorportal.amazon.com/mws?Action=GetGraph&Version=2007-07-07&SchemaName1=Service&DataSet1=Prod&Marketplace1=MAD4&HostGroup1=ALL&Host1=ALL&ServiceName1=LagrangeModelService&MethodName1=LagrangeModelTask&Client1=ALL&MetricClass1=NONE&Instance1=NONE&Metric1=OUTBOUND.CurrentSinglesOverrideCapacity&Period1=FiveMinute&Stat1=avg&LiveData1=true&Label1=Service%20OUTBOUND.CurrentSinglesOverrideCapacity&SchemaName2=Search&Pattern2=dataset%3D%24Prod%24%20marketplace%3D%24MAD4%24%20hostgroup%3D%24ALL%24%20host%3D%24ALL%24%20servicename%3D%24PythiaCLI%24%20methodname%3D%24RawDataAggregator%24%20client%3D%24PythiaCLI%24%20metricclass%3D%24NONE%24%20instance%3D%24NONE%24%20PACK.EACH.Count%20NOT%20Fracs%20NOT%20metric%3D%28%24PPAFE1.PACK.EACH.Count%24%20OR%20%24PPAFE2.PACK.EACH.Count%24%20OR%20%24PPHOV.PACK.EACH.Count%24%29%20schemaname%3DService%20Single%20OR%20SmartPac&Stat2=sum&SchemaName3=Service&Metric3=OUTBOUND.CurrentOSPSinglesCapacity&Stat3=avg&Label3=Service%20OUTBOUND.CurrentOSPSinglesCapacity&HeightInPixels=350&WidthInPixels=700&GraphTitle=LAGRANGE%20SINGLES&DecoratePoints=true&Palette=cloudwatch&TZ=Europe%2FMadrid@TZ%3A%20Madrid&StartTime1=-PT3H&EndTime1=-PT0H&FunctionExpression1=M1&FunctionLabel1=Singles%20Override%20%5Blast%3A%20%7Blast%7D%5D&FunctionYAxisPreference1=left&FunctionExpression2=SUM%28S2%29*12&FunctionLabel2=Singles%20OB%20Pack%20%5Blast%3A%20%7Blast%7D%5D&FunctionYAxisPreference2=left&FunctionExpression3=M3&FunctionLabel3=ALPS%20Singles%5Blast%3A%20%7Blast%7D%5D&FunctionYAxisPreference3=left&OutputFormat=CSV_TRANSPOSE"


def requests_retry_session(retries=10,
                           backoff_factor=0.3,
                           status_forcelist=(500, 502, 503, 504),
                           session=None):

    session = session or requests.Session()

    retry = Retry(total=retries,
                  read=retries,
                  connect=retries,
                  backoff_factor=backoff_factor,
                  status_forcelist=status_forcelist)

    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def get_nextCPT (df):
    ExSD_list = ["02:30","03:00","03:30","06:45","10:45","14:30","18:45","19:15","19:45","23:00","23:30"]
    df['ExSD'] = pd.to_datetime(df['ExSD'])
    df['ExSD_str'] = df['ExSD'].dt.strftime('%H:%M')
    df = df[df['ExSD_str'].isin(ExSD_list)]
    now = dt.datetime.now()
    minT = df['ExSD'].min()
    
    PADtime = ((minT - now)- pd.Timedelta(minutes=20))
    PADtime = PADtime.total_seconds()/60
    nextCPT = df.loc[df['ExSD'] == minT]['ExSD_str'].min()
    
    return PADtime,nextCPT


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




def pull_rodeo_csv(url):
    resp = requests_retry_session().get(url,
                                    auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),
                                    verify=False,
                                    allow_redirects=True,
                                    timeout=30)

    if resp.status_code == 200:

        csv_data = resp.content

        if csv_data is not None:
            
            rawData = pd.read_csv(io.StringIO(csv_data.decode('utf-8')))
            df = rawData.dropna(axis=0, thresh=4)
            df = df.groupby(['Process Path', 'Work Pool','ExSD']).agg({'Quantity': 'sum'}).reset_index()
            

        else:
            print("No Data")
    
    else:
        print(resp.raise_for_status())

    return df

st.set_page_config(
    page_title=f"{fc} OB Flowboard",
    page_icon=logo,
    layout="wide"
)

#Pull Rodeo data
df = pull_rodeo_csv(url)

#Pull Lagrange values for MultiMedium (Current capacity + LG Override)
LG_MM = pull_igraph_csv(url2)
LG_MM = LG_MM.drop([0,1,2,3,4]).set_index('Id').dropna(axis=0)
MMCap = LG_MM['Label=Multis OB Pack [last: {last}]'].iat[-1]
MMCap = int(float(MMCap))
MM_OR = LG_MM['Label=Multis Override [last: {last}]'].iat[-1]
MM_OR = int(float(MM_OR))

#Pull Lagrange values for SingleMedium (Current capacity + LG Override)
LG_SM = pull_igraph_csv(url3)
LG_SM = LG_SM.drop([0,1,2,3,4]).set_index('Id').dropna(axis=0)
SMCap = LG_SM['Label=Singles OB Pack [last: {last}]'].iat[-1]
SMCap = int(float(SMCap))
SM_OR = LG_SM['Label=Singles Override [last: {last}]'].iat[-1]
SM_OR = int(float(SM_OR))

#Get Next ExSD + minutes to next ExSD PADTimev
PADtime, nextCPT = get_nextCPT(df)

#Calculating %CAPS globally
url4 = "https://monitorportal.amazon.com/mws?Action=GetGraph&Version=2007-07-07&SchemaName1=Service&DataSet1=Prod&Marketplace1=MAD4&HostGroup1=ALL&Host1=ALL&ServiceName1=SkynetCapacityModelService&MethodName1=RetrieveRodeoBuffers&Client1=ALL&MetricClass1=NONE&Instance1=NONE&Metric1=WorkPoolSize.PPSingleMedium.PickingNotYetPickedPrioritized&Period1=FiveMinute&Stat1=avg&Label1=WorkPoolSize.PPSingleMedium.PickingNotYetPickedPrioritized&SchemaName2=Service&Metric2=WorkPoolSize.PPMultiMedium.ReadyToPickUnconstrained%20&Label2=WorkPoolSize.PPMultiMedium.ReadyToPickUnconstrained&SchemaName3=Service&Metric3=WorkPoolSize.PPSingleMedium.PickingNotYetPickedHardCapped&Label3=WorkPoolSize.PPSingleMedium.PickingNotYetPickedHardCapped&SchemaName4=Service&Metric4=WorkPoolSize.PPMultiMedium.ReadyToPickHardCapped&Label4=WorkPoolSize.PPMultiMedium.ReadyToPickHardCapped&SchemaName5=Service&Metric5=WorkPoolSize.PPSingleMedium.PickingNotYetPickedNotPrioritized&Label5=WorkPoolSize.PPSingleMedium.PickingNotYetPickedNotPrioritized&SchemaName6=Service&Metric6=WorkPoolSize.PPMultiWrap.ReadyToPickHardCapped&Label6=WorkPoolSize.PPMultiWrap.ReadyToPickHardCapped&SchemaName7=Service&Metric7=WorkPoolSize.PPMultiWrap.ReadyToPickUnconstrained%20&Label7=WorkPoolSize.PPMultiWrap.ReadyToPickUnconstrained&HeightInPixels=500&WidthInPixels=900&GraphTitle=MAD4%20TCAPs&Palette=cloudwatch&TZ=Europe%2FMadrid@TZ%3A%20Madrid&ShowGaps=false&UpperValueLeft=50000&LowerValueLeft=0&LabelLeft=Units%20%28k%29&UpperValueRight=100&LowerValueRight=0&LabelRight=Percentage&StartTime1=-PT8H&EndTime1=-PT0H&FunctionExpression1=%28M3%2BM4%2BM6%29&FunctionLabel1=Hardcapped%20units%20%5B%7Blast%7D%20k%5D&FunctionYAxisPreference1=left&FunctionExpression2=%28M1%2BM2%2BM5%2BM7%29&FunctionLabel2=Available%20units%20PNYP%20%5B%7Blast%7D%20k%5D&FunctionYAxisPreference2=left&FunctionExpression3=%28M3%2BM4%2BM6%29%2F%28M1%2BM2%2BM3%2BM4%2BM5%2BM6%2BM7%29*100&FunctionLabel3=Percentage%20TCAPs%20%5B%7Blast%7D%20%25%5D&FunctionYAxisPreference3=right&OutputFormat=CSV_TRANSPOSE"
df_caps = pull_igraph_csv(url4)
df_caps = df_caps.drop([0,1,2,3,4]).set_index('Id').dropna(axis=0)
pct_CAPS = df_caps['Label=Percentage TCAPs [{last} %]'].iat[-1]
pct_CAPS = ("%.0f%%" % (int(float(pct_CAPS))))

#Calculate MultiMedium %CAPS
MM_CAPS = (df.loc[(df['Work Pool'] == "PickingNotYetPickedNonPickable") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum())+(df.loc[(df['Work Pool'] == "ReadyToPickNonPickable") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum())
MM_NoCAPS = (df.loc[(df['Work Pool'] == "PickingNotYetPicked") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum())+(df.loc[(df['Work Pool'] == "ReadyToPick") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum())
MM_CAPS_pct = MM_CAPS/MM_NoCAPS
MM_CAPS_pct = ("%.0f%%" % (MM_CAPS_pct*100))

#Calculate SingleMedium %CAPS
SM_CAPS = df.loc[(df['Work Pool'] == "PickingNotYetPickedNonPickable") & (df['Process Path'] == "PPSingleMedium"),'Quantity'].sum()
SM_NoCAPS = df.loc[(df['Work Pool'] == "PickingNotYetPicked") & (df['Process Path'] == "PPSingleMedium"),'Quantity'].sum()
SM_CAPS_pct = SM_CAPS/SM_NoCAPS
SM_CAPS_pct = ("%.0f%%" % (SM_CAPS_pct*100))


#Displaying FlowBoard - Sidebar
with st.sidebar:
    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.image(logo, width=60)
        st.write(f"Next CPT: **{nextCPT}**")
        st.write(f"**{round(int(PADtime))}** Mins to PAD time")

    with col2:
        st.header(f"{fc} OB Flowboard")
        
    
    c1, c2, c3 = st.columns(3,gap="small")
    with c1:
        st.metric(label="LG Single", value=SMCap, delta= SMCap-SM_OR)
        st.metric(label="Single CAPS %", value=SM_CAPS_pct)
        
    with c2:
        st.metric(label="LG Multi", value=MMCap, delta= MMCap - MM_OR)
        st.metric(label="Multi CAPS %", value=MM_CAPS_pct)
    with c3:
        st.metric(label="LG Total", value=(SMCap+MMCap), delta=(SMCap+MMCap) - (SM_OR+MM_OR) )
        st.metric(label="Total CAPS %", value= pct_CAPS)
    


SM_PP = df.loc[(df['Work Pool'] == "PickingPicked") & (df['Process Path'] == "PPSingleMedium"),'Quantity'].sum()
SM_PNYP_UC = (df.loc[(df['Work Pool'] == "PickingNotYetPickedNotPrioritized") & (df['Process Path'] == "PPSingleMedium"),'Quantity'].sum()) + (df.loc[(df['Work Pool'] == "PickingNotYetPickedPrioritized") & (df['Process Path'] == "PPSingleMedium"),'Quantity'].sum())
SM_PNYP = df.loc[(df['Work Pool'] == "PickingNotYetPicked") & (df['Process Path'] == "PPSingleMedium"),'Quantity'].sum()
MM_R2P_UC = df.loc[(df['Work Pool'] == "ReadyToPickUnconstrained") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum()
MM_PNYP_UC = (df.loc[(df['Work Pool'] == "PickingNotYetPickedNotPrioritized") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum()) + (df.loc[(df['Work Pool'] == "PickingNotYetPickedPrioritized") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum())
MM_PP = df.loc[(df['Work Pool'] == "PickingPicked") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum()
MM_RB = df.loc[(df['Work Pool'] == "RebinBuffered") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum()
MM_SRT = df.loc[(df['Work Pool'] == "Sorted") & (df['Process Path'] == "PPMultiMedium"),'Quantity'].sum()

placeholder = st.empty()

with placeholder.container():
    
    u1,u2,u3,u4,u5,u6 = st.columns(6, gap="small")

    with u1:
        st.header("Single")
    with u2:
        st.metric(label="Pickable Units", value=SM_PNYP_UC)
    with u3:
        st.metric(label="PickingPicked", value=SM_PP)
    with u4:
        st.empty()
    with u5:
        st.empty()     
    with u6:
        st.metric(label="Pickable Backlog", value=MM_R2P_UC+MM_PNYP_UC+SM_PNYP_UC)

    st.markdown("""---""")

    u1,u2,u3,u4,u5,u6 = st.columns(6, gap="small")

    with u1:
        st.header("Multi")
    with u2:
        st.metric(label="Unconstrained Units", value=MM_R2P_UC)
    with u3:
        st.metric(label="PickingNotYetPicked", value=MM_PNYP_UC)
    with u4:
        st.metric(label="PickingPicked", value=MM_PP)
    with u5:
        st.metric(label="RebinBuffered", value=MM_RB)
    with u6:
        st.metric(label="Sorted", value=MM_SRT)

    st.markdown("""---""")




    

