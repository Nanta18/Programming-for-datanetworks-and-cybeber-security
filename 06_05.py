# Insecure
insert_data_sql = "INSERT INTO homework (last name, year of birth, time of purchase) values('Jack', '19.5.2004 14:27:50, 19.10.2023 14:16:32'); DROP TABLE homework; --)"

# Secure
insert_data_sql = "INSERT INTO homework (\"last name\", \"year of birth\", \"time of purchase\") VALUES (%s, %s, %s)"
data ['Jack', '19.5.2004 14:27:50, 19.10.2023 14:16:32'); DROP TABLE homework; --]
# Not working with same input
