from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from googleapiclient.discovery import build
import io
import re
from apiclient import errors

# разрешения сервиса
SCOPES = ['https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets']
# данные для авторизации
SERVICE_ACCOUNT_FILE = 'googlecreds.json'
# id редактируемой папки 
folder_id = '1ZdNqAQ7AZkb_d6fjWGJ7tPCuetAcNwyS'
# авторизация и инициализация сервисов
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)
sheets_service = build('sheets', 'v4', credentials=credentials)
# id таблицы
table_id = '1AfTTr1Q5AfINtmnR_nPYvuEi2B-CG_NMRkRoqGLIpoE'

def get_data():
    sheet_name = sheets_service.spreadsheets().get(spreadsheetId=table_id, ranges=[]).execute()['sheets'][0]['properties']['title']
    data = sheets_service.spreadsheets().values().batchGet(spreadsheetId=table_id,
                                                    ranges=sheet_name).execute()['valueRanges'][0]['values']
    response = []
    for record in data[1:len(data)]:
        if '' not in record and data.index(record) != 0:
            data.remove(record)
    for record in data[1:len(data)]:
        new_item = [record[0], record[1]]
        for i in range(2, len(record)):
            if record[i] == '':
                new_item.append(data[0][i])
        response.append(new_item)
    return response
