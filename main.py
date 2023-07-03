from k_amino import Client

print("""\033[92m extractor pro by Gh[Face] and GOD KWEL999
 ______      _                  _   _____ _____
|  ____|    | |                | | |_   _|  __ \
| |__  __  _| |_ _ __ __ _  ___| |_  | | | |  | |
|  __| \ \/ / __| '__/ _` |/ __| __| | | | |  | |
| |____ >  <| |_| | | (_| | (__| |_ _| |_| |__| |
|______/_/\_\\__|_|  \__,_|\___|\__|_____|

""")

client = Client()
client.login(email=input("email:  "), password=input("password: "))
print(f"""
\n\ndevice:  {client.deviceId}
\n\nsid:  {client.sid}
\n\nsecret:  {client.secret}
\n\nuserId:  {client.uid}
""")

while True:
    try:
        object_pro = int(input('extract functions – \n\n1.get chatId \n2.get blogId \n3.get wikiId \n4.get comId \n5.get global user \n6.get userid \nselect function:  '))
        object_link = client.get_from_link(input('object link:  '))
        object_id = object_link.objectId
        ndc_info = client.get_community_info(comId=object_link.comId).json
        if object_pro == 1:
            print(f"your chatId:  {object_id}")
        
        elif object_pro == 2:
            print(f"your blogId:  {object_id}")
            
        elif object_pro == 3:
            print(f"your wiki:  {object_id}")
            
        elif object_pro == 4:
            print(f"finded ndc: {ndc_info['name']} \nyour comId:  {ndc_info['ndcId']}")
            
        elif object_pro == 5:
            user_info = client.get_user_info(userId=object_id).json
            print(f"info user: {user_info['nickname']} \nuser finded:  http://aminoapps.com/u/{user_info['aminoId']}")
            
        elif object_pro == 6:
            print(f"your userid:  {object_id}")
            
        else:
            print(f'{object_pro} – try again!')
            
    except Exception as no:
            print(no)
