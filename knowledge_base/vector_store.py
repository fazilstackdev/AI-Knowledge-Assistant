import chromadb


client=chromadb.PersistentClient(
    path="chroma_db"
)


collection=client.get_or_create_collection(
    name="knowledge_base"
)





   
    
    
def store_chunks(
    chunks,
    embeddings,
    document_id
):
    ids=[]
    metadatas=[]
    for i  in range(len(chunks)):
        ids.append(f"{document_id}_{i}")
        metadatas.append(
            {
                "document_id":document_id
            }
        )
    collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )    
    
    

from .embeddings import model



def search_chunks(
    query,
    document_id,
    n_results=3
   ):

    query_embedding = model.encode(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=n_results,
        where={
            "document_id": document_id
        }
    )
    print("Retrieved Chunks:",
      len(results["documents"][0]))
    

    return results
    
    
    
    
    