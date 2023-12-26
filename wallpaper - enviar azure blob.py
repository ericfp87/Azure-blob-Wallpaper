from azure.storage.blob import BlobClient
import os

cadeia_conexao = 'DefaultEndpointsProtocol=https;AccountName=bulbeenergia;AccountKey=EDCC5GAqNRf32VKfViuLP2ySXjlodeY3zWMFUMk5RJdFqz58KUqT+bAibtknl+xFZ2bVbTCuopS9+AStlDBqMA==;EndpointSuffix=core.windows.net'

for arquivo in os.listdir("G:\\Drives compartilhados\\Bulbers\\Recursos Humanos\\Wallpaper"):
    novo_nome_arquivo_blob = 'RH/wallpaper/fundo-tela-note.png'


    blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-bulbe", blob_name=novo_nome_arquivo_blob)

    with open("G:\\Drives compartilhados\\Bulbers\\Recursos Humanos\\Wallpaper\\" + arquivo, "rb") as data:
        blob.upload_blob(data, overwrite=True)





# from azure.storage.blob import BlobClient
# import os



# cadeia_conexao = 'DefaultEndpointsProtocol=https;AccountName=bulbeenergia;AccountKey=EDCC5GAqNRf32VKfViuLP2ySXjlodeY3zWMFUMk5RJdFqz58KUqT+bAibtknl+xFZ2bVbTCuopS9+AStlDBqMA==;EndpointSuffix=core.windows.net'

# for arquivo in os.listdir("G:\\Drives compartilhados\\RH - DP\\01 - RH 2022\\35 - Outros\\9. Wallpaper"):
#     arquivo_blob = 'RH/wallpaper/' + arquivo


# blob = BlobClient.from_connection_string(conn_str=cadeia_conexao, container_name="datalake-bulbe", blob_name=arquivo_blob)

# with open("G:\\Drives compartilhados\\RH - DP\\01 - RH 2022\\35 - Outros\\9. Wallpaper\\" + arquivo, "rb") as data:
#     blob.upload_blob(data, overwrite = True)