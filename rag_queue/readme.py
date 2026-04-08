

"""
chat.py and ragpiple.py are syn ( not production level)

asyn -> lets do this in backgrround and let user do what ever he wants 

problem -> server <- req 1, req 2, req 3, req 4, req 5
solution -> queue system ( fifo ) -> first in first out
queue in system design->(fifo)

   query
     |
     |
     \/
http server ( fast api)
for queue to work -> package PYTHON RQ

this use redis as backend -> to store the query and result


IN ORDER work queue system we. need redis server running in background
1.method-> redis server running in background
2.method->valkey(replacement for redis) docker run -p 6379:6379 redis




we make worker in quue/worker.py ->
 this will process the query and return the result

 and client in client/rq_client.py -> this will add the query to the queue
   and wait for the result

   what actually we do in worker and in client -> 
   same as chat.py but in worker we will process 
   the query and return the result to the client
     and in client we will add the query to the
       queue and wait for the result
   

   fastapi server(post/chat{msg}) -> -> enque the 
   query(process)and return the result to the user

"""