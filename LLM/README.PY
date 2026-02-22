
""""
Q. WHAT IS LLM->
ANS: LLM stands for "Large Language Model".
 It is a type of artificial intelligence model that is designed to understand and generate human-like text based 
on the input it receives. LLMs are trained on vast amounts of text data and can perform a wide range of natural language processing tasks
, such as language translation, text summarization, question answering, 
and more. Examples of LLMs include OpenAI's GPT-3 and Google's BERT

    """


"""
Q.HOW LLM WORKS-> GPT-> GENERATIVE PRE-TRAINED TRANSFORMER

INPUT TOKEN->LLM->OUTPUT TOKEN
generate content on basis of previous content/pre trained

chatgpt ,gemini are transformer  which is generative in nature on basis of pre training on large data set

ANS: LLMs work by using a deep learning architecture called a transformer
, which allows them to process and generate text in a way that captures
 the context and meaning of the input.


"""


"""
Q what is transformer->
ans->transformer  which is generative in nature on basis of pre training on large data set

idea behind -> user give some input and transformer generate output on basis of pre training on large data set

eg. translation, summarization, question answering, etc
hey-> transformer (prediction)-> hola  

to ans input token only and only predict next token and repeat the process until we get the desired output

LLM reqiues gpu for training and inference because they involve complex computations and large amounts of data.
"""


"""
Q.what is Token?

ANS: A token is a unit of text that is used as input or output for language models.

eg. hii my name is bhavishya-> tokenize-> ["hii", "my", "name", "is", "bhavishya"]
convert into numbers-> [1, 2, 3, 4, 5] this is called tokenization process, which is a crucial step in natural language processing (NLP) tasks.

tokenization is the process of breaking down text into smaller units, called tokens, which can be words, subwords, or characters.

"""


"""
embeddings are a way to represent words or phrases as numerical vectors 
in a continuous vector space.

vector embeddings capture the semantic meaning of words, 
allowing language models to understand relationships between words 
and perform various NLP tasks more effectively.

eg : a dog eat cat these are words how can these words understand by 
machine-> we convert these words into numbers -> [0.1, 0.2, 0.3] this is called embedding vector


seamantic meaning of words is captured by embeddings, which allows language models 
to understand relationships between words and perform various NLP tasks more effectively.

vector embeddings store semantic meaning words

"""



"""

eg1. dog ate cat
eg2 . cat ate dog

step1-> tokenization ->[56, 78, 90]
step2 vector embeddings->
dog -> [0.1, 0.2, 0.3]
ate -> [0.4, 0.5, 0.6]
cat -> [0.7, 0.8, 0.9]

step 3-> positional encoding-> we add positional encoding to the embeddings to capture the order of words in a sentence.

positonal encoding  tells that eg 1 is differnt from 2
because 1 is first word and 2 is second word in the sentence,
 this helps the model understand the structure of the sentence and 
 the relationships between words based on their positions.

 step 4->self attension-> self attention is a mechanism that allows the model
   to weigh the importance of different words in a sentence
     when making predictions.

     eg1. river bank
     eg2. money bank

     here the word "bank" has different meanings in the two sentences,
     and self-attention helps the model understand the context and determine
     the correct meaning based on the surrounding words.



     

"""