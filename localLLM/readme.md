local LLM deployment and api 

# there are many local llms
-> in this model we are learn how we are going to walkthrough these models offline in our machine 

there are opensource models deepseek-r1,Llama 3.3 ,Qwen 2.5-vl,gemma 3 , Llama

why are you use local LLM 
-> for privacy issue 
-> download opensuouce model 


 example -> iLlama-> they required good hardware to run locally if we download they cost much to hardware 
docker -> alternate download docker and run on docker container 
 docker is conatiner managemnet tool 

 1->doenload doker
 2-> docker run ollama/ollama 
 3-> go to ollma repo(https://hub.docker.com/r/ollama/ollama)

 and run command on ternimanl(docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
)

4-> openweb ui ( is something you download as a ui layer for ollma )

website-> https://docs.openwebui.com/getting-started/quick-start/

command 
step1-> docker pull ghcr.io/open-webui/open-webui:main

step2->run the conatiner  docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main

run localhost:3000

5-> select model for this we have to pull model 
 go to webui settings -> models
 go to ollama and search model choose a suitable model for that ( ex gemma2:2b)download and use it 


 fast api  

 integrate ollama with fast api and python api's

 pip install ollama
to run  fastapi dev server.py