import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from sanction.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음

CSV_PATH_PRODUCTS = './docs/sanctionlist/main.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)  # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        bulk_list = []
        for row in data_reader:
                bulk_list.append(SanctionMain(
                        ent_num=row[1],
                        sdn_name=row[2],
                        sdn_type=row[3],
                        program=row[4],
                        title=row[5],
                        call_sign=row[6],
                        vess_type=row[7],
                        tonnage=row[8],
                        grt=row[9],
                        vess_flag=row[10],
                        vess_owner=row[11],
                        remarks=row[12],
                        is_sdn=row[13]))
        SanctionMain.objects.bulk_create(bulk_list)

CSV_PATH_PRODUCTS = './docs/sanctionlist/add.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        bulk_list = []
        for row in data_reader:
                bulk_list.append(SanctionAdd(
                        ent_num = row[1],
                        add_num = row[2],
                        address = row[3],
                        address_more = row[4],
                        country = row[5],
                        add_remarks = row[6]))
        SanctionAdd.objects.bulk_create(bulk_list)

CSV_PATH_PRODUCTS = './docs/sanctionlist/alt.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)  # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
        bulk_list = []
        for row in data_reader:
                bulk_list.append(SanctionAlt(
                        ent_num = row[1],
                        alt_num = row[2],
                        alt_type = row[3],
                        alt_remarks = row[4]))
        SanctionAlt.objects.bulk_create(bulk_list)