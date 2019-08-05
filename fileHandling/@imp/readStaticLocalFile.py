import logging
import urllib
import pandas as  pd
import pandas_gbq as pdgb
import os
import shutil
import datetime

logger = logging.getLogger()

def readCompleteFileAsString(fileName = "../fileHandling/src_file/sample_ar_adjustments_all_1.csv"):
	with open(fileName, 'r') as f1:
		data = f1.read()

	print("data : ", data)
	print("type(data)", type(data))


def readLineWise(fileName = "../fileHandling/src_file/sample_ar_adjustments_all_1.csv"):
	with open(fileName, 'r') as f2:
		data = f2.readline(2) # read just 1st line and return a string.(x): string of length x (starting x charecters)
		print("inside data : ", data)
		print("inside type(data)", type(data))

	print("outside data : ", data)
	print("outside type(data)", type(data))


def readLinesWise(fileName = "../fileHandling/src_file/sample_ar_adjustments_all_1.csv"):
	with open(fileName, 'r') as f2:
		data = f2.readlines(2) # inside data and outside data are same
		print("inside data : ", data)
		print("inside type(data)", type(data))

	print("outside data : ", data)
	print("outside type(data)", type(data))

print("calling readLineWise", readLineWise())
print("calling readLinesWise", readLinesWise())




#
#
# def task():
#     logger.info('Starting')
#     try:
#     	df = pd.read_csv(EV.File_path+'Customer_Care/Agent_Summary.csv',dtype = {'Contact_Name': str},low_memory=False)
#     	for col in list(df.columns):
#            df[col] = df[col].apply(lambda x: x.replace(u'\r', u' ').replace(u'\n',u' ') if isinstance(x, str) or isinstance(x, unicode) else x)
#         pdgb.to_gbq(df,'Datahub.INCONTACT_CC_AGENT_SUMMARY_TMP', EV.project_id,if_exists='replace')
# 	dest_folder='/home/IT_Admin/Orchestration_New/Source Files/Customer_Care/Archive/'
# 	src_folder='/home/IT_Admin/Orchestration_New/Source Files/Customer_Care/'
# 	dt = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
# 	files=['Agent_Summary.csv']
# 	for f in files:
# 		shutil.copy(src_folder+f,dest_folder)
# 	os.chdir(dest_folder)
# 	src1='Agent_Summary'
# 	src='Agent_Summary.csv'
# 	tgt=src1+ dt+'.csv'
# 	os.rename(src,tgt)
# 	os.chdir('/home/IT_Admin/Orchestration_New/')
#
#         #########################################
#         response = {'Record_Count': len(df.index), 'Error_Message': 'No errors encountered.', 'Status': 'Succeeded'}
#         return response
#     except Exception as err_msg:
#         response = {'Record_Count': '0', 'Error_Message': str(err_msg), 'Status': 'Failed'}
#         return response
#
# if __name__ == '__main__':
#     task()
#
#
#
#
