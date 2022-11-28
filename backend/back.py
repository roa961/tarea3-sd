from re import search
import grpc
from concurrent import futures
import proto_web_pb2 as pwb2
import proto_web_pb2_grpc as pwb2gc
from time import sleep
import psycopg2 as ps


class SearchService(pwb2gc.SearchServicer):
    def __init__(self, *args, **kwargs):
        pass
    def GetServerResponse(self, request, context):
        item = []
        response=[]
        message = request.message
        result = f'"{message}"'
        cur.execute("SELECT * FROM palabras;")
        qres = cur.fetchall()
        #print(qres)
        for i in qres:
            if message in i:
                item.append(i)

        print(item)
        if len(item) == 0:
            result = dict()
            result['palabra'] = "No hay datos"
            result['message'] = "No hay datos"
            response.append(result)
            return pwb2.SearchResults(web=response)
        for j in item:
            print(j[0])
            result = dict()
            result['palabra'] = j[0]
            result['par'] = j[1]
            print(result)
            response.append(result)
        print("--------")
        print(result)
        print("--------")
        print(response)
        print(pwb2.SearchResults(web=response))

        return pwb2.SearchResults(web=response)


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    pwb2gc.add_SearchServicer_to_server(SearchService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__== "__main__":
    sleep(15)
    try:
        con = ps.connect("dbname=paginas user=postgres password=postgres host=postgresql")
        print("Servidor conectado a la db")
    except:
        print("No fue posible conectarse a la db")
    cur =con.cursor()
    serv()
    